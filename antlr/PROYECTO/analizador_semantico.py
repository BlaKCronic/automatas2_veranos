# Analizador SEMANTICO (criterio 6 del proyecto: al menos un intento de
# validacion semantica, implementado con un Listener de ANTLR que se
# recorre DESPUES de que el analisis lexico y sintactico terminaron sin
# errores fatales).
#
# Aqui tambien se resuelve el pedido del profesor de mapear "vistas,
# controladores, rutas, formularios, validaciones, plantillas, sesiones,
# cookies, peticiones GET/POST y aspectos basicos de seguridad" a algo
# concreto: como HTML/CSS no ejecutan logica de servidor (no hay
# controladores ni conexion a base de datos reales en un documento
# estatico), estos criterios se detectan como PATRONES en el marcado
# (ver Readme.md, seccion "Mapeo de requisitos web"):
#
#   <form method="GET/POST" action="...">   -> ruta + peticion HTTP
#   <input type="password">                 -> autenticacion
#   <input type="hidden">                   -> sesion / token CSRF
#   required / pattern / type=email, etc.   -> validaciones de formulario
#   <template>                              -> plantilla
#   onClick= y otros atributos "on*"        -> riesgo de seguridad (XSS)
#   target="_blank" sin rel="noopener"      -> riesgo de seguridad
#   recursos http:// en pagina https        -> contenido mixto inseguro
#
# El analizador de CSS revisa reglas propias de ese lenguaje (unidades,
# colores, orden de @import, buenas practicas con !important, etc.)
import re

from HTMLParserListener import HTMLParserListener
from CSSListener import CSSListener
from CSSParser import CSSParser


NIVEL_ERROR = "error"
NIVEL_ADVERTENCIA = "advertencia"
NIVEL_INFO = "info"

# Elementos HTML "vacios" (void elements): no llevan etiqueta de cierre
VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

METODOS_HTTP_VALIDOS = {"get", "post"}

ATRIBUTOS_DE_VALIDACION = {"required", "pattern", "min", "max", "maxlength", "minlength", "step"}

TIPOS_INPUT_CON_VALIDACION_IMPLICITA = {"email", "url", "number", "tel", "date"}

UNIDADES_CSS_VALIDAS = {
    "px", "em", "rem", "vh", "vw", "vmin", "vmax", "pt", "pc", "cm", "mm",
    "in", "ex", "ch", "fr", "deg", "rad", "grad", "turn", "s", "ms",
    "dpi", "dpcm", "dppx", "q",
}

FAMILIAS_CSS_GENERICAS = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui"}


def _texto_attr_value(ctx):
    """Extrae el texto de un attrValue (STRING sin comillas, o NAME)."""

    if ctx is None:
        return None
    if ctx.STRING() is not None:
        texto = ctx.STRING().getText()
        return texto[1:-1]
    if ctx.NAME() is not None:
        return ctx.NAME().getText()
    return None


def _posicion(ctx):

    try:
        token = ctx.start
        return token.line, token.column
    except AttributeError:
        return None, None


class _ListenerConHallazgos:
    """Funcionalidad compartida para acumular hallazgos con nivel/categoria."""

    def __init__(self):
        self.hallazgos = []

    def _agregar(self, nivel, categoria, mensaje, ctx=None):

        linea, columna = _posicion(ctx) if ctx is not None else (None, None)
        self.hallazgos.append({
            "nivel": nivel,
            "categoria": categoria,
            "mensaje": mensaje,
            "linea": linea,
            "columna": columna,
        })


# ================= LISTENER SEMANTICO PARA HTML =================

class HTMLSemanticListener(HTMLParserListener, _ListenerConHallazgos):

    def __init__(self):
        HTMLParserListener.__init__(self)
        _ListenerConHallazgos.__init__(self)
        self._conteo_tags = {"html": 0, "head": 0, "body": 0}
        self._tiene_charset = False
        self._ids_vistos = {}

    def _atributos(self, element_ctx):

        atributos = {}
        for attr_ctx in element_ctx.attribute():
            nombre = attr_ctx.attrName().NAME().getText().lower()
            valor = _texto_attr_value(attr_ctx.attrValue()) if attr_ctx.attrValue() else None
            atributos[nombre] = valor
        return atributos

    def enterHtmlDocument(self, ctx):

        if ctx.DOCTYPE() is None:
            self._agregar(NIVEL_ADVERTENCIA, "estructura",
                           "Falta la declaracion <!DOCTYPE html> al inicio del documento.", ctx)

    # Elemento vacio (void): <br>, <img>, <input>, ... nunca llevan cierre.
    # La gramatica ya lo garantiza a nivel sintactico (ver HTMLParser.g4),
    # asi que aqui solo se revisan los atributos.
    def enterVoidElement(self, ctx):

        nombre_tag = ctx.VOID_NAME().getText().lower()
        attrs = self._atributos(ctx)
        self._procesar_atributos(nombre_tag, attrs, ctx)

    # Elemento normal: <div>...</div>. La gramatica exige que, si no se
    # autocierra, tenga una etiqueta de cierre -- pero NO que el nombre
    # de esa etiqueta coincida con el de apertura. Verificar esa
    # coincidencia es, precisamente, el tipo de chequeo que corresponde
    # a la capa semantica.
    def enterNormalElement(self, ctx):

        nombre_tag = ctx.tagName().NAME().getText().lower()
        attrs = self._atributos(ctx)

        if ctx.closeTagName() is not None:
            nombre_cierre = ctx.closeTagName().NAME().getText().lower()
            if nombre_cierre != nombre_tag:
                self._agregar(NIVEL_ERROR, "estructura",
                               f"Etiqueta de cierre </{nombre_cierre}> no coincide con la apertura "
                               f"<{nombre_tag}>.", ctx)

        if nombre_tag in VOID_ELEMENTS:
            # Alguien escribio un elemento tipicamente vacio (ej. <br>) con
            # sintaxis de elemento normal, ej. "<br>texto</br>": sintacticamente
            # valido para la gramatica (br no esta en VOID_NAME si se usa asi
            # por error de tipeo), pero semanticamente incorrecto.
            self._agregar(NIVEL_ADVERTENCIA, "estructura",
                           f"<{nombre_tag}> deberia ser un elemento vacio (sin contenido ni etiqueta de "
                           f"cierre).", ctx)

        self._procesar_atributos(nombre_tag, attrs, ctx)

        # --- Estructura general del documento (html/head/body son elementos normales) ---
        if nombre_tag in self._conteo_tags:
            self._conteo_tags[nombre_tag] += 1
            if nombre_tag == "html" and "lang" not in attrs:
                self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                               "El elemento <html> no tiene atributo lang (afecta accesibilidad y SEO).", ctx)

    # Chequeos comunes a cualquier elemento (vacio o normal), basados
    # unicamente en el nombre de la etiqueta y sus atributos.
    def _procesar_atributos(self, nombre_tag, attrs, ctx):

        if nombre_tag == "meta" and attrs.get("charset") is not None:
            self._tiene_charset = True

        # --- id unicos ---
        id_valor = attrs.get("id")
        if id_valor:
            self._ids_vistos[id_valor] = self._ids_vistos.get(id_valor, 0) + 1

        # --- Formularios: rutas + peticiones GET/POST ---
        if nombre_tag == "form":
            metodo = (attrs.get("method") or "get").lower()
            if metodo not in METODOS_HTTP_VALIDOS:
                self._agregar(NIVEL_ERROR, "formulario",
                               f"El formulario usa method=\"{metodo}\", que no es GET ni POST.", ctx)
            else:
                self._agregar(NIVEL_INFO, "ruta",
                               f"Formulario detectado: peticion {metodo.upper()} hacia "
                               f"\"{attrs.get('action', '(sin action)')}\".", ctx)
            if not attrs.get("action"):
                self._agregar(NIVEL_ADVERTENCIA, "ruta",
                               "El formulario no define atributo action (ruta de destino en el servidor).", ctx)

        # --- Inputs: autenticacion, sesiones/cookies (csrf), validaciones ---
        if nombre_tag == "input":
            tipo_input = (attrs.get("type") or "text").lower()

            if tipo_input == "password":
                self._agregar(NIVEL_INFO, "autenticacion",
                               "Campo de autenticacion detectado (input type=\"password\").", ctx)
                autocomplete = (attrs.get("autocomplete") or "").lower()
                if autocomplete not in ("off", "new-password", "current-password"):
                    self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                                   "El campo de password no define autocomplete seguro "
                                   "(recomendado: autocomplete=\"new-password\"/\"current-password\").", ctx)

            if tipo_input == "hidden":
                self._agregar(NIVEL_INFO, "sesion",
                               f"Posible dato de sesion/token CSRF: input hidden name=\"{attrs.get('name')}\".", ctx)

            tiene_validacion = any(a in attrs for a in ATRIBUTOS_DE_VALIDACION) \
                or tipo_input in TIPOS_INPUT_CON_VALIDACION_IMPLICITA
            if tiene_validacion:
                self._agregar(NIVEL_INFO, "validacion",
                               f"Validacion de formulario detectada en input name=\"{attrs.get('name')}\" "
                               f"(type=\"{tipo_input}\").", ctx)

        # --- Plantillas ---
        if nombre_tag == "template":
            self._agregar(NIVEL_INFO, "plantilla", "Elemento <template> detectado (plantilla reutilizable).", ctx)

        # --- Seguridad: manejadores de eventos inline (riesgo XSS) ---
        for nombre_attr in attrs:
            if nombre_attr.startswith("on"):
                self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                               f"Atributo de evento inline \"{nombre_attr}\" en <{nombre_tag}> "
                               f"(riesgo de XSS; preferir listeners en JS externo).", ctx)

        # --- Seguridad: target=_blank sin rel=noopener/noreferrer ---
        if (attrs.get("target") or "").lower() == "_blank":
            rel = (attrs.get("rel") or "").lower()
            if "noopener" not in rel and "noreferrer" not in rel:
                self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                               f"<{nombre_tag} target=\"_blank\"> sin rel=\"noopener noreferrer\" "
                               f"(riesgo de reverse tabnabbing).", ctx)

        # --- Seguridad: recursos cargados por HTTP sin cifrar ---
        for campo in ("src", "href"):
            valor = attrs.get(campo)
            if valor and valor.lower().startswith("http://"):
                self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                               f"<{nombre_tag} {campo}=\"{valor}\"> carga un recurso por HTTP sin cifrar "
                               f"(contenido mixto).", ctx)

        # --- JS fuera de alcance ---
        if nombre_tag == "script":
            self._agregar(NIVEL_INFO, "estructura",
                           "Se detecto <script>; su contenido JS no se analiza (fuera del alcance de este "
                           "proyecto, que cubre HTML5 y CSS).", ctx)

    def exitHtmlDocument(self, ctx):

        for tag in ("html", "head", "body"):
            veces = self._conteo_tags[tag]
            if veces == 0:
                self._agregar(NIVEL_ADVERTENCIA, "estructura", f"No se encontro el elemento <{tag}>.", ctx)
            elif veces > 1:
                self._agregar(NIVEL_ADVERTENCIA, "estructura",
                               f"Se encontraron {veces} etiquetas <{tag}> (deberia haber una sola).", ctx)

        if not self._tiene_charset:
            self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                           "No se encontro <meta charset=\"...\"> (se recomienda declarar la codificacion).", ctx)

        for id_valor, veces in self._ids_vistos.items():
            if veces > 1:
                self._agregar(NIVEL_ERROR, "estructura",
                               f"El id \"{id_valor}\" esta duplicado ({veces} veces); los id deben ser unicos "
                               f"en el documento.", ctx)


# ================= LISTENER SEMANTICO PARA CSS =================

class CSSSemanticListener(CSSListener, _ListenerConHallazgos):

    def __init__(self):
        CSSListener.__init__(self)
        _ListenerConHallazgos.__init__(self)

    # --- Orden de @import: debe ir antes que cualquier regla normal ---
    def enterStyleSheet(self, ctx):

        vio_regla_normal = False
        for hijo in ctx.children or []:
            if isinstance(hijo, CSSParser.RuleSetContext):
                vio_regla_normal = True
            elif isinstance(hijo, CSSParser.AtRuleContext):
                import_ctx = hijo.importRule()
                if import_ctx is not None and vio_regla_normal:
                    self._agregar(NIVEL_ADVERTENCIA, "estructura",
                                   "@import debe declararse antes que cualquier otra regla en la hoja de "
                                   "estilos (segun la especificacion de CSS, en caso contrario los "
                                   "navegadores lo ignoran).", import_ctx)

    def _revisar_bloque_declaraciones(self, declaraciones, ctx_referencia, contexto_msg=""):

        propiedades_vistas = {}
        contador_important = 0

        for decl in declaraciones:
            nombre_prop = decl.property_().IDENT().getText().lower()
            propiedades_vistas[nombre_prop] = propiedades_vistas.get(nombre_prop, 0) + 1

            if decl.IMPORTANT() is not None:
                contador_important += 1

            for valor in decl.valueList().value():
                # Unidad no reconocida (numero pegado a una unidad, ej. "10xyz")
                if valor.DIMENSION() is not None:
                    texto = valor.DIMENSION().getText()
                    unidad = re.sub(r"^[0-9.]+", "", texto).lower()
                    if unidad not in UNIDADES_CSS_VALIDAS:
                        self._agregar(NIVEL_ADVERTENCIA, "css",
                                       f"Unidad CSS no reconocida \"{unidad}\" en la propiedad "
                                       f"\"{nombre_prop}\"{contexto_msg}.", valor)

                # Color hexadecimal con longitud invalida (#RGB, #RGBA, #RRGGBB, #RRGGBBAA)
                if valor.HASH() is not None:
                    hexadecimal = valor.HASH().getText()[1:]
                    if len(hexadecimal) not in (3, 4, 6, 8):
                        self._agregar(NIVEL_ADVERTENCIA, "css",
                                       f"Color hexadecimal \"#{hexadecimal}\" con longitud invalida "
                                       f"({len(hexadecimal)} digitos; se esperaban 3, 4, 6 u 8).", valor)

            # font-family sin familia generica de respaldo
            if nombre_prop == "font-family":
                nombres = [v.IDENT().getText().lower() for v in decl.valueList().value() if v.IDENT() is not None]
                if nombres and not any(n in FAMILIAS_CSS_GENERICAS for n in nombres):
                    self._agregar(NIVEL_INFO, "css",
                                   "font-family sin familia generica de respaldo al final "
                                   "(por ejemplo: sans-serif, serif, monospace).", decl)

        for nombre_prop, veces in propiedades_vistas.items():
            if veces > 1:
                self._agregar(NIVEL_ADVERTENCIA, "css",
                               f"La propiedad \"{nombre_prop}\" esta declarada {veces} veces dentro de la "
                               f"misma regla{contexto_msg}; solo la ultima aplica.", ctx_referencia)

        if contador_important >= 3:
            self._agregar(NIVEL_INFO, "css",
                           f"Uso frecuente de !important ({contador_important} veces) en una misma regla; "
                           f"suele indicar problemas de especificidad y dificulta el mantenimiento.",
                           ctx_referencia)

    def enterRuleSet(self, ctx):

        if len(ctx.declaration()) == 0:
            self._agregar(NIVEL_ADVERTENCIA, "css", "Regla CSS sin declaraciones (bloque vacio).", ctx)
        else:
            self._revisar_bloque_declaraciones(ctx.declaration(), ctx)

    def enterFontFaceRule(self, ctx):

        self._revisar_bloque_declaraciones(ctx.declaration(), ctx, contexto_msg=" (@font-face)")

    def enterKeyframeBlock(self, ctx):

        self._revisar_bloque_declaraciones(ctx.declaration(), ctx, contexto_msg=" (@keyframes)")

    def enterMediaRule(self, ctx):

        if len(ctx.ruleSet()) == 0:
            self._agregar(NIVEL_ADVERTENCIA, "css", "@media sin ninguna regla dentro (bloque vacio).", ctx)

    def enterImportRule(self, ctx):

        url_texto = None
        if ctx.STRING() is not None:
            url_texto = ctx.STRING().getText()[1:-1]
        elif ctx.funcCall() is not None:
            func_ctx = ctx.funcCall()
            contenido = func_ctx.funcContent()
            if contenido is not None:
                for tok in contenido.funcToken():
                    valor = tok.value()
                    if valor is not None and valor.STRING() is not None:
                        url_texto = valor.STRING().getText()[1:-1]
                        break

        if url_texto and url_texto.lower().startswith("http://"):
            self._agregar(NIVEL_ADVERTENCIA, "seguridad",
                           f"@import carga \"{url_texto}\" por HTTP sin cifrar (contenido mixto).", ctx)


# ================= COORDINADOR =================

_LISTENERS = {
    "html": HTMLSemanticListener,
    "css": CSSSemanticListener,
}


class AnalizadorSemantico:
    """Recorre el arbol de derivacion con ParseTreeWalker y un Listener
    propio, DESPUES de que el analisis lexico y sintactico terminaron.
    """

    def __init__(self, tipo):

        if tipo not in _LISTENERS:
            raise ValueError(f"Tipo de lenguaje no soportado: {tipo}")

        self.tipo = tipo
        self._clase_listener = _LISTENERS[tipo]
        self.listener = None

    def analizar(self, arbol):

        from antlr4 import ParseTreeWalker

        self.listener = self._clase_listener()
        walker = ParseTreeWalker()
        walker.walk(self.listener, arbol)
        return self.listener.hallazgos

    def obtener_hallazgos(self):

        return self.listener.hallazgos if self.listener else []
