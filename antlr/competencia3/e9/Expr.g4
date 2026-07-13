grammar Expr;

root: ifStat EOF;

ifStat: IF '(' comp ')';

comp: ID OP NUM;

IF: 'if';
OP: '>=' | '<=' | '==' | '!=' | '>' | '<';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;