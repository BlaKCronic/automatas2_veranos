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
        4,1,9,15,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,1,
        1,1,1,1,1,0,0,2,0,2,0,1,1,0,1,8,13,0,7,1,0,0,0,2,12,1,0,0,0,4,6,
        3,2,1,0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,0,
        0,0,9,7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,7,0,0,0,13,3,1,
        0,0,0,1,7
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "COMANDO", "OPCION", "CADENA", "IP", 
                      "RUTA", "DOMINIO", "NUMERO", "IDENTIFICADOR", "WS" ]

    RULE_programa = 0
    RULE_elemento = 1

    ruleNames =  [ "programa", "elemento" ]

    EOF = Token.EOF
    COMANDO=1
    OPCION=2
    CADENA=3
    IP=4
    RUTA=5
    DOMINIO=6
    NUMERO=7
    IDENTIFICADOR=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def elemento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ElementoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ElementoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_programa




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 510) != 0):
                self.state = 4
                self.elemento()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMANDO(self):
            return self.getToken(ExprParser.COMANDO, 0)

        def OPCION(self):
            return self.getToken(ExprParser.OPCION, 0)

        def IP(self):
            return self.getToken(ExprParser.IP, 0)

        def RUTA(self):
            return self.getToken(ExprParser.RUTA, 0)

        def DOMINIO(self):
            return self.getToken(ExprParser.DOMINIO, 0)

        def CADENA(self):
            return self.getToken(ExprParser.CADENA, 0)

        def NUMERO(self):
            return self.getToken(ExprParser.NUMERO, 0)

        def IDENTIFICADOR(self):
            return self.getToken(ExprParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_elemento




    def elemento(self):

        localctx = ExprParser.ElementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_elemento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 510) != 0)):
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





