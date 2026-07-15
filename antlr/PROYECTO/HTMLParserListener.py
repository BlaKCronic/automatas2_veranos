# Generated from HTMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HTMLParser import HTMLParser
else:
    from HTMLParser import HTMLParser

# This class defines a complete listener for a parse tree produced by HTMLParser.
class HTMLParserListener(ParseTreeListener):

    # Enter a parse tree produced by HTMLParser#htmlDocument.
    def enterHtmlDocument(self, ctx:HTMLParser.HtmlDocumentContext):
        pass

    # Exit a parse tree produced by HTMLParser#htmlDocument.
    def exitHtmlDocument(self, ctx:HTMLParser.HtmlDocumentContext):
        pass


    # Enter a parse tree produced by HTMLParser#content.
    def enterContent(self, ctx:HTMLParser.ContentContext):
        pass

    # Exit a parse tree produced by HTMLParser#content.
    def exitContent(self, ctx:HTMLParser.ContentContext):
        pass


    # Enter a parse tree produced by HTMLParser#voidElement.
    def enterVoidElement(self, ctx:HTMLParser.VoidElementContext):
        pass

    # Exit a parse tree produced by HTMLParser#voidElement.
    def exitVoidElement(self, ctx:HTMLParser.VoidElementContext):
        pass


    # Enter a parse tree produced by HTMLParser#normalElement.
    def enterNormalElement(self, ctx:HTMLParser.NormalElementContext):
        pass

    # Exit a parse tree produced by HTMLParser#normalElement.
    def exitNormalElement(self, ctx:HTMLParser.NormalElementContext):
        pass


    # Enter a parse tree produced by HTMLParser#tagName.
    def enterTagName(self, ctx:HTMLParser.TagNameContext):
        pass

    # Exit a parse tree produced by HTMLParser#tagName.
    def exitTagName(self, ctx:HTMLParser.TagNameContext):
        pass


    # Enter a parse tree produced by HTMLParser#closeTagName.
    def enterCloseTagName(self, ctx:HTMLParser.CloseTagNameContext):
        pass

    # Exit a parse tree produced by HTMLParser#closeTagName.
    def exitCloseTagName(self, ctx:HTMLParser.CloseTagNameContext):
        pass


    # Enter a parse tree produced by HTMLParser#comment.
    def enterComment(self, ctx:HTMLParser.CommentContext):
        pass

    # Exit a parse tree produced by HTMLParser#comment.
    def exitComment(self, ctx:HTMLParser.CommentContext):
        pass


    # Enter a parse tree produced by HTMLParser#attribute.
    def enterAttribute(self, ctx:HTMLParser.AttributeContext):
        pass

    # Exit a parse tree produced by HTMLParser#attribute.
    def exitAttribute(self, ctx:HTMLParser.AttributeContext):
        pass


    # Enter a parse tree produced by HTMLParser#attrName.
    def enterAttrName(self, ctx:HTMLParser.AttrNameContext):
        pass

    # Exit a parse tree produced by HTMLParser#attrName.
    def exitAttrName(self, ctx:HTMLParser.AttrNameContext):
        pass


    # Enter a parse tree produced by HTMLParser#attrValue.
    def enterAttrValue(self, ctx:HTMLParser.AttrValueContext):
        pass

    # Exit a parse tree produced by HTMLParser#attrValue.
    def exitAttrValue(self, ctx:HTMLParser.AttrValueContext):
        pass



del HTMLParser