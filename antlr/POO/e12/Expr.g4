grammar Expr;

program: line* EOF;

line: declaracion
    | asignacion
    | ifStmt
    | printStmt
    | bloque
    ;

declaracion: TIPO ID ASSIGN valor SEMICOLON;
asignacion: ID ASSIGN valor SEMICOLON;
ifStmt: IF LPAREN comparacion RPAREN bloque;
printStmt: SYSTEM_OUT_PRINTLN LPAREN valor (PLUS valor)* RPAREN SEMICOLON;
bloque: LBRACE line* RBRACE;

comparacion: ID GE NUM;
valor: NUM | TEXT | ID;

TIPO: 'int' | 'String';
IF: 'if';
SYSTEM_OUT_PRINTLN: 'System.out.println';
LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
ASSIGN: '=';
SEMICOLON: ';';
PLUS: '+';
GE: '>=';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
TEXT: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;