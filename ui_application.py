import tkinter as tk
from tkinter import messagebox
from syntax_parser import parse
from execution_interpreter import generate_code, Environment
from generate import generate_interpreter
import generate

def procesar():
    generate.out = ''
    generate.for_out = []
    generate.variable = []
    generate.value_variable = []
    generate.function_name = []
    generate.loacal_vars = []
    entrada = text_area_entrada.get('1.0', tk.END).strip()  # Obtener y limpiar la entrada}}}}}
    if not entrada:
        messagebox.showerror("Error", "La entrada no puede estar vacía.")
        return

    resultado_parser = parse(entrada)
    salida = generate_interpreter(resultado_parser)
    text_area_lexico.delete('1.0', tk.END)
    text_area_lexico.insert(tk.END, str(resultado_parser))

    if type(salida) == list:
        text_area_python.delete('1.0', tk.END)
        for i in salida:
            text_area_python.insert(tk.END, str(i)+'\n')
    else:
        text_area_python.delete('1.0', tk.END)
        text_area_python.insert(tk.END, salida)

    env = Environment()
    messagebox.showinfo("Éxito", "Script procesado y ejecutado.")

root = tk.Tk()
root.title("Analizador semántico")

label_entrada = tk.Label(root, text="Entrada de código")
label_entrada.pack()
text_area_entrada = tk.Text(root, height=10, width=100)
text_area_entrada.pack(padx=10, pady=10)

boton_procesar = tk.Button(root, text="Procesar", command=procesar)
boton_procesar.pack(padx=10, pady=10)

label_lexico = tk.Label(root, text="Árbol de Análisis Sintáctico")
label_lexico.pack()
text_area_lexico = tk.Text(root, height=10, width=100)
text_area_lexico.pack(padx=10, pady=10)

label_python = tk.Label(root, text="Salida del intérprete")
label_python.pack()
text_area_python = tk.Text(root, height=10, width=100)
text_area_python.pack(padx=10, pady=10)

root.mainloop()
