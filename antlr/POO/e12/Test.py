import sys
import os
from antlr4 import *

# Añadir la carpeta actual al path para encontrar ExprLexer.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ExprLexer import ExprLexer

# Leer archivo
input_stream = FileStream(sys.argv[1], encoding='utf-8')

# Crear lexer
lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()
print("Tokens:")

for token in tokens.tokens:
    if token.type == Token.EOF:
        break

    print("Texto: ", token.text)
    print("Linea: ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "<EOF>"
    print("Nombre del token: ", nombre_token)
    print("Tipo: ", token.type)
    print("---------------------")