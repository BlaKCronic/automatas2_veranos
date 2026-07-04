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
    : CREATE | TABLE | SERIAL | PRIMARY | KEY | VARCHAR | NOT | NULL
    | INTEGER | DATE | INSERT | INTO | VALUES | SELECT | FROM
    | INNER | JOIN | ON | WHERE
    | IDENTIFICADOR | ENTERO | CADENA
    | IGUAL
    | PAR_IZQ | PAR_DER | COMA | PUNTO_COMA | PUNTO
    ;

// ---------- Palabras reservadas SQL ----------
CREATE  : 'CREATE' ;
TABLE   : 'TABLE' ;
SERIAL  : 'SERIAL' ;
PRIMARY : 'PRIMARY' ;
KEY     : 'KEY' ;
VARCHAR : 'VARCHAR' ;
NOT     : 'NOT' ;
NULL    : 'NULL' ;
INTEGER : 'INTEGER' ;
DATE    : 'DATE' ;
INSERT  : 'INSERT' ;
INTO    : 'INTO' ;
VALUES  : 'VALUES' ;
SELECT  : 'SELECT' ;
FROM    : 'FROM' ;
INNER   : 'INNER' ;
JOIN    : 'JOIN' ;
ON      : 'ON' ;
WHERE   : 'WHERE' ;

// ---------- Operadores ----------
IGUAL : '=' ;

// ---------- Simbolos ----------
PAR_IZQ    : '(' ;
PAR_DER    : ')' ;
COMA       : ',' ;
PUNTO_COMA : ';' ;
PUNTO      : '.' ;

// ---------- Literales e identificadores ----------
ENTERO        : [0-9]+ ;
CADENA        : '\'' (~['\r\n])* '\'' ;
IDENTIFICADOR : [a-zA-Z_] [a-zA-Z0-9_]* ;

// ---------- Espacios en blanco (ignorados) ----------
WS : [ \t\r\n]+ -> skip ;
