grammar Expr;

options {
  caseInsensitive = true;
}

program: statement* EOF;

statement: updateStmt;

updateStmt:
    UPDATE ID SET assignment (COMMA assignment)* WHERE condition SEMICOLON;

assignment:
    ID EQ literalValue;

condition:
    ID EQ literalValue;

literalValue:
    STRING
    | NUM
    | ID;

UPDATE: 'UPDATE';
SET: 'SET';
WHERE: 'WHERE';
COMMA: ',';
SEMICOLON: ';';
EQ: '=';
STRING: '\'' (~['\r\n])* '\'';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
