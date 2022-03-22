import ply.yacc as yacc
from ejemplo import tokens 


names = { }

def p_statement_assign(t):
    'statement : KEY EQUAL expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression EXTRA expression
                  | expression QUIT expression
                  | expression HOUR expression
                  | expression ENTRE expression
                  | expression ELEV expression
                  | expression MAQ expression
                  | expression MEQ expression
                  | expression MAI expression
                  | expression MEI expression
                  | expression COMPARE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>': t[0] = t[1] > t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]

def p_expression_group(t):
    'expression : LEFT expression RIGHT'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMERIC'
    t[0] = t[1]

def p_expression_name(t):
    'expression : KEY'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print(f"No se encuentra: {t[1]}")
        t[0] = 0

def p_error(t):
    print(f'Error sintactico: {t[1]}')

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
   