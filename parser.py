import ply.yacc as yacc
from ejemplo import tokens 

def p_expression_extra(p):
    'expression : expression EXTRA term'
    p[0] = p[1] + p[3]

def p_expression_quit(p):
    'expression : expression QUIT term'
    p[0] = p[1] - p[3]
    
def p_expression_numeric(p):
    'expression : expression NUMERIC'
    p[0] = p[1]

def p_term_hour(p):
    'term : term HOUR factor'
    p[0] = p[1] * p[3]

def p_term_entre(p):
     'term : term ENTRE factor'
     p[0] = p[1] / p[3]
 
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
 
def p_factor_numeric(p):
    'factor : NUMERIC'
    p[0] = p[1]

def p_factor_expr(p):
     'factor : LEFT expression RIGHT'
     p[0] = p[2]
 
 # Error rule for syntax errors
def p_error(p):
    print("Error sintactico!")

parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
   