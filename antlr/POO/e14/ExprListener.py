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


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#updateStmt.
    def enterUpdateStmt(self, ctx:ExprParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#updateStmt.
    def exitUpdateStmt(self, ctx:ExprParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#condition.
    def enterCondition(self, ctx:ExprParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExprParser#condition.
    def exitCondition(self, ctx:ExprParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExprParser#literalValue.
    def enterLiteralValue(self, ctx:ExprParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by ExprParser#literalValue.
    def exitLiteralValue(self, ctx:ExprParser.LiteralValueContext):
        pass



del ExprParser