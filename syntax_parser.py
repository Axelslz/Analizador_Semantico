import ply.yacc as yacc
from token_lexer import tokens, lexer

# Programa principal
def p_program(p):
    'program : statement_list'
    p[0] = p[1]

# Lista de declaraciones
def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

# Una declaración individual
def p_statement(p):
    '''statement : var_decl
                 | echo_statement
                 | function_decl
                 | repeat_statement
                 | if_statement
                 | return_statement'''
    p[0] = p[1]

# Declaración de una variable
def p_var_decl(p):
    'var_decl : INT IDENTIFIER EQUALS expression SEMICOLON'
    p[0] = ('var_decl', p[1], p[2], p[4])

# Impresión de una expresión
def p_echo_statement(p):
    'echo_statement : ECHO LPAREN expression RPAREN SEMICOLON'
    p[0] = ('echo', p[3])

# Declaración de función
def p_function_decl(p):
    'function_decl : FUNC IDENTIFIER LPAREN opt_param_list RPAREN LBRACE statement_list RBRACE'
    p[0] = ('function_decl', p[2], p[4], p[7])

# Lista opcional de parámetros
def p_opt_param_list(p):
    '''opt_param_list : param_list
                      | empty'''
    p[0] = p[1]

# Lista de parámetros
def p_param_list(p):
    '''param_list : param_list COMMA INT IDENTIFIER
                  | INT IDENTIFIER'''
    if len(p) == 5:
        p[0] = p[1] + [(p[3], p[4])]
    else:
        p[0] = [(p[1], p[2])]

# Bucle 'repetir'
def p_repeat_statement(p):
    'repeat_statement : REPEAT LPAREN var_decl expression SEMICOLON increment RPAREN LBRACE statement_list RBRACE'
    p[0] = ('repeat_statement', p[3], p[4], p[6], p[9])

# Condición
def p_condition(p):
    'condition : expression'
    p[0] = p[1]

# Incremento
def p_increment(p):
    'increment : IDENTIFIER PLUS PLUS SEMICOLON'
    p[0] = ('increment', p[1])

# Declaración 'si'
def p_if_statement(p):
    'if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE opt_else'
    p[0] = ('if_statement', p[3], p[6], p[8])

# Declaración 'sino' opcional
def p_opt_else(p):
    '''opt_else : ELSE LBRACE statement_list RBRACE
                | empty'''
    if len(p) > 1:
        p[0] = ('else', p[1], p[3])
    else:
        p[0] = None

# Declaración de retorno
def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = ('return', p[2])

# Elemento vacío
def p_empty(p):
    'empty :'
    p[0] = None

# Definición de una expresión
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MORE expression
                  | expression LESS expression
                  | NUMBER
                  | IDENTIFIER'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = ('add', p[1], p[3])
        elif p[2] == '-':
            p[0] = ('subtract', p[1], p[3])
        elif p[2] == '>':
            p[0] = ('more', p[1], p[3])
        elif p[2] == '<':
            p[0] = ('less', p[1], p[3])
    else:
        if isinstance(p[1], str) and p[1].startswith('$'):
            p[0] = (p[1])
        else:
            p[0] = p[1]

# Error sintáctico
def p_error(p):
    if p:
        print(f"Syntax error at {p.type} with value {p.value} at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Construir el parser
parser = yacc.yacc()

# Define a function to parse input data
def parse(data):
    lexer.input(data)
    return parser.parse(tokenfunc=lexer.token)
