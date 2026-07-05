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


    # Enter a parse tree produced by ExprParser#createTableStmt.
    def enterCreateTableStmt(self, ctx:ExprParser.CreateTableStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#createTableStmt.
    def exitCreateTableStmt(self, ctx:ExprParser.CreateTableStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#columnDef.
    def enterColumnDef(self, ctx:ExprParser.ColumnDefContext):
        pass

    # Exit a parse tree produced by ExprParser#columnDef.
    def exitColumnDef(self, ctx:ExprParser.ColumnDefContext):
        pass


    # Enter a parse tree produced by ExprParser#typeDef.
    def enterTypeDef(self, ctx:ExprParser.TypeDefContext):
        pass

    # Exit a parse tree produced by ExprParser#typeDef.
    def exitTypeDef(self, ctx:ExprParser.TypeDefContext):
        pass


    # Enter a parse tree produced by ExprParser#columnConstraint.
    def enterColumnConstraint(self, ctx:ExprParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by ExprParser#columnConstraint.
    def exitColumnConstraint(self, ctx:ExprParser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by ExprParser#insertStmt.
    def enterInsertStmt(self, ctx:ExprParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#insertStmt.
    def exitInsertStmt(self, ctx:ExprParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#valueList.
    def enterValueList(self, ctx:ExprParser.ValueListContext):
        pass

    # Exit a parse tree produced by ExprParser#valueList.
    def exitValueList(self, ctx:ExprParser.ValueListContext):
        pass


    # Enter a parse tree produced by ExprParser#literalValue.
    def enterLiteralValue(self, ctx:ExprParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by ExprParser#literalValue.
    def exitLiteralValue(self, ctx:ExprParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by ExprParser#selectStmt.
    def enterSelectStmt(self, ctx:ExprParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#selectStmt.
    def exitSelectStmt(self, ctx:ExprParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#selectItem.
    def enterSelectItem(self, ctx:ExprParser.SelectItemContext):
        pass

    # Exit a parse tree produced by ExprParser#selectItem.
    def exitSelectItem(self, ctx:ExprParser.SelectItemContext):
        pass


    # Enter a parse tree produced by ExprParser#tableRef.
    def enterTableRef(self, ctx:ExprParser.TableRefContext):
        pass

    # Exit a parse tree produced by ExprParser#tableRef.
    def exitTableRef(self, ctx:ExprParser.TableRefContext):
        pass


    # Enter a parse tree produced by ExprParser#alias.
    def enterAlias(self, ctx:ExprParser.AliasContext):
        pass

    # Exit a parse tree produced by ExprParser#alias.
    def exitAlias(self, ctx:ExprParser.AliasContext):
        pass


    # Enter a parse tree produced by ExprParser#condition.
    def enterCondition(self, ctx:ExprParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExprParser#condition.
    def exitCondition(self, ctx:ExprParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExprParser#valueExpr.
    def enterValueExpr(self, ctx:ExprParser.ValueExprContext):
        pass

    # Exit a parse tree produced by ExprParser#valueExpr.
    def exitValueExpr(self, ctx:ExprParser.ValueExprContext):
        pass


    # Enter a parse tree produced by ExprParser#columnName.
    def enterColumnName(self, ctx:ExprParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by ExprParser#columnName.
    def exitColumnName(self, ctx:ExprParser.ColumnNameContext):
        pass



del ExprParser