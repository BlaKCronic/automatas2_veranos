grammar Expr;

options {
  caseInsensitive = true;
}

program: statement* EOF;

statement
    : createTableStmt
    | insertStmt
    | selectStmt
    ;

createTableStmt:
    CREATE TABLE ID LPAREN columnDef (COMMA columnDef)* RPAREN SEMICOLON;

columnDef:
    ID typeDef columnConstraint*;

typeDef:
    SERIAL
    | INTEGER
    | VARCHAR LPAREN NUM RPAREN
    | DATE;

columnConstraint:
    NOT NULL
    | PRIMARY KEY;

insertStmt:
    INSERT INTO ID LPAREN columnName (COMMA columnName)* RPAREN VALUES valueList (COMMA valueList)* SEMICOLON;

valueList:
    LPAREN literalValue (COMMA literalValue)* RPAREN;

literalValue:
    STRING
    | NUM
    | ID;

selectStmt:
    SELECT selectItem (COMMA selectItem)*
    FROM tableRef (INNER JOIN tableRef ON condition)?
    WHERE condition SEMICOLON;

selectItem:
    columnName;

tableRef:
    ID alias?;

alias:
    ID;

condition:
    columnName EQ valueExpr;

valueExpr:
    literalValue
    | columnName;

columnName:
    ID (DOT ID)*;

CREATE: 'CREATE';
TABLE: 'TABLE';
INSERT: 'INSERT';
INTO: 'INTO';
VALUES: 'VALUES';
SELECT: 'SELECT';
FROM: 'FROM';
INNER: 'INNER';
JOIN: 'JOIN';
ON: 'ON';
WHERE: 'WHERE';
SERIAL: 'SERIAL';
INTEGER: 'INTEGER';
VARCHAR: 'VARCHAR';
DATE: 'DATE';
PRIMARY: 'PRIMARY';
KEY: 'KEY';
NOT: 'NOT';
NULL: 'NULL';
EQ: '=';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
SEMICOLON: ';';
DOT: '.';
STRING: '\'' (~['\r\n])* '\'';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
