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
        4,1,17,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,56,8,5,10,5,
        12,5,59,9,5,1,5,1,5,1,5,1,6,1,6,5,6,66,8,6,10,6,12,6,69,9,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,
        1,0,14,16,76,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,39,1,0,0,0,
        8,44,1,0,0,0,10,50,1,0,0,0,12,63,1,0,0,0,14,72,1,0,0,0,16,76,1,0,
        0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,
        32,3,4,2,0,27,32,3,6,3,0,28,32,3,8,4,0,29,32,3,10,5,0,30,32,3,12,
        6,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,
        1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,35,5,14,0,0,35,36,5,10,0,0,
        36,37,3,16,8,0,37,38,5,11,0,0,38,5,1,0,0,0,39,40,5,14,0,0,40,41,
        5,10,0,0,41,42,3,16,8,0,42,43,5,11,0,0,43,7,1,0,0,0,44,45,5,2,0,
        0,45,46,5,6,0,0,46,47,3,14,7,0,47,48,5,7,0,0,48,49,3,12,6,0,49,9,
        1,0,0,0,50,51,5,3,0,0,51,52,5,6,0,0,52,57,3,16,8,0,53,54,5,12,0,
        0,54,56,3,16,8,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,7,0,0,61,62,5,11,0,0,
        62,11,1,0,0,0,63,67,5,4,0,0,64,66,3,2,1,0,65,64,1,0,0,0,66,69,1,
        0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,
        71,5,5,0,0,71,13,1,0,0,0,72,73,5,14,0,0,73,74,5,13,0,0,74,75,5,15,
        0,0,75,15,1,0,0,0,76,77,7,0,0,0,77,17,1,0,0,0,4,21,31,57,67
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'if'", "'System.out.println'", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "'='", "';'", 
                     "'+'", "'>='" ]

    symbolicNames = [ "<INVALID>", "TIPO", "IF", "SYSTEM_OUT_PRINTLN", "LBRACE", 
                      "RBRACE", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "ASSIGN", "SEMICOLON", "PLUS", "GE", "ID", "NUM", 
                      "TEXT", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_declaracion = 2
    RULE_asignacion = 3
    RULE_ifStmt = 4
    RULE_printStmt = 5
    RULE_bloque = 6
    RULE_comparacion = 7
    RULE_valor = 8

    ruleNames =  [ "program", "line", "declaracion", "asignacion", "ifStmt", 
                   "printStmt", "bloque", "comparacion", "valor" ]

    EOF = Token.EOF
    TIPO=1
    IF=2
    SYSTEM_OUT_PRINTLN=3
    LBRACE=4
    RBRACE=5
    LPAREN=6
    RPAREN=7
    LBRACKET=8
    RBRACKET=9
    ASSIGN=10
    SEMICOLON=11
    PLUS=12
    GE=13
    ID=14
    NUM=15
    TEXT=16
    WS=17

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16414) != 0):
                self.state = 18
                self.line()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
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

        def declaracion(self):
            return self.getTypedRuleContext(ExprParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ExprParser.AsignacionContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ExprParser.IfStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(ExprParser.PrintStmtContext,0)


        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.declaracion()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.asignacion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.ifStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.printStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.bloque()
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


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(ExprParser.TIPO, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def valor(self):
            return self.getTypedRuleContext(ExprParser.ValorContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = ExprParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(ExprParser.TIPO)
            self.state = 34
            self.match(ExprParser.ID)
            self.state = 35
            self.match(ExprParser.ASSIGN)
            self.state = 36
            self.valor()
            self.state = 37
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def valor(self):
            return self.getTypedRuleContext(ExprParser.ValorContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = ExprParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ExprParser.ID)
            self.state = 40
            self.match(ExprParser.ASSIGN)
            self.state = 41
            self.valor()
            self.state = 42
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def comparacion(self):
            return self.getTypedRuleContext(ExprParser.ComparacionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(ExprParser.BloqueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = ExprParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.IF)
            self.state = 45
            self.match(ExprParser.LPAREN)
            self.state = 46
            self.comparacion()
            self.state = 47
            self.match(ExprParser.RPAREN)
            self.state = 48
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYSTEM_OUT_PRINTLN(self):
            return self.getToken(ExprParser.SYSTEM_OUT_PRINTLN, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValorContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValorContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PLUS)
            else:
                return self.getToken(ExprParser.PLUS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = ExprParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ExprParser.SYSTEM_OUT_PRINTLN)
            self.state = 51
            self.match(ExprParser.LPAREN)
            self.state = 52
            self.valor()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 53
                self.match(ExprParser.PLUS)
                self.state = 54
                self.valor()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(ExprParser.RPAREN)
            self.state = 61
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExprParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprParser.RBRACE, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.LineContext)
            else:
                return self.getTypedRuleContext(ExprParser.LineContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = ExprParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ExprParser.LBRACE)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16414) != 0):
                self.state = 64
                self.line()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(ExprParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def GE(self):
            return self.getToken(ExprParser.GE, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)




    def comparacion(self):

        localctx = ExprParser.ComparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ExprParser.ID)
            self.state = 73
            self.match(ExprParser.GE)
            self.state = 74
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def TEXT(self):
            return self.getToken(ExprParser.TEXT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = ExprParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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





