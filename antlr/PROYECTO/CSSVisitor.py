# Generated from CSS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSSParser import CSSParser
else:
    from CSSParser import CSSParser

# This class defines a complete generic visitor for a parse tree produced by CSSParser.

class CSSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSSParser#styleSheet.
    def visitStyleSheet(self, ctx:CSSParser.StyleSheetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#ruleSet.
    def visitRuleSet(self, ctx:CSSParser.RuleSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#selectorList.
    def visitSelectorList(self, ctx:CSSParser.SelectorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#selector.
    def visitSelector(self, ctx:CSSParser.SelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#combinator.
    def visitCombinator(self, ctx:CSSParser.CombinatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#simpleSelector.
    def visitSimpleSelector(self, ctx:CSSParser.SimpleSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#selectorPart.
    def visitSelectorPart(self, ctx:CSSParser.SelectorPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#elementName.
    def visitElementName(self, ctx:CSSParser.ElementNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#classSelector.
    def visitClassSelector(self, ctx:CSSParser.ClassSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#idSelector.
    def visitIdSelector(self, ctx:CSSParser.IdSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#attrSelector.
    def visitAttrSelector(self, ctx:CSSParser.AttrSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#attrOp.
    def visitAttrOp(self, ctx:CSSParser.AttrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#pseudoClass.
    def visitPseudoClass(self, ctx:CSSParser.PseudoClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#pseudoElement.
    def visitPseudoElement(self, ctx:CSSParser.PseudoElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#atRule.
    def visitAtRule(self, ctx:CSSParser.AtRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#mediaRule.
    def visitMediaRule(self, ctx:CSSParser.MediaRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#mediaQueryList.
    def visitMediaQueryList(self, ctx:CSSParser.MediaQueryListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#mediaQuery.
    def visitMediaQuery(self, ctx:CSSParser.MediaQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#importRule.
    def visitImportRule(self, ctx:CSSParser.ImportRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#fontFaceRule.
    def visitFontFaceRule(self, ctx:CSSParser.FontFaceRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#keyframesRule.
    def visitKeyframesRule(self, ctx:CSSParser.KeyframesRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#keyframeBlock.
    def visitKeyframeBlock(self, ctx:CSSParser.KeyframeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#keyframeSelector.
    def visitKeyframeSelector(self, ctx:CSSParser.KeyframeSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#declaration.
    def visitDeclaration(self, ctx:CSSParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#property.
    def visitProperty(self, ctx:CSSParser.PropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#valueList.
    def visitValueList(self, ctx:CSSParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#value.
    def visitValue(self, ctx:CSSParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#funcCall.
    def visitFuncCall(self, ctx:CSSParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#funcContent.
    def visitFuncContent(self, ctx:CSSParser.FuncContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSSParser#funcToken.
    def visitFuncToken(self, ctx:CSSParser.FuncTokenContext):
        return self.visitChildren(ctx)



del CSSParser