grammar Expr;

program: line* EOF;

line: palabra
    | numero
    | simbolo
    | texto
    | printCall
    ;

palabra: ID;
numero: NUMBER;
simbolo: '+' | '=' | ';' | '(' | ')' | '{' | '}' | '[' | ']' | '.';
texto: TEXT;
printCall: SYSTEM_OUT_PRINTLN;

SYSTEM_OUT_PRINTLN: 'System.out.println';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
TEXT: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;
