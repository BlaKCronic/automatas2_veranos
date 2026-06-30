from antlr4 import *
from ExprLexer import ExprLexer

lexer = ExprLexer(InputStream(input("?> ")))

tokens = CommonTokenStream(lexer)
tokens.fill()
print("Tokens:")

for token in tokens.tokens:
    print("Texto: ", token.text)
    print("Linea: ", token.line)
    print("Columna: ", token.column)
    print("Tipo: ", token.type)
    print("---------------------")