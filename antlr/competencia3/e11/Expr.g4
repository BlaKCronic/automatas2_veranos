grammar Expr;

root: classDecl EOF;

classDecl: 'public' 'class' ID '{' methodDecl '}';

methodDecl: 'public' 'static' 'void' 'main' '(' 'String' '[' ']' ID ')' '{' stat* '}';

stat: varDecl
    | printStat
    ;

varDecl: TYPE ID '=' expr ';';

printStat: 'System' '.' 'out' '.' 'println' '(' expr ')' ';';

expr: expr op=('+'|'-') expr   # AddSub
    | expr op=('*'|'/') expr  # MulDiv
    | STRING                  # Str
    | NUM                     # Number
    | ID                      # Var
    ;

TYPE: 'int' | 'String' | 'double' | 'boolean';
STRING: '"' .*? '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;