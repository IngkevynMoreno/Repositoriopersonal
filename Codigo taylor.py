import tkinter as tk
from tkinter import messagebox, scrolledtext
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def calcular_taylor():

    funcion_str = entrada_funcion.get()
    a = float(entrada_a.get())
    n = int(entrada_n.get())

    try:
        x = sp.symbols('x')
        funcion = sp.sympify(funcion_str)


        resultado_polinomios.delete(1.0, tk.END)


        polinomios = []
        for i in range(n + 1):

            taylor_i = sum((funcion.diff(x, k).subs(x, a) / sp.factorial(k)) * (x - a) ** k for k in range(i + 1))
            polinomios.append(sp.simplify(taylor_i))
            resultado_polinomios.insert(tk.END, f"p_{i}(x) = {sp.simplify(taylor_i)}\n")

        graficar_funcion(funcion, polinomios, a)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def graficar_funcion(funcion, polinomios, a):
    x = sp.symbols('x')
    funcion_lambda = sp.lambdify(x, funcion, 'numpy')


    x_vals = np.linspace(a - 5, a + 5, 400)
    y_vals_funcion = funcion_lambda(x_vals)


    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals_funcion, label='Función Original', color='blue', linewidth=2)

    colores = ['red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']  
    for i, poli in enumerate(polinomios):

        polinomio_lambda = sp.lambdify(x, poli, 'numpy')
        

        y_vals_polinomio = np.array([polinomio_lambda(val) for val in x_vals])
        
        plt.plot(x_vals, y_vals_polinomio, linestyle='--', color=colores[i % len(colores)], label=f'p_{i}(x)', linewidth=1.5)

    plt.axvline(x=a, color='black', linestyle='--', label=f'Expansión en a={a}')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Aproximaciones del Polinomio de Taylor')
    plt.grid(True)
    plt.show()


ventana = tk.Tk()
ventana.title("Polinomio de Taylor")


tk.Label(ventana, text="Función (en términos de x):").grid(row=0, column=0, padx=10, pady=10)
entrada_funcion = tk.Entry(ventana, width=30)
entrada_funcion.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="a (punto de expansión):").grid(row=1, column=0, padx=10, pady=10)
entrada_a = tk.Entry(ventana, width=10)
entrada_a.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="n (grado del polinomio):").grid(row=2, column=0, padx=10, pady=10)
entrada_n = tk.Entry(ventana, width=10)
entrada_n.grid(row=2, column=1, padx=10, pady=10)


boton_calcular = tk.Button(ventana, text="Calcular y Graficar", command=calcular_taylor)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


tk.Label(ventana, text="Resultados de cada polinomio:").grid(row=4, column=0, columnspan=2, padx=10, pady=10)
resultado_polinomios = scrolledtext.ScrolledText(ventana, width=50, height=10)
resultado_polinomios.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


ventana.mainloop()