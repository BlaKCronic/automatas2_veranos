grammar Expr;

root: expr EOF;

expr: expr MAS expr | NUM;

MAS: '+';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;