grammar Expr;

// ----------------------------------------------------------------------
// Regla inicial del parser (se conserva para que ANTLR genere el parser).
// El analizador lexico solo usa el lexer, pero mantenemos una regla raiz
// para conservar la estructura del proyecto.
//
// Nota: las palabras reservadas se reconocen en MAYUSCULAS, tal como
// aparecen en el codigo SQL de prueba.
// ----------------------------------------------------------------------
programa: elemento* EOF ;

elemento
    : UPDATE | SET | WHERE
    | IDENTIFICADOR | ENTERO | CADENA
    | IGUAL
    | COMA | PUNTO_COMA
    ;

// ---------- Palabras reservadas SQL ----------
UPDATE : 'UPDATE' ;
SET    : 'SET' ;
WHERE  : 'WHERE' ;

// ---------- Operadores ----------
IGUAL : '=' ;

// ---------- Simbolos ----------
COMA       : ',' ;
PUNTO_COMA : ';' ;

// ---------- Literales e identificadores ----------
ENTERO        : [0-9]+ ;
CADENA        : '\'' (~['\r\n])* '\'' ;
IDENTIFICADOR : [a-zA-Z_] [a-zA-Z0-9_]* ;

// ---------- Espacios en blanco (ignorados) ----------
WS : [ \t\r\n]+ -> skip ;
