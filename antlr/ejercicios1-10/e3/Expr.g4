grammar Expr;

root: expr EOF;

expr: EOF;

ID: [a-zA-Z]+;
IGUAL: '=';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;