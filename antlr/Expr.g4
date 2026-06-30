grammar Expr;

root: expr EOF;

expr: EOF;

IF: 'if';
ID: [a-zA-Z_]+;
MAYOR_QUE: '>';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;