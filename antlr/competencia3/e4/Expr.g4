grammar Expr;

root: expr EOF;

expr: IF cond;

cond: operand MAYORQUE operand;

operand: ID | NUM;

IF: 'if';
ID: [a-zA-Z]+;
MAYORQUE: '>';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;