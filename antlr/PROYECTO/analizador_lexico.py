# Importamos herramientas principales de ANTLR
from antlr4 import InputStream, CommonTokenStream, Token

# Importamos ErrorListener para capturar errores lexicos
from antlr4.error.ErrorListener import ErrorListener

# Importamos los lexers generados por ANTLR para cada lenguaje soportado
from HTMLLexer import HTMLLexer
from CSSLexer import CSSLexer


# Clase para guardar errores lexicos
class ErroresLexicos(ErrorListener):

    # Constructor
    def __init__(self):

        # Lista donde guardaremos los errores
        self.lista = []

    # Metodo que ANTLR ejecuta cuando encuentra error lexico
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Mapa de lexers disponibles segun el tipo de lenguaje detectado
_LEXERS = {
    "html": HTMLLexer,
    "css": CSSLexer,
}


# Clase para hacer el analisis lexico. Recibe el tipo de lenguaje
# ("html" o "css") y usa el lexer generado por ANTLR correspondiente.
class AnalizadorLexico:

    # Constructor
    def __init__(self, tipo):

        if tipo not in _LEXERS:
            raise ValueError(f"Tipo de lenguaje no soportado: {tipo}")

        # Guardamos el tipo de lenguaje y la clase de lexer a usar
        self.tipo = tipo
        self._clase_lexer = _LEXERS[tipo]

        # Variable para guardar el lexer
        self.lexer = None

        # Variable para guardar los tokens
        self.tokens = None

        # Objeto para guardar errores lexicos
        self.errores = ErroresLexicos()

    # Metodo para analizar codigo
    def analizar(self, codigo):

        # Convertimos el texto en entrada para ANTLR
        entrada = InputStream(codigo)

        # Creamos el lexer correspondiente al tipo de lenguaje
        self.lexer = self._clase_lexer(entrada)

        # Quitamos los errores normales de ANTLR
        self.lexer.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.lexer.addErrorListener(self.errores)

        # Creamos el flujo de tokens
        self.tokens = CommonTokenStream(self.lexer)

        # Leemos todos los tokens
        self.tokens.fill()

    # Metodo para obtener tokens como lista
    def obtener_tokens(self):

        # Creamos una lista vacia
        resultado = []

        # Recorremos todos los tokens
        for token in self.tokens.tokens:

            # Saltamos EOF porque es el fin del archivo
            if token.type == Token.EOF:

                # Continuamos con el siguiente token
                continue

            # Obtenemos el nombre del token
            nombre_token = self.lexer.symbolicNames[token.type]

            # Agregamos el token a la lista
            resultado.append({
                "lexema": token.text,
                "token": nombre_token,
                "tipo": token.type,
                "linea": token.line,
                "columna": token.column
            })

        # Retornamos la lista de tokens
        return resultado

    # Metodo para obtener errores lexicos
    def obtener_errores(self):

        # Retornamos la lista de errores
        return self.errores.lista

    # Metodo para volver a crear un flujo de tokens "fresco" (sin consumir),
    # necesario porque CommonTokenStream.fill() ya deja el stream en la
    # posicion final y el parser sintactico necesita empezar desde el inicio.
    def nuevo_flujo_tokens(self, codigo):

        entrada = InputStream(codigo)
        lexer = self._clase_lexer(entrada)
        lexer.removeErrorListeners()
        return lexer, CommonTokenStream(lexer)
