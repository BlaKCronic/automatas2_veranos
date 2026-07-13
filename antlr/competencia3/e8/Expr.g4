grammar Expr;

root: comp EOF;

comp: ID OP NUM;

OP: '>=' | '<=' | '==' | '!=' | '>' | '<';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;