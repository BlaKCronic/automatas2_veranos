lexer grammar HTMLLexer;

// ============================================================
// Analizador lexico para un subconjunto representativo de HTML5.
//
// Alcance deliberado (ver Readme.md para justificacion completa):
//   - Se reconoce DOCTYPE, comentarios, elementos, atributos,
//     texto y elementos vacios (void elements).
//   - El contenido de <style> y <script> se trata como TEXTO
//     plano (no se re-analiza como CSS/JS dentro de HTML). CSS
//     se analiza por separado con CSS.g4 cuando se sube un
//     archivo .css independiente.
//   - Se usan modos de lexer porque HTML es sensible al contexto:
//     fuera de una etiqueta el "alfabeto" es texto libre, dentro
//     de una etiqueta (<...>) el alfabeto son nombres, '=',
//     cadenas y '>'/'/>' .
// ============================================================

options {
    caseInsensitive = true;
}

// ---------------- MODO POR DEFECTO (texto) ----------------

DOCTYPE
    : '<!DOCTYPE' ~[>]* '>'
    ;

COMMENT
    : '<!--' .*? '-->'
    ;

CDATA
    : '<![CDATA[' .*? ']]>'
    ;

TAG_OPEN_SLASH
    : '</' -> pushMode(TAG)
    ;

TAG_OPEN
    : '<' -> pushMode(TAG)
    ;

// Texto plano: cualquier secuencia de caracteres que no inicie una etiqueta.
TEXT
    : ~[<]+
    ;

// ---------------- MODO TAG: dentro de <...> ----------------

mode TAG;

TAG_CLOSE
    : '>' -> popMode
    ;

TAG_SELFCLOSE
    : '/>' -> popMode
    ;

EQUALS
    : '='
    ;

STRING
    : '"' ~["]* '"'
    | '\'' ~[']* '\''
    ;

// Nombres de elementos "vacios" (void elements) de HTML5: nunca llevan
// etiqueta de cierre. Se reconocen como un token aparte (declarado ANTES
// de NAME) para que la gramatica pueda distinguir sintacticamente un
// elemento vacio de uno normal sin necesidad de comparar cadenas en
// tiempo de parseo, evitando asi que una etiqueta de cierre lejana
// termine emparejandose por error con la etiqueta vacia mas cercana.
VOID_NAME
    : 'area' | 'base' | 'br' | 'col' | 'embed' | 'hr' | 'img' | 'input'
    | 'link' | 'meta' | 'param' | 'source' | 'track' | 'wbr'
    ;

// Nombres de etiquetas y atributos: letras, digitos, guion, dos puntos y guion bajo
// (permite atributos tipo data-*, aria-*, xml:lang, etc.)
NAME
    : [a-z_] [a-z0-9\-_:.]*
    ;

TAG_WS
    : [ \t\r\n]+ -> skip
    ;
