import ply.lex as lex

# Palabras reservadas y su correspondiente token
reserved = {
    'func': 'FUNC',
    'imprimir': 'ECHO',
    'si': 'IF',
    'sino': 'ELSE',
    'repetir': 'REPEAT',
    'retornar': 'RETURN',
    'int': 'INT'  # Asumiendo que 'int' es una palabra reservada para tipos de datos
}

# Tokens no reservados
tokens = [
    'IDENTIFIER', 'NUMBER', 'STRING', 'PLUS', 'MINUS', 'EQUALS', 'SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'MORE', 'LESS'
] + list(reserved.values())

# Reglas simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_MORE = r'>'
t_LESS = r'<'

# Reglas complejas
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')  # Remove the surrounding quotes
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert string to integer
    return t

def t_IDENTIFIER(t):
    r'\$?[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
