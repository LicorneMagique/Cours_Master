grammar Arit1;

// MIF08@Lyon1 and CAP@ENSL, simple arit evaluator with semantic actions
// Reminder: lower-caps for parser rules, UPPER-CAPS for lexer rules.

prog:
      statement+ EOF
    ;

statement:
      expr SCOL    {print($expr.text+" = "+str($expr.val))} // print the value
    ;

expr returns [int val]:
  e1=expr MULT  e2=expr {$val=$e1.val*$e2.val} // MULT is * (matched before PLUS if possible)
    | e1=expr PLUS  e2=expr {$val=$e1.val+$e2.val} // PLUS is +
    | a=atom {$val=$a.val} // just copy the value
    ;

atom returns [int val]:
      INT               {$val = int($INT.text)} // get the value from the lexer
    | '(' expr ')'      {$val=$expr.val} // just copy the value
    ;


SCOL :      ';';
PLUS :      '+';
MINUS :     '-';
MULT :      '*';
DIV :       '/';

INT:        [0-9]+;

COMMENT
  : '//' ~[\r\n]* -> skip
  ;


NEWLINE:    '\r'? '\n' -> skip;
WS  :       (' '|'\t')+  -> skip;
