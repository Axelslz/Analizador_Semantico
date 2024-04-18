class Environment:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            raise Exception(f"Variable '{name}' not defined.")

def generate_code(node, env=None):
    if env is None:
        env = Environment()

    if isinstance(node, list):
        last_value = None
        for n in node:
            last_value = generate_code(n, env)
        return last_value

    node_type = node[0]

    if node_type == 'var_decl':
        _, var_name, value = node
        env.set_variable(var_name, evaluate_expression(value, env))
        return env.get_variable(var_name)

    elif node_type == 'echo':
        _, expr = node
        value = evaluate_expression(expr, env)
        print(value)
        return value

    elif node_type == 'function_decl':
        _, func_name, params, body = node
        env.set_variable(func_name, (params, body))
        return None

    elif node_type == 'if_statement':
        _, condition, true_block, else_block = node
        if evaluate_expression(condition, env):
            generate_code(true_block, env)
        elif else_block is not None:
            generate_code(else_block, env)
        return None

    # Handle other node types as necessary

def evaluate_expression(expr, env):
    if isinstance(expr, tuple):
        op, left, right = expr
        if op == 'add':
            return evaluate_expression(left, env) + evaluate_expression(right, env)
        # Handle other operators as necessary
    elif isinstance(expr, str):
        # Handle variables and string literals
        if expr[0] == '$':  # Assuming variables are identified by a leading '$'
            return env.get_variable(expr[1:])
        else:
            return expr.strip('"')  # Remove quotes from string literals
    elif isinstance(expr, int):
        return expr
    else:
        raise Exception(f"Unrecognized expression: {expr}")

# Handle the parser error function as necessary
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}, line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Define a function to call the main routine, if your language uses a 'main' function as an entry point
def call_main(env):
    main_func = env.get_variable('main')
    if main_func is not None:
        _, params, body = main_func
        generate_code(body, env)


