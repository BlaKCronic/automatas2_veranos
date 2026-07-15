# Generated from HTMLParser.g4 by ANTLR 4.13.2
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
        4,1,13,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,3,0,20,8,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,
        1,0,1,0,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,
        41,9,2,1,2,1,2,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,2,5,
        2,55,8,2,10,2,12,2,58,9,2,1,2,1,2,1,2,1,2,3,2,64,8,2,3,2,66,8,2,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,3,6,77,8,6,1,7,1,7,1,8,1,8,1,
        8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,7,8,1,0,11,12,1,0,10,12,83,
        0,19,1,0,0,0,2,32,1,0,0,0,4,65,1,0,0,0,6,67,1,0,0,0,8,69,1,0,0,0,
        10,71,1,0,0,0,12,73,1,0,0,0,14,78,1,0,0,0,16,80,1,0,0,0,18,20,5,
        1,0,0,19,18,1,0,0,0,19,20,1,0,0,0,20,24,1,0,0,0,21,23,3,2,1,0,22,
        21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,
        0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,33,3,4,2,0,30,33,3,
        10,5,0,31,33,5,6,0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,
        3,1,0,0,0,34,35,5,5,0,0,35,39,5,11,0,0,36,38,3,12,6,0,37,36,1,0,
        0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,
        1,0,0,0,42,66,7,0,0,0,43,44,5,5,0,0,44,48,3,6,3,0,45,47,3,12,6,0,
        46,45,1,0,0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,63,1,
        0,0,0,50,48,1,0,0,0,51,64,5,8,0,0,52,56,5,7,0,0,53,55,3,2,1,0,54,
        53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,56,1,0,0,0,59,60,5,4,0,0,60,61,3,8,4,0,61,62,5,7,0,0,62,64,
        1,0,0,0,63,51,1,0,0,0,63,52,1,0,0,0,64,66,1,0,0,0,65,34,1,0,0,0,
        65,43,1,0,0,0,66,5,1,0,0,0,67,68,5,12,0,0,68,7,1,0,0,0,69,70,5,12,
        0,0,70,9,1,0,0,0,71,72,5,2,0,0,72,11,1,0,0,0,73,76,3,14,7,0,74,75,
        5,9,0,0,75,77,3,16,8,0,76,74,1,0,0,0,76,77,1,0,0,0,77,13,1,0,0,0,
        78,79,7,1,0,0,79,15,1,0,0,0,80,81,7,2,0,0,81,17,1,0,0,0,9,19,24,
        32,39,48,56,63,65,76
    ]

class HTMLParser ( Parser ):

    grammarFileName = "HTMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'</'", "'<'", "<INVALID>", "'>'", "'/>'", "'='" ]

    symbolicNames = [ "<INVALID>", "DOCTYPE", "COMMENT", "CDATA", "TAG_OPEN_SLASH", 
                      "TAG_OPEN", "TEXT", "TAG_CLOSE", "TAG_SELFCLOSE", 
                      "EQUALS", "STRING", "VOID_NAME", "NAME", "TAG_WS" ]

    RULE_htmlDocument = 0
    RULE_content = 1
    RULE_element = 2
    RULE_tagName = 3
    RULE_closeTagName = 4
    RULE_comment = 5
    RULE_attribute = 6
    RULE_attrName = 7
    RULE_attrValue = 8

    ruleNames =  [ "htmlDocument", "content", "element", "tagName", "closeTagName", 
                   "comment", "attribute", "attrName", "attrValue" ]

    EOF = Token.EOF
    DOCTYPE=1
    COMMENT=2
    CDATA=3
    TAG_OPEN_SLASH=4
    TAG_OPEN=5
    TEXT=6
    TAG_CLOSE=7
    TAG_SELFCLOSE=8
    EQUALS=9
    STRING=10
    VOID_NAME=11
    NAME=12
    TAG_WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class HtmlDocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HTMLParser.EOF, 0)

        def DOCTYPE(self):
            return self.getToken(HTMLParser.DOCTYPE, 0)

        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.ContentContext)
            else:
                return self.getTypedRuleContext(HTMLParser.ContentContext,i)


        def getRuleIndex(self):
            return HTMLParser.RULE_htmlDocument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtmlDocument" ):
                listener.enterHtmlDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtmlDocument" ):
                listener.exitHtmlDocument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHtmlDocument" ):
                return visitor.visitHtmlDocument(self)
            else:
                return visitor.visitChildren(self)




    def htmlDocument(self):

        localctx = HTMLParser.HtmlDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_htmlDocument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 18
                self.match(HTMLParser.DOCTYPE)


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 100) != 0):
                self.state = 21
                self.content()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(HTMLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(HTMLParser.ElementContext,0)


        def comment(self):
            return self.getTypedRuleContext(HTMLParser.CommentContext,0)


        def TEXT(self):
            return self.getToken(HTMLParser.TEXT, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent" ):
                listener.enterContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent" ):
                listener.exitContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = HTMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_content)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.element()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.comment()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(HTMLParser.TEXT)
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


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HTMLParser.RULE_element

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VoidElementContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HTMLParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)
        def VOID_NAME(self):
            return self.getToken(HTMLParser.VOID_NAME, 0)
        def TAG_SELFCLOSE(self):
            return self.getToken(HTMLParser.TAG_SELFCLOSE, 0)
        def TAG_CLOSE(self):
            return self.getToken(HTMLParser.TAG_CLOSE, 0)
        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(HTMLParser.AttributeContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidElement" ):
                listener.enterVoidElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidElement" ):
                listener.exitVoidElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidElement" ):
                return visitor.visitVoidElement(self)
            else:
                return visitor.visitChildren(self)


    class NormalElementContext(ElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HTMLParser.ElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAG_OPEN(self):
            return self.getToken(HTMLParser.TAG_OPEN, 0)
        def tagName(self):
            return self.getTypedRuleContext(HTMLParser.TagNameContext,0)

        def TAG_SELFCLOSE(self):
            return self.getToken(HTMLParser.TAG_SELFCLOSE, 0)
        def TAG_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(HTMLParser.TAG_CLOSE)
            else:
                return self.getToken(HTMLParser.TAG_CLOSE, i)
        def TAG_OPEN_SLASH(self):
            return self.getToken(HTMLParser.TAG_OPEN_SLASH, 0)
        def closeTagName(self):
            return self.getTypedRuleContext(HTMLParser.CloseTagNameContext,0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(HTMLParser.AttributeContext,i)

        def content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HTMLParser.ContentContext)
            else:
                return self.getTypedRuleContext(HTMLParser.ContentContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalElement" ):
                listener.enterNormalElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalElement" ):
                listener.exitNormalElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalElement" ):
                return visitor.visitNormalElement(self)
            else:
                return visitor.visitChildren(self)



    def element(self):

        localctx = HTMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = HTMLParser.VoidElementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(HTMLParser.TAG_OPEN)
                self.state = 35
                self.match(HTMLParser.VOID_NAME)
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11 or _la==12:
                    self.state = 36
                    self.attribute()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = HTMLParser.NormalElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(HTMLParser.TAG_OPEN)
                self.state = 44
                self.tagName()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11 or _la==12:
                    self.state = 45
                    self.attribute()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 63
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8]:
                    self.state = 51
                    self.match(HTMLParser.TAG_SELFCLOSE)
                    pass
                elif token in [7]:
                    self.state = 52
                    self.match(HTMLParser.TAG_CLOSE)
                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 100) != 0):
                        self.state = 53
                        self.content()
                        self.state = 58
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 59
                    self.match(HTMLParser.TAG_OPEN_SLASH)
                    self.state = 60
                    self.closeTagName()
                    self.state = 61
                    self.match(HTMLParser.TAG_CLOSE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HTMLParser.NAME, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_tagName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagName" ):
                listener.enterTagName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagName" ):
                listener.exitTagName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagName" ):
                return visitor.visitTagName(self)
            else:
                return visitor.visitChildren(self)




    def tagName(self):

        localctx = HTMLParser.TagNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tagName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(HTMLParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseTagNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HTMLParser.NAME, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_closeTagName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloseTagName" ):
                listener.enterCloseTagName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloseTagName" ):
                listener.exitCloseTagName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCloseTagName" ):
                return visitor.visitCloseTagName(self)
            else:
                return visitor.visitChildren(self)




    def closeTagName(self):

        localctx = HTMLParser.CloseTagNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_closeTagName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(HTMLParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(HTMLParser.COMMENT, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = HTMLParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(HTMLParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrName(self):
            return self.getTypedRuleContext(HTMLParser.AttrNameContext,0)


        def EQUALS(self):
            return self.getToken(HTMLParser.EQUALS, 0)

        def attrValue(self):
            return self.getTypedRuleContext(HTMLParser.AttrValueContext,0)


        def getRuleIndex(self):
            return HTMLParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = HTMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.attrName()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 74
                self.match(HTMLParser.EQUALS)
                self.state = 75
                self.attrValue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(HTMLParser.NAME, 0)

        def VOID_NAME(self):
            return self.getToken(HTMLParser.VOID_NAME, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_attrName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrName" ):
                listener.enterAttrName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrName" ):
                listener.exitAttrName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrName" ):
                return visitor.visitAttrName(self)
            else:
                return visitor.visitChildren(self)




    def attrName(self):

        localctx = HTMLParser.AttrNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
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


    class AttrValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(HTMLParser.STRING, 0)

        def NAME(self):
            return self.getToken(HTMLParser.NAME, 0)

        def VOID_NAME(self):
            return self.getToken(HTMLParser.VOID_NAME, 0)

        def getRuleIndex(self):
            return HTMLParser.RULE_attrValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrValue" ):
                listener.enterAttrValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrValue" ):
                listener.exitAttrValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrValue" ):
                return visitor.visitAttrValue(self)
            else:
                return visitor.visitChildren(self)




    def attrValue(self):

        localctx = HTMLParser.AttrValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
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





