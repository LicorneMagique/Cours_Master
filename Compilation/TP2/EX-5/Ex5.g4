// grammaire de vérification des parenthèses et cochets

grammar Ex5;

start: expr ';' EOF ;

expr: 'a' expr 'bb'
    |
    ;

CHARS : ~[ab] -> skip ; // skips all characters
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
