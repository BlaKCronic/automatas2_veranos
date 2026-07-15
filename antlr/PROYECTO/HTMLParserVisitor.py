# Generated from HTMLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HTMLParser import HTMLParser
else:
    from HTMLParser import HTMLParser

# This class defines a complete generic visitor for a parse tree produced by HTMLParser.

class HTMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HTMLParser#htmlDocument.
    def visitHtmlDocument(self, ctx:HTMLParser.HtmlDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#content.
    def visitContent(self, ctx:HTMLParser.ContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#voidElement.
    def visitVoidElement(self, ctx:HTMLParser.VoidElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#normalElement.
    def visitNormalElement(self, ctx:HTMLParser.NormalElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#tagName.
    def visitTagName(self, ctx:HTMLParser.TagNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#closeTagName.
    def visitCloseTagName(self, ctx:HTMLParser.CloseTagNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#comment.
    def visitComment(self, ctx:HTMLParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#attribute.
    def visitAttribute(self, ctx:HTMLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#attrName.
    def visitAttrName(self, ctx:HTMLParser.AttrNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HTMLParser#attrValue.
    def visitAttrValue(self, ctx:HTMLParser.AttrValueContext):
        return self.visitChildren(ctx)



del HTMLParser