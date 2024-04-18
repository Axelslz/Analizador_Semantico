import sys
from syntax_parser import parse
from token_lexer import lexer
from execution_interpreter import generate_code, Environment

def execute_parser(script):
    lexer.input(script)
    tokens = [(tok.type, tok.value) for tok in lexer]
    print("Análisis léxico completado sin errores. Mostrando tokens:\n")
    for tok in tokens:
        print(f"{tok[0]}: {tok[1]}")
    return tokens

def execute_code(script):
    result = parse(script)
    if result is not None:
        print("Análisis sintáctico completado sin errores.")
        env = Environment()
        output = generate_code(result, env)
        print("Ejecución completada.")
        return output
    else:
        print("Error de sintaxis: el parser no pudo procesar la entrada correctamente.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python run_program.py <archivo_de_codigo>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            script = file.read()
            print("Iniciando análisis léxico y sintáctico...\n")
            execute_parser(script)
            print("\nIniciando ejecución del código...\n")
            execute_code(script)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {filename}")
    except Exception as e:
        print(f"Error durante la ejecución del script: {e}")
