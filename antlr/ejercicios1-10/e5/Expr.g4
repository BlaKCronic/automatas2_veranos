grammar Expr;

root: expr EOF;

expr: EOF;

PRINT: [Pp][Rr][Ii][Nn][Tt];
CADENA: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;