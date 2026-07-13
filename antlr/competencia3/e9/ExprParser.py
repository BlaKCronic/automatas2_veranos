# Generated from ./Expr.g4 by ANTLR 4.13.2
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
        4,1,7,19,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,15,0,6,1,0,0,0,2,9,1,0,0,0,4,
        14,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,3,0,0,10,11,
        5,1,0,0,11,12,3,4,2,0,12,13,5,2,0,0,13,3,1,0,0,0,14,15,5,5,0,0,15,
        16,5,4,0,0,16,17,5,6,0,0,17,5,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'if'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "OP", 
                      "ID", "NUM", "WS" ]

    RULE_root = 0
    RULE_ifStat = 1
    RULE_comp = 2

    ruleNames =  [ "root", "ifStat", "comp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    OP=4
    ID=5
    NUM=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStat(self):
            return self.getTypedRuleContext(ExprParser.IfStatContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.ifStat()
            self.state = 7
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def comp(self):
            return self.getTypedRuleContext(ExprParser.CompContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_ifStat




    def ifStat(self):

        localctx = ExprParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ifStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(ExprParser.IF)
            self.state = 10
            self.match(ExprParser.T__0)
            self.state = 11
            self.comp()
            self.state = 12
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def OP(self):
            return self.getToken(ExprParser.OP, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comp




    def comp(self):

        localctx = ExprParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(ExprParser.ID)
            self.state = 15
            self.match(ExprParser.OP)
            self.state = 16
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





