from flask import Flask, request, render_template, jsonify
import ply.lex as lex

# Configuración de Flask
app = Flask(__name__)

# Lista de nombres de tokens
tokens = (
    'NUMERO',
    'PARENTESIS_IZQUIERDO',
    'PARENTESIS_DERECHO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'IGUAL',
    'PUNTO',
)

# Definición de los tokens
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_IGUAL = r'='
t_PUNTO = r'\.'

# Regla para identificar números
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Ignorar espacios en blanco
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()

# Función para analizar la expresión
def analizar_expresion(expresion):
    lexer.input(expresion)
    tokens = []
    for tok in lexer:
        tokens.append({'token': tok.value, 'tipo': tok.type})
    return tokens

# Ruta para mostrar el HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la expresión matemática
@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.get_json()
    expresion = data.get('expresion', '')
    tokens = analizar_expresion(expresion)
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(debug=True)
