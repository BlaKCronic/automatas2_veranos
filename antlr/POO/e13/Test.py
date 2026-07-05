import os
import sys
from antlr4 import *

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ExprLexer import ExprLexer
from ExprParser import ExprParser

# Leer archivo
input_path = sys.argv[1]
input_stream = FileStream(input_path, encoding='utf-8')

# Mostrar tokens
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("Tokens:")
for token in token_stream.tokens:
    if token.type == Token.EOF:
        break
    print("---------------------")
    print("Texto: ", token.text)
    print("Linea: ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "<EOF>"
    print("Nombre del token: ", nombre_token)
    print("Tipo: ", token.type)

# Analizar sintácticamente
input_stream = FileStream(input_path, encoding='utf-8')
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

parse_tree = parser.program()

print("\nErrores de sintaxis:", parser.getNumberOfSyntaxErrors())
if parser.getNumberOfSyntaxErrors() == 0:
    print("Análisis sintáctico correcto")
    print("\nÁrbol sintáctico:")
    print(parse_tree.toStringTree(recog=parser))
else:
    print("Se encontraron errores en el análisis")