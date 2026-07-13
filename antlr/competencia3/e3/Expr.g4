grammar Expr;

root: expr EOF;

expr:expr IGUAL expr | NUM | ID;

ID: [a-zA-Z]+;
IGUAL: '=';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;