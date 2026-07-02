grammar Expr;

root: expr EOF;

expr: EOF;

NUM: [0-9]+;
MENOS: '-';
WS: [ \t\r\n]+ -> skip;