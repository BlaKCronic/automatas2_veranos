# Validador de CONTENIDO, separado a proposito de Archivo (archivo.py).
#
# Archivo.es_html()/es_css() solo miran el nombre del archivo (la
# extension). Eso no evita que alguien suba un .txt renombrado a .html,
# o un .css que en realidad es un archivo de texto cualquiera. Este
# modulo hace una segunda validacion, esta vez mirando el CONTENIDO,
# con heuristicas de "sniffing" basadas en patrones tipicos de cada
# lenguaje (no requiere parsear todavia, es una revision rapida antes
# de gastar el analisis lexico/sintactico completo).
import re


# Patron de una etiqueta HTML: <tag ...>, </tag> o <tag .../>
_PATRON_TAG_HTML = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^<>]*)?/?>")

# Patron de un doctype html
_PATRON_DOCTYPE = re.compile(r"<!DOCTYPE\s+html", re.IGNORECASE)

# Patron de una regla CSS: selector { propiedad: valor; }
_PATRON_REGLA_CSS = re.compile(r"[.#a-zA-Z0-9_\-\*\[\]:, ]+\{[^{}]*:[^{}]*;?[^{}]*\}")

# Patron de un at-rule de CSS
_PATRON_AT_RULE_CSS = re.compile(r"@(media|import|font-face|keyframes)\b", re.IGNORECASE)


class ValidadorContenido:

    # Analiza el codigo y calcula que tan probable es que sea HTML o CSS,
    # independientemente de lo que diga la extension del archivo.
    def analizar(self, codigo):

        coincidencias_tag = _PATRON_TAG_HTML.findall(codigo)
        tiene_doctype = bool(_PATRON_DOCTYPE.search(codigo))

        coincidencias_regla_css = _PATRON_REGLA_CSS.findall(codigo)
        coincidencias_at_rule = _PATRON_AT_RULE_CSS.findall(codigo)

        puntaje_html = len(coincidencias_tag) + (5 if tiene_doctype else 0)
        puntaje_css = len(coincidencias_regla_css) + len(coincidencias_at_rule)

        if puntaje_html == 0 and puntaje_css == 0:
            tipo_probable = "desconocido"
        elif puntaje_html >= puntaje_css:
            tipo_probable = "html"
        else:
            tipo_probable = "css"

        return {
            "tipo_probable": tipo_probable,
            "puntaje_html": puntaje_html,
            "puntaje_css": puntaje_css,
            "tiene_doctype": tiene_doctype,
        }

    # Metodo principal: compara el tipo esperado (segun la extension del
    # archivo) contra el tipo que realmente parece tener el contenido.
    # Retorna (es_valido, mensaje).
    def validar(self, codigo, tipo_esperado):

        resultado = self.analizar(codigo)
        tipo_probable = resultado["tipo_probable"]

        if not codigo.strip():
            return False, "El archivo esta vacio."

        if tipo_probable == "desconocido":
            return False, (
                "El contenido no parece ni HTML ni CSS "
                "(no se encontraron etiquetas tipo <tag> ni reglas tipo selector { propiedad: valor; })."
            )

        if tipo_probable != tipo_esperado:
            return False, (
                f"La extension indica '{tipo_esperado}' pero el contenido del archivo "
                f"parece ser '{tipo_probable}' (puntaje html={resultado['puntaje_html']}, "
                f"css={resultado['puntaje_css']})."
            )

        return True, f"El contenido es consistente con '{tipo_esperado}'."
