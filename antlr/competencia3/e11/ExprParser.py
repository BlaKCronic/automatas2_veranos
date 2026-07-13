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
        4,1,27,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,2,1,2,1,
        3,1,3,3,3,46,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,2,1,
        0,19,20,1,0,21,22,79,0,14,1,0,0,0,2,17,1,0,0,0,4,24,1,0,0,0,6,45,
        1,0,0,0,8,47,1,0,0,0,10,53,1,0,0,0,12,67,1,0,0,0,14,15,3,2,1,0,15,
        16,5,0,0,1,16,1,1,0,0,0,17,18,5,1,0,0,18,19,5,2,0,0,19,20,5,25,0,
        0,20,21,5,3,0,0,21,22,3,4,2,0,22,23,5,4,0,0,23,3,1,0,0,0,24,25,5,
        1,0,0,25,26,5,5,0,0,26,27,5,6,0,0,27,28,5,7,0,0,28,29,5,8,0,0,29,
        30,5,9,0,0,30,31,5,10,0,0,31,32,5,11,0,0,32,33,5,25,0,0,33,34,5,
        12,0,0,34,38,5,3,0,0,35,37,3,6,3,0,36,35,1,0,0,0,37,40,1,0,0,0,38,
        36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,42,5,4,0,
        0,42,5,1,0,0,0,43,46,3,8,4,0,44,46,3,10,5,0,45,43,1,0,0,0,45,44,
        1,0,0,0,46,7,1,0,0,0,47,48,5,23,0,0,48,49,5,25,0,0,49,50,5,13,0,
        0,50,51,3,12,6,0,51,52,5,14,0,0,52,9,1,0,0,0,53,54,5,15,0,0,54,55,
        5,16,0,0,55,56,5,17,0,0,56,57,5,16,0,0,57,58,5,18,0,0,58,59,5,8,
        0,0,59,60,3,12,6,0,60,61,5,12,0,0,61,62,5,14,0,0,62,11,1,0,0,0,63,
        64,6,6,-1,0,64,68,5,24,0,0,65,68,5,26,0,0,66,68,5,25,0,0,67,63,1,
        0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,77,1,0,0,0,69,70,10,5,0,0,70,
        71,7,0,0,0,71,76,3,12,6,6,72,73,10,4,0,0,73,74,7,1,0,0,74,76,3,12,
        6,5,75,69,1,0,0,0,75,72,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,13,1,0,0,0,79,77,1,0,0,0,5,38,45,67,75,77
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'public'", "'class'", "'{'", "'}'", "'static'", 
                     "'void'", "'main'", "'('", "'String'", "'['", "']'", 
                     "')'", "'='", "';'", "'System'", "'.'", "'out'", "'println'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TYPE", "STRING", 
                      "ID", "NUM", "WS" ]

    RULE_root = 0
    RULE_classDecl = 1
    RULE_methodDecl = 2
    RULE_stat = 3
    RULE_varDecl = 4
    RULE_printStat = 5
    RULE_expr = 6

    ruleNames =  [ "root", "classDecl", "methodDecl", "stat", "varDecl", 
                   "printStat", "expr" ]

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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    TYPE=23
    STRING=24
    ID=25
    NUM=26
    WS=27

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

        def classDecl(self):
            return self.getTypedRuleContext(ExprParser.ClassDeclContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.classDecl()
            self.state = 15
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def methodDecl(self):
            return self.getTypedRuleContext(ExprParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_classDecl




    def classDecl(self):

        localctx = ExprParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(ExprParser.T__0)
            self.state = 18
            self.match(ExprParser.T__1)
            self.state = 19
            self.match(ExprParser.ID)
            self.state = 20
            self.match(ExprParser.T__2)
            self.state = 21
            self.methodDecl()
            self.state = 22
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_methodDecl




    def methodDecl(self):

        localctx = ExprParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ExprParser.T__0)
            self.state = 25
            self.match(ExprParser.T__4)
            self.state = 26
            self.match(ExprParser.T__5)
            self.state = 27
            self.match(ExprParser.T__6)
            self.state = 28
            self.match(ExprParser.T__7)
            self.state = 29
            self.match(ExprParser.T__8)
            self.state = 30
            self.match(ExprParser.T__9)
            self.state = 31
            self.match(ExprParser.T__10)
            self.state = 32
            self.match(ExprParser.ID)
            self.state = 33
            self.match(ExprParser.T__11)
            self.state = 34
            self.match(ExprParser.T__2)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==23:
                self.state = 35
                self.stat()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ExprParser.VarDeclContext,0)


        def printStat(self):
            return self.getTypedRuleContext(ExprParser.PrintStatContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stat




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.varDecl()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.printStat()
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


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(ExprParser.TYPE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_varDecl




    def varDecl(self):

        localctx = ExprParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExprParser.TYPE)
            self.state = 48
            self.match(ExprParser.ID)
            self.state = 49
            self.match(ExprParser.T__12)
            self.state = 50
            self.expr(0)
            self.state = 51
            self.match(ExprParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_printStat




    def printStat(self):

        localctx = ExprParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.T__14)
            self.state = 54
            self.match(ExprParser.T__15)
            self.state = 55
            self.match(ExprParser.T__16)
            self.state = 56
            self.match(ExprParser.T__15)
            self.state = 57
            self.match(ExprParser.T__17)
            self.state = 58
            self.match(ExprParser.T__7)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(ExprParser.T__11)
            self.state = 61
            self.match(ExprParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)



    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)



    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = ExprParser.StrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 64
                self.match(ExprParser.STRING)
                pass
            elif token in [26]:
                localctx = ExprParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(ExprParser.NUM)
                pass
            elif token in [25]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 75
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.AddSubContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulDivContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        self.expr(5)
                        pass

             
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




