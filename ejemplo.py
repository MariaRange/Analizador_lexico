# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex
 
# List of token names.   This is always required



reserved = {
    'if' : 'IF', 
    'else' : 'ELSE',
    'for' : 'FOR' ,
    'while' : 'WHILE' ,
    'then' : 'THEN' ,

}

tokens = [
    'NUMERIC',
    'VARIABLE',
    'EXTRA',
    'QUIT',
    'HOUR',
    'ENTRE',
    'LEFT',
    'RIGHT',
    'COMPARE',
    'DIST',
    'MAQ',
    'MEQ',
    'MAI',
    'MEI',
    'LKEY',
    'RKEY',
    'LCOR',
    'RCOR',
    'COM',
    'ELEV',
] + list(reserved.values())
 
# Regular expression rules for simple tokens
t_NUMERIC  = r'\d+'
#t_VARIABLE =r'[a-zA-Z_][a-zA-Z_0-9]*'
t_EXTRA    = r'\+'
t_QUIT     = r'-'
t_HOUR     = r'\*'
t_ENTRE    = r'/'
t_LEFT     = r'\('
t_RIGHT    = r'\)'
t_COMPARE  = r'=='
t_DIST     = r'!='
t_MAQ      = r'>'
t_MEQ      = r'<'
t_MAI      = r'>='
t_MEI      = r'<='
t_LKEY     = r'\{'
t_RKEY     = r'\}'
t_LCOR     = r'\['
t_RCOR     = r'\]'
t_COM      = r'//'
t_ELEV     = r'\*\*'

# A regular expression rule with some action code
t_IF       = r'if'
t_ELSE     = r'else'
t_FOR      = r'for'
t_WHILE    = r'while'
t_THEN     = r'then'

# Check for reserved words
def t_VARIABLE(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'VARIABLE')    
     return t

# No return value. Token discarded
def t_COMMENT(t):
     r'\#.*'
     pass     
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Caracter Incorrecto '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()
 
 

with open('content.txt') as file:
    data = file.read()
# Test it out
#data = '''
# 3 + 4 * 10
#   + -20 *2
# '''
 
    # Give the lexer some input
    #sentencia=input("Ingresa una cadena: ")
    #lexer.input(sentencia)
    lexer.input(data)
    
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
 

 
#for tok in lexer:
#     print(tok)
 

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # No more input
#    print(tok.type, tok.value, tok.lineno, tok.lexpos)