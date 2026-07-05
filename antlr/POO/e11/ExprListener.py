# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#line.
    def enterLine(self, ctx:ExprParser.LineContext):
        pass

    # Exit a parse tree produced by ExprParser#line.
    def exitLine(self, ctx:ExprParser.LineContext):
        pass


    # Enter a parse tree produced by ExprParser#palabra.
    def enterPalabra(self, ctx:ExprParser.PalabraContext):
        pass

    # Exit a parse tree produced by ExprParser#palabra.
    def exitPalabra(self, ctx:ExprParser.PalabraContext):
        pass


    # Enter a parse tree produced by ExprParser#numero.
    def enterNumero(self, ctx:ExprParser.NumeroContext):
        pass

    # Exit a parse tree produced by ExprParser#numero.
    def exitNumero(self, ctx:ExprParser.NumeroContext):
        pass


    # Enter a parse tree produced by ExprParser#simbolo.
    def enterSimbolo(self, ctx:ExprParser.SimboloContext):
        pass

    # Exit a parse tree produced by ExprParser#simbolo.
    def exitSimbolo(self, ctx:ExprParser.SimboloContext):
        pass


    # Enter a parse tree produced by ExprParser#texto.
    def enterTexto(self, ctx:ExprParser.TextoContext):
        pass

    # Exit a parse tree produced by ExprParser#texto.
    def exitTexto(self, ctx:ExprParser.TextoContext):
        pass


    # Enter a parse tree produced by ExprParser#printCall.
    def enterPrintCall(self, ctx:ExprParser.PrintCallContext):
        pass

    # Exit a parse tree produced by ExprParser#printCall.
    def exitPrintCall(self, ctx:ExprParser.PrintCallContext):
        pass



del ExprParser