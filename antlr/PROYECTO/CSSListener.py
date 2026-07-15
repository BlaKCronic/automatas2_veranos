# Generated from CSS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSSParser import CSSParser
else:
    from CSSParser import CSSParser

# This class defines a complete listener for a parse tree produced by CSSParser.
class CSSListener(ParseTreeListener):

    # Enter a parse tree produced by CSSParser#styleSheet.
    def enterStyleSheet(self, ctx:CSSParser.StyleSheetContext):
        pass

    # Exit a parse tree produced by CSSParser#styleSheet.
    def exitStyleSheet(self, ctx:CSSParser.StyleSheetContext):
        pass


    # Enter a parse tree produced by CSSParser#ruleSet.
    def enterRuleSet(self, ctx:CSSParser.RuleSetContext):
        pass

    # Exit a parse tree produced by CSSParser#ruleSet.
    def exitRuleSet(self, ctx:CSSParser.RuleSetContext):
        pass


    # Enter a parse tree produced by CSSParser#selectorList.
    def enterSelectorList(self, ctx:CSSParser.SelectorListContext):
        pass

    # Exit a parse tree produced by CSSParser#selectorList.
    def exitSelectorList(self, ctx:CSSParser.SelectorListContext):
        pass


    # Enter a parse tree produced by CSSParser#selector.
    def enterSelector(self, ctx:CSSParser.SelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#selector.
    def exitSelector(self, ctx:CSSParser.SelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#combinator.
    def enterCombinator(self, ctx:CSSParser.CombinatorContext):
        pass

    # Exit a parse tree produced by CSSParser#combinator.
    def exitCombinator(self, ctx:CSSParser.CombinatorContext):
        pass


    # Enter a parse tree produced by CSSParser#simpleSelector.
    def enterSimpleSelector(self, ctx:CSSParser.SimpleSelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#simpleSelector.
    def exitSimpleSelector(self, ctx:CSSParser.SimpleSelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#selectorPart.
    def enterSelectorPart(self, ctx:CSSParser.SelectorPartContext):
        pass

    # Exit a parse tree produced by CSSParser#selectorPart.
    def exitSelectorPart(self, ctx:CSSParser.SelectorPartContext):
        pass


    # Enter a parse tree produced by CSSParser#elementName.
    def enterElementName(self, ctx:CSSParser.ElementNameContext):
        pass

    # Exit a parse tree produced by CSSParser#elementName.
    def exitElementName(self, ctx:CSSParser.ElementNameContext):
        pass


    # Enter a parse tree produced by CSSParser#classSelector.
    def enterClassSelector(self, ctx:CSSParser.ClassSelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#classSelector.
    def exitClassSelector(self, ctx:CSSParser.ClassSelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#idSelector.
    def enterIdSelector(self, ctx:CSSParser.IdSelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#idSelector.
    def exitIdSelector(self, ctx:CSSParser.IdSelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#attrSelector.
    def enterAttrSelector(self, ctx:CSSParser.AttrSelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#attrSelector.
    def exitAttrSelector(self, ctx:CSSParser.AttrSelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#attrOp.
    def enterAttrOp(self, ctx:CSSParser.AttrOpContext):
        pass

    # Exit a parse tree produced by CSSParser#attrOp.
    def exitAttrOp(self, ctx:CSSParser.AttrOpContext):
        pass


    # Enter a parse tree produced by CSSParser#pseudoClass.
    def enterPseudoClass(self, ctx:CSSParser.PseudoClassContext):
        pass

    # Exit a parse tree produced by CSSParser#pseudoClass.
    def exitPseudoClass(self, ctx:CSSParser.PseudoClassContext):
        pass


    # Enter a parse tree produced by CSSParser#pseudoElement.
    def enterPseudoElement(self, ctx:CSSParser.PseudoElementContext):
        pass

    # Exit a parse tree produced by CSSParser#pseudoElement.
    def exitPseudoElement(self, ctx:CSSParser.PseudoElementContext):
        pass


    # Enter a parse tree produced by CSSParser#atRule.
    def enterAtRule(self, ctx:CSSParser.AtRuleContext):
        pass

    # Exit a parse tree produced by CSSParser#atRule.
    def exitAtRule(self, ctx:CSSParser.AtRuleContext):
        pass


    # Enter a parse tree produced by CSSParser#mediaRule.
    def enterMediaRule(self, ctx:CSSParser.MediaRuleContext):
        pass

    # Exit a parse tree produced by CSSParser#mediaRule.
    def exitMediaRule(self, ctx:CSSParser.MediaRuleContext):
        pass


    # Enter a parse tree produced by CSSParser#mediaQueryList.
    def enterMediaQueryList(self, ctx:CSSParser.MediaQueryListContext):
        pass

    # Exit a parse tree produced by CSSParser#mediaQueryList.
    def exitMediaQueryList(self, ctx:CSSParser.MediaQueryListContext):
        pass


    # Enter a parse tree produced by CSSParser#mediaQuery.
    def enterMediaQuery(self, ctx:CSSParser.MediaQueryContext):
        pass

    # Exit a parse tree produced by CSSParser#mediaQuery.
    def exitMediaQuery(self, ctx:CSSParser.MediaQueryContext):
        pass


    # Enter a parse tree produced by CSSParser#importRule.
    def enterImportRule(self, ctx:CSSParser.ImportRuleContext):
        pass

    # Exit a parse tree produced by CSSParser#importRule.
    def exitImportRule(self, ctx:CSSParser.ImportRuleContext):
        pass


    # Enter a parse tree produced by CSSParser#fontFaceRule.
    def enterFontFaceRule(self, ctx:CSSParser.FontFaceRuleContext):
        pass

    # Exit a parse tree produced by CSSParser#fontFaceRule.
    def exitFontFaceRule(self, ctx:CSSParser.FontFaceRuleContext):
        pass


    # Enter a parse tree produced by CSSParser#keyframesRule.
    def enterKeyframesRule(self, ctx:CSSParser.KeyframesRuleContext):
        pass

    # Exit a parse tree produced by CSSParser#keyframesRule.
    def exitKeyframesRule(self, ctx:CSSParser.KeyframesRuleContext):
        pass


    # Enter a parse tree produced by CSSParser#keyframeBlock.
    def enterKeyframeBlock(self, ctx:CSSParser.KeyframeBlockContext):
        pass

    # Exit a parse tree produced by CSSParser#keyframeBlock.
    def exitKeyframeBlock(self, ctx:CSSParser.KeyframeBlockContext):
        pass


    # Enter a parse tree produced by CSSParser#keyframeSelector.
    def enterKeyframeSelector(self, ctx:CSSParser.KeyframeSelectorContext):
        pass

    # Exit a parse tree produced by CSSParser#keyframeSelector.
    def exitKeyframeSelector(self, ctx:CSSParser.KeyframeSelectorContext):
        pass


    # Enter a parse tree produced by CSSParser#declaration.
    def enterDeclaration(self, ctx:CSSParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CSSParser#declaration.
    def exitDeclaration(self, ctx:CSSParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CSSParser#property.
    def enterProperty(self, ctx:CSSParser.PropertyContext):
        pass

    # Exit a parse tree produced by CSSParser#property.
    def exitProperty(self, ctx:CSSParser.PropertyContext):
        pass


    # Enter a parse tree produced by CSSParser#valueList.
    def enterValueList(self, ctx:CSSParser.ValueListContext):
        pass

    # Exit a parse tree produced by CSSParser#valueList.
    def exitValueList(self, ctx:CSSParser.ValueListContext):
        pass


    # Enter a parse tree produced by CSSParser#value.
    def enterValue(self, ctx:CSSParser.ValueContext):
        pass

    # Exit a parse tree produced by CSSParser#value.
    def exitValue(self, ctx:CSSParser.ValueContext):
        pass


    # Enter a parse tree produced by CSSParser#funcCall.
    def enterFuncCall(self, ctx:CSSParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CSSParser#funcCall.
    def exitFuncCall(self, ctx:CSSParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CSSParser#funcContent.
    def enterFuncContent(self, ctx:CSSParser.FuncContentContext):
        pass

    # Exit a parse tree produced by CSSParser#funcContent.
    def exitFuncContent(self, ctx:CSSParser.FuncContentContext):
        pass


    # Enter a parse tree produced by CSSParser#funcToken.
    def enterFuncToken(self, ctx:CSSParser.FuncTokenContext):
        pass

    # Exit a parse tree produced by CSSParser#funcToken.
    def exitFuncToken(self, ctx:CSSParser.FuncTokenContext):
        pass



del CSSParser