grammar Expr;

root: expr EOF;

expr: EOF;

IF: [Ii][Ff];
L_PAREN: '(';
R_PAREN: ')';
ID: [a-zA-Z]+;
MAYOR: '>';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;