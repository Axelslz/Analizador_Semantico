variable = []
value_variable = []
function_name = []
loacal_vars = []
out = ''
for_out = []


def generate_interpreter(simp):
    global out, variable, value_variable
    for i in simp:
        if i[0] == 'var_decl':
            if i[2] in variable:
                out += 'VARIABLE YA DEFINIDA'
            else:
                variable.append(i[2])
                value_variable.append(i[3])
        if i[0] == 'echo':
            print(i[1])
            if i[1] not in variable and i[1][0] == '$':
                out += "VARIABLE NO DECLARADA"
            elif i[1] in variable and i[1][0] == '$':
                out += value_variable[variable.index(i[0])]
            elif i[1][0] == 'add':
                if i[1][1] in variable:
                    if i[1][2] in variable:
                        out += str(value_variable[variable.index(i[1][1])] + value_variable[variable.index(i[1][2])])
                    else:
                        out += str(value_variable[variable.index(i[1][1])] + i[1][2])
                elif type(i[1][1]) == int:
                    if i[1][2] in variable:
                        out += str(i[1][1] + value_variable[variable.index(i[1][2])])
                    else:
                        out += str(i[1][1] + i[1][2])
                else:
                    out += "VARIABLE NO DECLARADA"
            elif i[1][0] == 'subtract':
                if i[1][1] in variable:
                    if i[1][2] in variable:
                        out += str(value_variable[variable.index(i[1][1])] - value_variable[variable.index(i[1][2])])
                    else:
                        out += str(value_variable[variable.index(i[1][1])] - i[1][2])
                elif type(i[1][1]) == int:
                    if i[1][2] in variable:
                        out += str(i[1][1] - value_variable[variable.index(i[1][2])])
                    else:
                        out += str(i[1][1] - i[1][2])
                else:
                    out += "VARIABLE NO DECLARADA"
            else:
                out += str(i[1])
        if i[0] == 'function_decl':
            if i[1] in function_name:
                out += "YA TA DECLARADA PIBE"
            else:
                function_name.append(i[0])
                if i[2] is not None:
                    if len(i[2]) > 1 and i[2]:
                        for j in i[2]:
                            if j[1] in variable:
                                out += 'VARIABLE YA DEFINIDA'
                                return out
                            else:
                                variable.append(j[1])
                    elif type(i[2]) == list:
                        variable.append(i[2][1])
                generate_interpreter(i[3])
        if i[0] == 'if_statement':
            print(i[1][0])
            if i[1][0] == 'more':
                print(i)
                if i[1][1] in variable:
                    print(i[1][2])
                    if i[1][2] in variable:
                        if value_variable[variable.index(i[1][1])] > value_variable[variable.index(i[1][2])]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    elif type(i[1][2]) == int:
                        if value_variable[variable.index(i[1][1])] > i[1][2]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][2])
                    else:
                        out += 'VARIABLE NO DECLARADA'
                elif type(i[1][1]) == int:
                    if i[1][2] in variable:
                        if i[1][1] > value_variable[variable.index(i[1][2])]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    elif type(i[1][2]) == int:
                        if i[1][1] > i[1][2]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    else:
                        out += 'VARIALBE NO DECLARADA'
                else:
                    out += 'VARIABLE NO DECLARADA'
            elif i[1][0] == 'less':
                if i[1][1] in variable:
                    if i[1][2] in variable:
                        if value_variable[variable.index(i[1][1])] < value_variable[variable.index(i[1][2])]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    elif type(i[1][2]) == int:
                        if value_variable[variable.index(i[1][1])] < i[1][2]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][2])
                    else:
                        out += 'VARIABLE NO DECLARADA'
                elif type(i[1][1]) == int:
                    if i[1][2] in variable:
                        if i[1][1] < value_variable[variable.index(i[1][2])]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    elif type(i[1][2]) == int:
                        if i[1][1] < i[1][2]:
                            generate_interpreter(i[2])
                        elif i[3][0] == 'else':
                            generate_interpreter(i[3][1])
                    else:
                        out += 'VARIALBE NO DECLARADA'
                else:
                    out += 'VARIABLE NO DECLARADA'
            else:
                out += 'ERROR DE COMPARACION'
        if i[0] == 'repeat_statement':
            print(i[4])
            if i[1] not in variable:
                variable.append(i[1][2])
                value_variable.append(i[1][3])
                for j in range(i[2][2]):
                    if i[4][0][1] in variable:
                        for_out.append(value_variable[variable.index(i[4][0][1])])
                    elif i[4][0][1][0] == '$' and i[4][0][1] not in variable:
                        out += 'VARIABLE NO DECLARADA'
                        return out
                    else:
                        for_out.append(i[4][0][1])
                    value_variable[variable.index(i[2][1])] += 1
                return for_out
            else:
                out += 'VARIABLE DECLARADA'
    return out
