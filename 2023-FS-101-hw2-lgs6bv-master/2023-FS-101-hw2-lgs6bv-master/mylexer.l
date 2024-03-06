/* A starting flex file */
		               /* ---- PROLOGUE ---- */
%{
#include <iostream>
using namespace std;

#include <iomanip>

int no_lines = 1;
int n_tokens = 0;
%}
		              /* ---- DEFINITIONS ---- */
%option noyywrap
DIGIT		[0-9]
CHAR        [a-zA-Z]
INTCONST    (\+|\-)?{DIGIT}+
DECCONST    {INTCONST}\.{DIGIT}+
SCICONST    {DECCONST}[E]{INTCONST}          
HEXCONST    [A-F0-9]+[H]
BINCONST    [0-1]+[B]
KEYWORD     (FUNCTION|IF|FI|LOOP|POOL|PRINT)
STRCONST    [\"][^ \t\n]+[\"]
CHCONST     [A-F0-9]{2}[X]
IDNET       {CHAR}({CHAR}|{DIGIT}|[_])*
OPERATORS   (\+|\-|\*|\/|\<|\>|\=|\&|#)
COMMENTS    [%].*

%%  		              /* ---- REGULAR EXPRESSIONS ---- */

[ \t]           ;
\n              { no_lines++; }
{INTCONST}      { cout << setw(2) << n_tokens << ": TOKEN: INTCONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{DECCONST}      { cout << setw(2) << n_tokens << ": TOKEN: DECCONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{SCICONST}      { cout << setw(2) << n_tokens << ": TOKEN: SCICONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{HEXCONST}      { cout << setw(2) << n_tokens << ": TOKEN: HEXCONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{BINCONST}      { cout << setw(2) << n_tokens << ": TOKEN: BINCONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{KEYWORD}       { cout << setw(2) << n_tokens << ": TOKEN: KEYWORD " << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{STRCONST}      { cout << setw(2) << n_tokens << ": TOKEN: STRCONST" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{CHCONST}       { cout << setw(2) << n_tokens << ": TOKEN: CHCONST " << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{IDNET}         { cout << setw(2) << n_tokens << ": TOKEN: IDENT   " << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{OPERATORS}     { cout << setw(2) << n_tokens << ": TOKEN: OPERATOR" << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }
{COMMENTS}      ; /* { cout << setw(2) << n_tokens << ": TOKEN: COMMENT " << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; } */
.               { cout << setw(2) << n_tokens << ": TOKEN: ?       " << setw(11) << "LEXEME: " << yytext << endl; n_tokens++; }

%%  		              /* ---- EPILOGUE ---- */

int main()
{
    yylex();
    cout << no_lines << " lines processed." << endl;
    return 0;
}
