grammar Expr;

root: decl EOF;

decl: TYPE ID '=' NUM;

TYPE: 'int';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;