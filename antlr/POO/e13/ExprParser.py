# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,168,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,3,1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,2,10,2,12,
        2,56,9,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,76,8,4,1,5,1,5,1,5,1,5,3,5,82,8,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,91,8,6,10,6,12,6,94,9,6,1,6,1,6,1,
        6,1,6,1,6,5,6,101,8,6,10,6,12,6,104,9,6,1,6,1,6,1,7,1,7,1,7,1,7,
        5,7,112,8,7,10,7,12,7,115,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,5,
        9,125,8,9,10,9,12,9,128,9,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        138,8,9,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,3,11,148,8,11,1,12,1,
        12,1,13,1,13,1,13,1,13,1,14,1,14,3,14,158,8,14,1,15,1,15,1,15,5,
        15,163,8,15,10,15,12,15,166,9,15,1,15,0,0,16,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,0,1,1,0,26,28,168,0,35,1,0,0,0,2,43,1,0,
        0,0,4,45,1,0,0,0,6,60,1,0,0,0,8,75,1,0,0,0,10,81,1,0,0,0,12,83,1,
        0,0,0,14,107,1,0,0,0,16,118,1,0,0,0,18,120,1,0,0,0,20,143,1,0,0,
        0,22,145,1,0,0,0,24,149,1,0,0,0,26,151,1,0,0,0,28,157,1,0,0,0,30,
        159,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,
        0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,
        1,0,0,0,40,44,3,4,2,0,41,44,3,12,6,0,42,44,3,18,9,0,43,40,1,0,0,
        0,43,41,1,0,0,0,43,42,1,0,0,0,44,3,1,0,0,0,45,46,5,1,0,0,46,47,5,
        2,0,0,47,48,5,27,0,0,48,49,5,21,0,0,49,54,3,6,3,0,50,51,5,23,0,0,
        51,53,3,6,3,0,52,50,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,
        0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,57,58,5,22,0,0,58,59,5,24,0,0,
        59,5,1,0,0,0,60,61,5,27,0,0,61,65,3,8,4,0,62,64,3,10,5,0,63,62,1,
        0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,
        65,1,0,0,0,68,76,5,12,0,0,69,76,5,13,0,0,70,71,5,14,0,0,71,72,5,
        21,0,0,72,73,5,28,0,0,73,76,5,22,0,0,74,76,5,15,0,0,75,68,1,0,0,
        0,75,69,1,0,0,0,75,70,1,0,0,0,75,74,1,0,0,0,76,9,1,0,0,0,77,78,5,
        18,0,0,78,82,5,19,0,0,79,80,5,16,0,0,80,82,5,17,0,0,81,77,1,0,0,
        0,81,79,1,0,0,0,82,11,1,0,0,0,83,84,5,3,0,0,84,85,5,4,0,0,85,86,
        5,27,0,0,86,87,5,21,0,0,87,92,3,30,15,0,88,89,5,23,0,0,89,91,3,30,
        15,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,
        95,1,0,0,0,94,92,1,0,0,0,95,96,5,22,0,0,96,97,5,5,0,0,97,102,3,14,
        7,0,98,99,5,23,0,0,99,101,3,14,7,0,100,98,1,0,0,0,101,104,1,0,0,
        0,102,100,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,1,0,0,
        0,105,106,5,24,0,0,106,13,1,0,0,0,107,108,5,21,0,0,108,113,3,16,
        8,0,109,110,5,23,0,0,110,112,3,16,8,0,111,109,1,0,0,0,112,115,1,
        0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,
        0,0,0,116,117,5,22,0,0,117,15,1,0,0,0,118,119,7,0,0,0,119,17,1,0,
        0,0,120,121,5,6,0,0,121,126,3,20,10,0,122,123,5,23,0,0,123,125,3,
        20,10,0,124,122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,
        1,0,0,0,127,129,1,0,0,0,128,126,1,0,0,0,129,130,5,7,0,0,130,137,
        3,22,11,0,131,132,5,8,0,0,132,133,5,9,0,0,133,134,3,22,11,0,134,
        135,5,10,0,0,135,136,3,26,13,0,136,138,1,0,0,0,137,131,1,0,0,0,137,
        138,1,0,0,0,138,139,1,0,0,0,139,140,5,11,0,0,140,141,3,26,13,0,141,
        142,5,24,0,0,142,19,1,0,0,0,143,144,3,30,15,0,144,21,1,0,0,0,145,
        147,5,27,0,0,146,148,3,24,12,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        23,1,0,0,0,149,150,5,27,0,0,150,25,1,0,0,0,151,152,3,30,15,0,152,
        153,5,20,0,0,153,154,3,28,14,0,154,27,1,0,0,0,155,158,3,16,8,0,156,
        158,3,30,15,0,157,155,1,0,0,0,157,156,1,0,0,0,158,29,1,0,0,0,159,
        164,5,27,0,0,160,161,5,25,0,0,161,163,5,27,0,0,162,160,1,0,0,0,163,
        166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,31,1,0,0,0,166,164,
        1,0,0,0,14,35,43,54,65,75,81,92,102,113,126,137,147,157,164
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'TABLE'", "'INSERT'", "'INTO'", 
                     "'VALUES'", "'SELECT'", "'FROM'", "'INNER'", "'JOIN'", 
                     "'ON'", "'WHERE'", "'SERIAL'", "'INTEGER'", "'VARCHAR'", 
                     "'DATE'", "'PRIMARY'", "'KEY'", "'NOT'", "'NULL'", 
                     "'='", "'('", "')'", "','", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "CREATE", "TABLE", "INSERT", "INTO", 
                      "VALUES", "SELECT", "FROM", "INNER", "JOIN", "ON", 
                      "WHERE", "SERIAL", "INTEGER", "VARCHAR", "DATE", "PRIMARY", 
                      "KEY", "NOT", "NULL", "EQ", "LPAREN", "RPAREN", "COMMA", 
                      "SEMICOLON", "DOT", "STRING", "ID", "NUM", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_createTableStmt = 2
    RULE_columnDef = 3
    RULE_typeDef = 4
    RULE_columnConstraint = 5
    RULE_insertStmt = 6
    RULE_valueList = 7
    RULE_literalValue = 8
    RULE_selectStmt = 9
    RULE_selectItem = 10
    RULE_tableRef = 11
    RULE_alias = 12
    RULE_condition = 13
    RULE_valueExpr = 14
    RULE_columnName = 15

    ruleNames =  [ "program", "statement", "createTableStmt", "columnDef", 
                   "typeDef", "columnConstraint", "insertStmt", "valueList", 
                   "literalValue", "selectStmt", "selectItem", "tableRef", 
                   "alias", "condition", "valueExpr", "columnName" ]

    EOF = Token.EOF
    CREATE=1
    TABLE=2
    INSERT=3
    INTO=4
    VALUES=5
    SELECT=6
    FROM=7
    INNER=8
    JOIN=9
    ON=10
    WHERE=11
    SERIAL=12
    INTEGER=13
    VARCHAR=14
    DATE=15
    PRIMARY=16
    KEY=17
    NOT=18
    NULL=19
    EQ=20
    LPAREN=21
    RPAREN=22
    COMMA=23
    SEMICOLON=24
    DOT=25
    STRING=26
    ID=27
    NUM=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 74) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createTableStmt(self):
            return self.getTypedRuleContext(ExprParser.CreateTableStmtContext,0)


        def insertStmt(self):
            return self.getTypedRuleContext(ExprParser.InsertStmtContext,0)


        def selectStmt(self):
            return self.getTypedRuleContext(ExprParser.SelectStmtContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.createTableStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.insertStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.selectStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateTableStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(ExprParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(ExprParser.TABLE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def columnDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ColumnDefContext)
            else:
                return self.getTypedRuleContext(ExprParser.ColumnDefContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_createTableStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateTableStmt" ):
                listener.enterCreateTableStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateTableStmt" ):
                listener.exitCreateTableStmt(self)




    def createTableStmt(self):

        localctx = ExprParser.CreateTableStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createTableStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ExprParser.CREATE)
            self.state = 46
            self.match(ExprParser.TABLE)
            self.state = 47
            self.match(ExprParser.ID)
            self.state = 48
            self.match(ExprParser.LPAREN)
            self.state = 49
            self.columnDef()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 50
                self.match(ExprParser.COMMA)
                self.state = 51
                self.columnDef()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(ExprParser.RPAREN)
            self.state = 58
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def typeDef(self):
            return self.getTypedRuleContext(ExprParser.TypeDefContext,0)


        def columnConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ColumnConstraintContext)
            else:
                return self.getTypedRuleContext(ExprParser.ColumnConstraintContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_columnDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDef" ):
                listener.enterColumnDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDef" ):
                listener.exitColumnDef(self)




    def columnDef(self):

        localctx = ExprParser.ColumnDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ExprParser.ID)
            self.state = 61
            self.typeDef()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==18:
                self.state = 62
                self.columnConstraint()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SERIAL(self):
            return self.getToken(ExprParser.SERIAL, 0)

        def INTEGER(self):
            return self.getToken(ExprParser.INTEGER, 0)

        def VARCHAR(self):
            return self.getToken(ExprParser.VARCHAR, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def DATE(self):
            return self.getToken(ExprParser.DATE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_typeDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeDef" ):
                listener.enterTypeDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeDef" ):
                listener.exitTypeDef(self)




    def typeDef(self):

        localctx = ExprParser.TypeDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeDef)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(ExprParser.SERIAL)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(ExprParser.INTEGER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(ExprParser.VARCHAR)
                self.state = 71
                self.match(ExprParser.LPAREN)
                self.state = 72
                self.match(ExprParser.NUM)
                self.state = 73
                self.match(ExprParser.RPAREN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(ExprParser.DATE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def NULL(self):
            return self.getToken(ExprParser.NULL, 0)

        def PRIMARY(self):
            return self.getToken(ExprParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(ExprParser.KEY, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_columnConstraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnConstraint" ):
                listener.enterColumnConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnConstraint" ):
                listener.exitColumnConstraint(self)




    def columnConstraint(self):

        localctx = ExprParser.ColumnConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_columnConstraint)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(ExprParser.NOT)
                self.state = 78
                self.match(ExprParser.NULL)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ExprParser.PRIMARY)
                self.state = 80
                self.match(ExprParser.KEY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(ExprParser.INSERT, 0)

        def INTO(self):
            return self.getToken(ExprParser.INTO, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(ExprParser.ColumnNameContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def VALUES(self):
            return self.getToken(ExprParser.VALUES, 0)

        def valueList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueListContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueListContext,i)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_insertStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStmt" ):
                listener.enterInsertStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStmt" ):
                listener.exitInsertStmt(self)




    def insertStmt(self):

        localctx = ExprParser.InsertStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_insertStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ExprParser.INSERT)
            self.state = 84
            self.match(ExprParser.INTO)
            self.state = 85
            self.match(ExprParser.ID)
            self.state = 86
            self.match(ExprParser.LPAREN)
            self.state = 87
            self.columnName()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 88
                self.match(ExprParser.COMMA)
                self.state = 89
                self.columnName()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(ExprParser.RPAREN)
            self.state = 96
            self.match(ExprParser.VALUES)
            self.state = 97
            self.valueList()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 98
                self.match(ExprParser.COMMA)
                self.state = 99
                self.valueList()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def literalValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LiteralValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.LiteralValueContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)




    def valueList(self):

        localctx = ExprParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(ExprParser.LPAREN)
            self.state = 108
            self.literalValue()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 109
                self.match(ExprParser.COMMA)
                self.state = 110
                self.literalValue()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)




    def literalValue(self):

        localctx = ExprParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(ExprParser.SELECT, 0)

        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(ExprParser.SelectItemContext,i)


        def FROM(self):
            return self.getToken(ExprParser.FROM, 0)

        def tableRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TableRefContext)
            else:
                return self.getTypedRuleContext(ExprParser.TableRefContext,i)


        def WHERE(self):
            return self.getToken(ExprParser.WHERE, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ConditionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ConditionContext,i)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def INNER(self):
            return self.getToken(ExprParser.INNER, 0)

        def JOIN(self):
            return self.getToken(ExprParser.JOIN, 0)

        def ON(self):
            return self.getToken(ExprParser.ON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)




    def selectStmt(self):

        localctx = ExprParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(ExprParser.SELECT)
            self.state = 121
            self.selectItem()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 122
                self.match(ExprParser.COMMA)
                self.state = 123
                self.selectItem()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(ExprParser.FROM)
            self.state = 130
            self.tableRef()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 131
                self.match(ExprParser.INNER)
                self.state = 132
                self.match(ExprParser.JOIN)
                self.state = 133
                self.tableRef()
                self.state = 134
                self.match(ExprParser.ON)
                self.state = 135
                self.condition()


            self.state = 139
            self.match(ExprParser.WHERE)
            self.state = 140
            self.condition()
            self.state = 141
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(ExprParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_selectItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectItem" ):
                listener.enterSelectItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectItem" ):
                listener.exitSelectItem(self)




    def selectItem(self):

        localctx = ExprParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_selectItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.columnName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def alias(self):
            return self.getTypedRuleContext(ExprParser.AliasContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_tableRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableRef" ):
                listener.enterTableRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableRef" ):
                listener.exitTableRef(self)




    def tableRef(self):

        localctx = ExprParser.TableRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tableRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(ExprParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 146
                self.alias()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AliasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlias" ):
                listener.enterAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlias" ):
                listener.exitAlias(self)




    def alias(self):

        localctx = ExprParser.AliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(ExprParser.ColumnNameContext,0)


        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def valueExpr(self):
            return self.getTypedRuleContext(ExprParser.ValueExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.columnName()
            self.state = 152
            self.match(ExprParser.EQ)
            self.state = 153
            self.valueExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalValue(self):
            return self.getTypedRuleContext(ExprParser.LiteralValueContext,0)


        def columnName(self):
            return self.getTypedRuleContext(ExprParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_valueExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueExpr" ):
                listener.enterValueExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueExpr" ):
                listener.exitValueExpr(self)




    def valueExpr(self):

        localctx = ExprParser.ValueExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_valueExpr)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.literalValue()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.columnName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.DOT)
            else:
                return self.getToken(ExprParser.DOT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)




    def columnName(self):

        localctx = ExprParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_columnName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ExprParser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 160
                self.match(ExprParser.DOT)
                self.state = 161
                self.match(ExprParser.ID)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





