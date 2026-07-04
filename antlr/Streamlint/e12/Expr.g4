grammar Expr;

// ----------------------------------------------------------------------
// Regla inicial del parser (se conserva para que ANTLR genere el parser).
// El analizador lexico solo usa el lexer, pero mantenemos una regla raiz
// para conservar la estructura del proyecto.
// ----------------------------------------------------------------------
programa: elemento* EOF ;

elemento
    : PUBLIC | CLASS | STATIC | VOID | INT | IF
    | IDENTIFICADOR | ENTERO | CADENA
    | MAS | IGUAL | MAYOR_IGUAL
    | PAR_IZQ | PAR_DER | LLAVE_IZQ | LLAVE_DER
    | COR_IZQ | COR_DER | PUNTO_COMA | PUNTO | COMA
    ;

// ---------- Palabras reservadas ----------
PUBLIC : 'public' ;
CLASS  : 'class' ;
STATIC : 'static' ;
VOID   : 'void' ;
INT    : 'int' ;
IF     : 'if' ;

// ---------- Operadores ----------
MAS         : '+' ;
IGUAL       : '=' ;
MAYOR_IGUAL : '>=' ;

// ---------- Simbolos ----------
PAR_IZQ    : '(' ;
PAR_DER    : ')' ;
LLAVE_IZQ  : '{' ;
LLAVE_DER  : '}' ;
COR_IZQ    : '[' ;
COR_DER    : ']' ;
PUNTO_COMA : ';' ;
PUNTO      : '.' ;
COMA       : ',' ;

// ---------- Literales e identificadores ----------
ENTERO        : [0-9]+ ;
CADENA        : '"' (~["\r\n])* '"' ;
IDENTIFICADOR : [a-zA-Z_] [a-zA-Z0-9_]* ;

// ---------- Espacios en blanco (ignorados) ----------
WS : [ \t\r\n]+ -> skip ;
