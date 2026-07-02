grammar Expr;

root: expr EOF;

expr: EOF;

PRINT: [Pp][Rr][Ii][Nn][Tt];
L_PAREN: '(';
R_PAREN: ')';
CADENA: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;