
from lib2to3.pgen2.token import EQUAL
import ply.lex as lex
import read_file
 



reserved = {
    'if' : 'IF', 
    'else' : 'ELSE',
    'for' : 'FOR' ,
    'while' : 'WHILE' ,
    'func' : 'FUNCTION',
    'class' : 'CLASS',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'return': "RETURN",
    'this' : "THIS"

}

tokens = (
        'KEY',
        'NUMERIC',
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
        'EQUAL',


        )
 
tokens = list(tokens) + list(reserved.values())

'''t_NUMERIC  = r'\d+'''
t_EXTRA= r'\+'
t_QUIT = r'\-'
t_HOUR= r'\*'
t_ENTRE = r'/'
t_ELEV = r'\*\*'
t_EQUAL= r'='
t_COMPARE= r'=='
t_DIST= r'!='
t_MAQ = r'<'
t_MEQ = r'>'
t_MEI = r'<='
t_MAI = r'>='
t_LEFT = r'\('
t_RIGHT = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LCOR = r'\['
t_RCOR= r'\]'


def t_KEY(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'KEY')
    return t

def t_CD0T(t):
    r''' '.*' | ".*" '''
    t.value = str(t.value)
    return t


def t_DCI(t):
   r'\d*\.\d+'
   t.value = float(t.value)
   return t

def t_NUMERIC(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter erroneo: '%s'" % t.value[0])
    t.lexer.skip(1)

#Ejecucion del analizador lexico
lexer = lex.lex()

if __name__ == '__main__':
    text = read_file.read_text()
    lexer.input(text)

    for token in lexer:
        print(token)