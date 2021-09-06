// grammaire de vérification des parenthèses et cochets

grammar Parentheses;

r: expr ';' EOF ;

expr: '(' expr ')' expr
    | '[' expr ']' expr
    |
    ;

CHARS : ~[()[\]] -> skip ; // skips all characters
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
