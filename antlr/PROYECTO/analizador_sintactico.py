# Helper del analizador SINTACTICO (criterio 3 del proyecto).
#
# Recibe el lexer + flujo de tokens ya construidos por AnalizadorLexico
# (analizador_lexico.py) y corre el parser de ANTLR correspondiente al
# tipo de lenguaje ("html" o "css"), capturando errores sintacticos con
# su propio ErrorListener (igual que se hace para el lexico) y dejando
# disponible el arbol de derivacion para mostrarlo en app.py y para que
# el analizador semantico (analizador_semantico.py) lo recorra despues.
from antlr4.error.ErrorListener import ErrorListener

from HTMLParser import HTMLParser
from CSSParser import CSSParser


# Clase para guardar errores sintacticos
class ErroresSintacticos(ErrorListener):

    def __init__(self):

        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Mapa de parsers y regla inicial ("simbolo distinguido") por lenguaje
_PARSERS = {
    "html": HTMLParser,
    "css": CSSParser,
}

_REGLA_INICIAL = {
    "html": "htmlDocument",
    "css": "styleSheet",
}


class AnalizadorSintactico:

    # Constructor: recibe el tipo de lenguaje ("html" o "css")
    def __init__(self, tipo):

        if tipo not in _PARSERS:
            raise ValueError(f"Tipo de lenguaje no soportado: {tipo}")

        self.tipo = tipo
        self._clase_parser = _PARSERS[tipo]
        self._regla_inicial = _REGLA_INICIAL[tipo]

        self.parser = None
        self.arbol = None
        self.errores = ErroresSintacticos()

    # Metodo para analizar un flujo de tokens ya generado por el analizador
    # lexico. Retorna el arbol de derivacion (parse tree).
    def analizar(self, flujo_tokens):

        # Creamos el parser correspondiente al tipo de lenguaje
        self.parser = self._clase_parser(flujo_tokens)

        # Quitamos los errores normales de ANTLR (que imprimen en consola)
        self.parser.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.parser.addErrorListener(self.errores)

        # Invocamos la regla inicial de la gramatica (htmlDocument / styleSheet)
        regla_inicial = getattr(self.parser, self._regla_inicial)
        self.arbol = regla_inicial()

        return self.arbol

    # Metodo para obtener errores sintacticos
    def obtener_errores(self):

        return self.errores.lista

    # Metodo para obtener una representacion en texto del arbol de derivacion,
    # util para mostrarla en la interfaz de Streamlit
    def obtener_arbol_texto(self):

        if self.arbol is None or self.parser is None:
            return ""

        return self.arbol.toStringTree(recog=self.parser)

    # Metodo para saber si el analisis sintactico fue exitoso
    def es_valido(self):

        return len(self.errores.lista) == 0
