grammar CSS;

// ============================================================
// Gramatica combinada (lexica + sintactica) para un subconjunto
// representativo de CSS3.
//
// Alcance deliberado (ver Readme.md):
//   - Selectores: tipo, universal, clase, id, atributo,
//     pseudo-clase, pseudo-elemento y combinadores (descendiente,
//     hijo directo >, hermano adyacente +, hermano general ~).
//   - At-rules soportadas explicitamente: @media, @import,
//     @font-face, @keyframes.
//   - Declaraciones propiedad:valor con numeros+unidad,
//     porcentajes, colores hex, strings, funciones (rgb(), url(),
//     calc(), etc.) y !important.
//   - No se valida la aritmetica interna de calc(): se reconoce
//     sintacticamente como lista de tokens dentro de parentesis.
//   - No se distingue lexicamente una "unidad" (px, em, s, ...)
//     de un identificador cualquiera: esa ambiguedad (p.ej. el
//     selector de etiqueta "s" vs la unidad "s" de segundos) se
//     resuelve dejando que el analizador semantico valide si el
//     identificador que sigue a un numero es una unidad conocida.
// ============================================================

options {
    caseInsensitive = true;
}

// ---------------- REGLAS SINTACTICAS ----------------

styleSheet
    : (atRule | ruleSet)* EOF
    ;

ruleSet
    : selectorList LBRACE declaration* RBRACE
    ;

selectorList
    : selector (COMMA selector)*
    ;

selector
    : simpleSelector (combinator? simpleSelector)*
    ;

combinator
    : GT
    | PLUS
    | TILDE
    ;

simpleSelector
    : selectorPart+
    ;

selectorPart
    : elementName
    | STAR
    | classSelector
    | idSelector
    | attrSelector
    | pseudoClass
    | pseudoElement
    ;

elementName
    : IDENT
    ;

classSelector
    : DOT IDENT
    ;

idSelector
    : HASH
    ;

attrSelector
    : LBRACK IDENT (attrOp (STRING | IDENT))? RBRACK
    ;

attrOp
    : EQ
    | TILDEEQ
    | PIPEEQ
    | CARETEQ
    | DOLLAREQ
    | STAREQ
    ;

pseudoClass
    : COLON IDENT (LPAREN (IDENT | NUMBER)? RPAREN)?
    ;

pseudoElement
    : COLONCOLON IDENT
    ;

atRule
    : mediaRule
    | importRule
    | fontFaceRule
    | keyframesRule
    ;

mediaRule
    : AT_MEDIA mediaQueryList LBRACE ruleSet* RBRACE
    ;

mediaQueryList
    : mediaQuery (COMMA mediaQuery)*
    ;

mediaQuery
    : IDENT? (AND? LPAREN IDENT (COLON value)? RPAREN)*
    ;

importRule
    : AT_IMPORT (STRING | funcCall) IDENT* SEMI
    ;

fontFaceRule
    : AT_FONTFACE LBRACE declaration* RBRACE
    ;

keyframesRule
    : AT_KEYFRAMES IDENT LBRACE keyframeBlock* RBRACE
    ;

keyframeBlock
    : keyframeSelector (COMMA keyframeSelector)* LBRACE declaration* RBRACE
    ;

keyframeSelector
    : IDENT
    | PERCENTAGE
    ;

declaration
    : property COLON valueList IMPORTANT? SEMI?
    ;

property
    : IDENT
    ;

valueList
    : value+
    ;

value
    : MINUS? DIMENSION
    | MINUS? NUMBER
    | PERCENTAGE
    | HASH
    | STRING
    | funcCall
    | IDENT
    | COMMA
    ;

funcCall
    : IDENT LPAREN funcContent? RPAREN
    ;

funcContent
    : funcToken+
    ;

funcToken
    : value
    | PLUS
    | MINUS
    | STAR
    | SLASH
    ;

// ---------------- REGLAS LEXICAS ----------------

COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

AT_MEDIA: '@media';
AT_IMPORT: '@import';
AT_FONTFACE: '@font-face';
AT_KEYFRAMES: '@keyframes' | '@-webkit-keyframes' | '@-moz-keyframes';
IMPORTANT: '!important';
AND: 'and';

STRING
    : '"' (~["\r\n])* '"'
    | '\'' (~['\r\n])* '\''
    ;

HASH
    : '#' [a-z0-9_\-]+
    ;

PERCENTAGE
    : MINUS? DIGITS ('.' DIGITS)? '%'
    | MINUS? '.' DIGITS '%'
    ;

// Numero pegado inmediatamente (sin espacio) a letras: "10px", "1.5em",
// "2deg". Se reconoce como UN solo token a nivel LEXICO -a proposito-
// porque el espacio en blanco se descarta (-> skip) antes de llegar al
// parser: si "unidad" se intentara resolver a nivel sintactico (numero
// token + identificador token) no habria forma de distinguir "10px"
// (numero+unidad) de "0 auto" (dos valores separados por un espacio),
// ya que ambos se verian identicos como secuencia de tokens NUMBER
// IDENT. El nombre de la unidad en si NO se valida aqui (ver mas abajo
// por que no conviene una lista fija de unidades a nivel lexico); eso
// lo hace el analizador semantico con el texto del token.
DIMENSION
    : (DIGITS ('.' DIGITS)? | '.' DIGITS) [a-z]+
    ;

NUMBER
    : DIGITS ('.' DIGITS)?
    | '.' DIGITS
    ;

fragment DIGITS: [0-9]+;

// Identificadores CSS: no pueden empezar con un guion seguido de un
// digito (eso se reserva para numeros negativos, ej. "-10px"), pero si
// pueden empezar con un guion seguido de letra (prefijos de motor, ej.
// "-webkit-transform") o con doble guion (propiedades personalizadas,
// ej. "--color-principal").
IDENT
    : [a-z_] [a-z0-9_\-]*
    | '-' [a-z_] [a-z0-9_\-]*
    | '-' '-' [a-z0-9_\-]*
    ;

LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
COLONCOLON: '::';
COLON: ':';
SEMI: ';';
COMMA: ',';
DOT: '.';
GT: '>';
PLUS: '+';
TILDE: '~';
STAR: '*';
SLASH: '/';
MINUS: '-';
TILDEEQ: '~=';
PIPEEQ: '|=';
CARETEQ: '^=';
DOLLAREQ: '$=';
STAREQ: '*=';
EQ: '=';
