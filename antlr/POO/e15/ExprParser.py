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
        4,1,17,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,2,3,2,26,
        8,2,1,2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,4,1,4,1,5,1,5,
        1,5,0,0,6,0,2,4,6,8,10,0,2,1,0,2,9,1,0,10,15,38,0,15,1,0,0,0,2,20,
        1,0,0,0,4,25,1,0,0,0,6,34,1,0,0,0,8,36,1,0,0,0,10,38,1,0,0,0,12,
        14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,
        0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,22,3,
        4,2,0,21,23,5,16,0,0,22,21,1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,
        26,3,6,3,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,31,3,8,4,
        0,28,30,3,10,5,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,5,1,0,0,0,33,31,1,0,0,0,34,35,5,1,0,0,35,7,1,0,0,0,36,
        37,7,0,0,0,37,9,1,0,0,0,38,39,7,1,0,0,39,11,1,0,0,0,4,15,22,25,31
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sudo'", "'nmap'", "'ss'", "'tcpdump'", 
                     "'curl'", "'dig'", "'journalctl'", "'grep'", "'ufw'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "SUDO", "NMAP", "SS", "TCPDUMP", "CURL", 
                      "DIG", "JOURNALCTL", "GREP", "UFW", "OPTION", "IP_CIDR", 
                      "IP_ADDR", "HOSTNAME", "STRING", "WORD", "SEMICOLON", 
                      "WS" ]

    RULE_program = 0
    RULE_commandLine = 1
    RULE_command = 2
    RULE_sudo = 3
    RULE_baseCommand = 4
    RULE_arg = 5

    ruleNames =  [ "program", "commandLine", "command", "sudo", "baseCommand", 
                   "arg" ]

    EOF = Token.EOF
    SUDO=1
    NMAP=2
    SS=3
    TCPDUMP=4
    CURL=5
    DIG=6
    JOURNALCTL=7
    GREP=8
    UFW=9
    OPTION=10
    IP_CIDR=11
    IP_ADDR=12
    HOSTNAME=13
    STRING=14
    WORD=15
    SEMICOLON=16
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

        def commandLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.CommandLineContext)
            else:
                return self.getTypedRuleContext(ExprParser.CommandLineContext,i)


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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1022) != 0):
                self.state = 12
                self.commandLine()
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


    class CommandLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ExprParser.CommandContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_commandLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandLine" ):
                listener.enterCommandLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandLine" ):
                listener.exitCommandLine(self)




    def commandLine(self):

        localctx = ExprParser.CommandLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commandLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.command()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 21
                self.match(ExprParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseCommand(self):
            return self.getTypedRuleContext(ExprParser.BaseCommandContext,0)


        def sudo(self):
            return self.getTypedRuleContext(ExprParser.SudoContext,0)


        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArgContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArgContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ExprParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 24
                self.sudo()


            self.state = 27
            self.baseCommand()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0):
                self.state = 28
                self.arg()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SudoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUDO(self):
            return self.getToken(ExprParser.SUDO, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_sudo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSudo" ):
                listener.enterSudo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSudo" ):
                listener.exitSudo(self)




    def sudo(self):

        localctx = ExprParser.SudoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sudo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ExprParser.SUDO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NMAP(self):
            return self.getToken(ExprParser.NMAP, 0)

        def SS(self):
            return self.getToken(ExprParser.SS, 0)

        def TCPDUMP(self):
            return self.getToken(ExprParser.TCPDUMP, 0)

        def CURL(self):
            return self.getToken(ExprParser.CURL, 0)

        def DIG(self):
            return self.getToken(ExprParser.DIG, 0)

        def JOURNALCTL(self):
            return self.getToken(ExprParser.JOURNALCTL, 0)

        def GREP(self):
            return self.getToken(ExprParser.GREP, 0)

        def UFW(self):
            return self.getToken(ExprParser.UFW, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_baseCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseCommand" ):
                listener.enterBaseCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseCommand" ):
                listener.exitBaseCommand(self)




    def baseCommand(self):

        localctx = ExprParser.BaseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_baseCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1020) != 0)):
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


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTION(self):
            return self.getToken(ExprParser.OPTION, 0)

        def IP_CIDR(self):
            return self.getToken(ExprParser.IP_CIDR, 0)

        def IP_ADDR(self):
            return self.getToken(ExprParser.IP_ADDR, 0)

        def HOSTNAME(self):
            return self.getToken(ExprParser.HOSTNAME, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def WORD(self):
            return self.getToken(ExprParser.WORD, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)




    def arg(self):

        localctx = ExprParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 64512) != 0)):
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





