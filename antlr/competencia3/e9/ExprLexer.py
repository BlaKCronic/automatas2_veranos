# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,52,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,32,8,3,1,4,1,4,5,4,36,8,4,10,4,12,4,39,9,4,1,5,4,5,42,
        8,5,11,5,12,5,43,1,6,4,6,47,8,6,11,6,12,6,48,1,6,1,6,0,0,7,1,1,3,
        2,5,3,7,4,9,5,11,6,13,7,1,0,5,2,0,60,60,62,62,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,
        58,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,
        31,1,0,0,0,9,33,1,0,0,0,11,41,1,0,0,0,13,46,1,0,0,0,15,16,5,40,0,
        0,16,2,1,0,0,0,17,18,5,41,0,0,18,4,1,0,0,0,19,20,5,105,0,0,20,21,
        5,102,0,0,21,6,1,0,0,0,22,23,5,62,0,0,23,32,5,61,0,0,24,25,5,60,
        0,0,25,32,5,61,0,0,26,27,5,61,0,0,27,32,5,61,0,0,28,29,5,33,0,0,
        29,32,5,61,0,0,30,32,7,0,0,0,31,22,1,0,0,0,31,24,1,0,0,0,31,26,1,
        0,0,0,31,28,1,0,0,0,31,30,1,0,0,0,32,8,1,0,0,0,33,37,7,1,0,0,34,
        36,7,2,0,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,
        0,38,10,1,0,0,0,39,37,1,0,0,0,40,42,7,3,0,0,41,40,1,0,0,0,42,43,
        1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,12,1,0,0,0,45,47,7,4,0,0,
        46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,
        0,0,0,50,51,6,6,0,0,51,14,1,0,0,0,5,0,31,37,43,48,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    IF = 3
    OP = 4
    ID = 5
    NUM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "OP", "ID", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "IF", "OP", "ID", "NUM", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


