grammar Expr;

root: expr EOF;

expr: EOF;

IF: 'IF';
ID: [a-zA-Z]+;
MAYOR_QUE: '>';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;