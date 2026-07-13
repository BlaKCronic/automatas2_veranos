grammar Expr;

root: expr EOF;

expr: expr MENOS expr | NUM;

MENOS: '-';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;