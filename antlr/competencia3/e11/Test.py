from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

with open("prueba.txt", "r", encoding="utf-8") as f:
    entrada = f.read()

lexer = ExprLexer(InputStream(entrada))
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
tree = parser.root()


if parser.getNumberOfSyntaxErrors() == 0:
    print("El codigo es sintacticamente correcto")
    print("Arbol: ")
    print(tree.toStringTree(recog=parser))
else:
    print("El codigo tiene errores sintacticos")