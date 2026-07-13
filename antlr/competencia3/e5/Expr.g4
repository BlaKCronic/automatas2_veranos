grammar Expr;

root: printStat EOF;

printStat: PRINT STRING;

PRINT: 'print';
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;