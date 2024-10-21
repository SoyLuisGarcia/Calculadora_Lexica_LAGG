import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMERO',
    'OPERADOR_SUMA',
    'OPERADOR_RESTA',
    'OPERADOR_MULTIPLICACION',
    'OPERADOR_DIVISION',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
)

# Reglas para tokens simples
t_OPERADOR_SUMA = r'\+'
t_OPERADOR_RESTA = r'-'
t_OPERADOR_MULTIPLICACION = r'\*'
t_OPERADOR_DIVISION = r'/'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'

# Regla para números
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()
