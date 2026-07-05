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
        4,1,15,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,
        6,8,10,12,0,1,1,0,1,10,37,0,17,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,
        6,31,1,0,0,0,8,33,1,0,0,0,10,35,1,0,0,0,12,37,1,0,0,0,14,16,3,2,
        1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,
        1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,28,3,4,2,0,23,
        28,3,6,3,0,24,28,3,8,4,0,25,28,3,10,5,0,26,28,3,12,6,0,27,22,1,0,
        0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,
        1,0,0,0,29,30,5,12,0,0,30,5,1,0,0,0,31,32,5,13,0,0,32,7,1,0,0,0,
        33,34,7,0,0,0,34,9,1,0,0,0,35,36,5,14,0,0,36,11,1,0,0,0,37,38,5,
        11,0,0,38,13,1,0,0,0,2,17,27
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'='", "';'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'.'", "'System.out.println'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SYSTEM_OUT_PRINTLN", 
                      "ID", "NUMBER", "TEXT", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_palabra = 2
    RULE_numero = 3
    RULE_simbolo = 4
    RULE_texto = 5
    RULE_printCall = 6

    ruleNames =  [ "program", "line", "palabra", "numero", "simbolo", "texto", 
                   "printCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    SYSTEM_OUT_PRINTLN=11
    ID=12
    NUMBER=13
    TEXT=14
    WS=15

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

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LineContext)
            else:
                return self.getTypedRuleContext(ExprParser.LineContext,i)


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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32766) != 0):
                self.state = 14
                self.line()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def palabra(self):
            return self.getTypedRuleContext(ExprParser.PalabraContext,0)


        def numero(self):
            return self.getTypedRuleContext(ExprParser.NumeroContext,0)


        def simbolo(self):
            return self.getTypedRuleContext(ExprParser.SimboloContext,0)


        def texto(self):
            return self.getTypedRuleContext(ExprParser.TextoContext,0)


        def printCall(self):
            return self.getTypedRuleContext(ExprParser.PrintCallContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = ExprParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.palabra()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.numero()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.simbolo()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.texto()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.printCall()
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


    class PalabraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_palabra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPalabra" ):
                listener.enterPalabra(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPalabra" ):
                listener.exitPalabra(self)




    def palabra(self):

        localctx = ExprParser.PalabraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_palabra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)




    def numero(self):

        localctx = ExprParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numero)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimboloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_simbolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimbolo" ):
                listener.enterSimbolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimbolo" ):
                listener.exitSimbolo(self)




    def simbolo(self):

        localctx = ExprParser.SimboloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simbolo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0)):
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


    class TextoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ExprParser.TEXT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_texto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTexto" ):
                listener.enterTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTexto" ):
                listener.exitTexto(self)




    def texto(self):

        localctx = ExprParser.TextoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_texto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ExprParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSTEM_OUT_PRINTLN(self):
            return self.getToken(ExprParser.SYSTEM_OUT_PRINTLN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_printCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintCall" ):
                listener.enterPrintCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintCall" ):
                listener.exitPrintCall(self)




    def printCall(self):

        localctx = ExprParser.PrintCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_printCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.SYSTEM_OUT_PRINTLN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





