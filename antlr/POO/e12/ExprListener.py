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


    # Enter a parse tree produced by ExprParser#declaracion.
    def enterDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracion.
    def exitDeclaracion(self, ctx:ExprParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExprParser#asignacion.
    def enterAsignacion(self, ctx:ExprParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ExprParser#asignacion.
    def exitAsignacion(self, ctx:ExprParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStmt.
    def enterIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStmt.
    def exitIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#printStmt.
    def enterPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#printStmt.
    def exitPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#bloque.
    def enterBloque(self, ctx:ExprParser.BloqueContext):
        pass

    # Exit a parse tree produced by ExprParser#bloque.
    def exitBloque(self, ctx:ExprParser.BloqueContext):
        pass


    # Enter a parse tree produced by ExprParser#comparacion.
    def enterComparacion(self, ctx:ExprParser.ComparacionContext):
        pass

    # Exit a parse tree produced by ExprParser#comparacion.
    def exitComparacion(self, ctx:ExprParser.ComparacionContext):
        pass


    # Enter a parse tree produced by ExprParser#valor.
    def enterValor(self, ctx:ExprParser.ValorContext):
        pass

    # Exit a parse tree produced by ExprParser#valor.
    def exitValor(self, ctx:ExprParser.ValorContext):
        pass



del ExprParser