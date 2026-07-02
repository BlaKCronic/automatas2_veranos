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
        4,0,5,37,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,5,3,24,8,3,10,3,12,3,27,9,
        3,1,3,1,3,1,4,4,4,32,8,4,11,4,12,4,33,1,4,1,4,0,0,5,1,1,3,2,5,3,
        7,4,9,5,1,0,7,2,0,80,80,112,112,2,0,82,82,114,114,2,0,73,73,105,
        105,2,0,78,78,110,110,2,0,84,84,116,116,3,0,10,10,13,13,34,34,3,
        0,9,10,13,13,32,32,38,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,21,1,
        0,0,0,9,31,1,0,0,0,11,12,7,0,0,0,12,13,7,1,0,0,13,14,7,2,0,0,14,
        15,7,3,0,0,15,16,7,4,0,0,16,2,1,0,0,0,17,18,5,40,0,0,18,4,1,0,0,
        0,19,20,5,41,0,0,20,6,1,0,0,0,21,25,5,34,0,0,22,24,8,5,0,0,23,22,
        1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,
        27,25,1,0,0,0,28,29,5,34,0,0,29,8,1,0,0,0,30,32,7,6,0,0,31,30,1,
        0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,
        36,6,4,0,0,36,10,1,0,0,0,3,0,25,33,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    L_PAREN = 2
    R_PAREN = 3
    CADENA = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "L_PAREN", "R_PAREN", "CADENA", "WS" ]

    ruleNames = [ "PRINT", "L_PAREN", "R_PAREN", "CADENA", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


