grammar Expr;

root: expr EOF;

expr: EOF;

NUM: [0-9]+;
MAS: '+';
MULT: '*';
WS: [ \t\r\n]+ -> skip;