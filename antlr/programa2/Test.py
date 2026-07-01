from antlr4 import *
from ExprLexer import ExprLexer
import sys

#leer archivos
input_stream = FileStream(sys.argv[1])

#terminal
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print("Tokens:")

for token in tokens.tokens:
    print("Texto: ", token.text)
    print("Linea: ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    print("Nombre del token: ", nombre_token)
    print("Tipo: ", token.type)
    print("---------------------")