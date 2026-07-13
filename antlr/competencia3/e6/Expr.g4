grammar Expr;

root: expr EOF;

expr: expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr  # AddSub
    | NUM                     # Number
    ;

NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;