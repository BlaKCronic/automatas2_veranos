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
        4,1,10,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,5,2,29,8,2,10,2,12,2,32,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,1,1,0,7,9,43,0,15,
        1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,37,1,0,0,0,8,41,1,0,0,0,10,45,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,
        0,0,20,21,3,4,2,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,5,8,0,0,24,25,
        5,2,0,0,25,30,3,6,3,0,26,27,5,4,0,0,27,29,3,6,3,0,28,26,1,0,0,0,
        29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,
        0,0,0,33,34,5,3,0,0,34,35,3,8,4,0,35,36,5,5,0,0,36,5,1,0,0,0,37,
        38,5,8,0,0,38,39,5,6,0,0,39,40,3,10,5,0,40,7,1,0,0,0,41,42,5,8,0,
        0,42,43,5,6,0,0,43,44,3,10,5,0,44,9,1,0,0,0,45,46,7,0,0,0,46,11,
        1,0,0,0,2,15,30
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'UPDATE'", "'SET'", "'WHERE'", "','", 
                     "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "UPDATE", "SET", "WHERE", "COMMA", "SEMICOLON", 
                      "EQ", "STRING", "ID", "NUM", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_updateStmt = 2
    RULE_assignment = 3
    RULE_condition = 4
    RULE_literalValue = 5

    ruleNames =  [ "program", "statement", "updateStmt", "assignment", "condition", 
                   "literalValue" ]

    EOF = Token.EOF
    UPDATE=1
    SET=2
    WHERE=3
    COMMA=4
    SEMICOLON=5
    EQ=6
    STRING=7
    ID=8
    NUM=9
    WS=10

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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

        def updateStmt(self):
            return self.getTypedRuleContext(ExprParser.UpdateStmtContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.updateStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(ExprParser.UPDATE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def SET(self):
            return self.getToken(ExprParser.SET, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(ExprParser.AssignmentContext,i)


        def WHERE(self):
            return self.getToken(ExprParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_updateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStmt" ):
                listener.enterUpdateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStmt" ):
                listener.exitUpdateStmt(self)




    def updateStmt(self):

        localctx = ExprParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_updateStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ExprParser.UPDATE)
            self.state = 23
            self.match(ExprParser.ID)
            self.state = 24
            self.match(ExprParser.SET)
            self.state = 25
            self.assignment()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 26
                self.match(ExprParser.COMMA)
                self.state = 27
                self.assignment()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(ExprParser.WHERE)
            self.state = 34
            self.condition()
            self.state = 35
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def literalValue(self):
            return self.getTypedRuleContext(ExprParser.LiteralValueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.ID)
            self.state = 38
            self.match(ExprParser.EQ)
            self.state = 39
            self.literalValue()
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

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def literalValue(self):
            return self.getTypedRuleContext(ExprParser.LiteralValueContext,0)


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
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(ExprParser.ID)
            self.state = 42
            self.match(ExprParser.EQ)
            self.state = 43
            self.literalValue()
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
        self.enterRule(localctx, 10, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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





