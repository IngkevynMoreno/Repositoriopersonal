import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

#Desarrollado por Juan Sebastian Rubiano Ramos y Kevyn Sebastian Moreno Gomez

funcion_input = input("Introduce la función(ej. sin(x), exp(x), x**2): ")
x0 = float(input("Introduce el valor de a: "))
n = int(input("Introduce el valor de n: "))

# Convertir la entrada en una función simbólica
f = sp.sympify(funcion_input)

# Función para calcular el polinomio de Taylor
def taylor_series(f, x0, n):
    taylor_poly = 0
    for i in range(n + 1):
        f_deriv = f.diff(x, i)
        taylor_poly += (f_deriv.subs(x, x0) / sp.factorial(i)) * (x - x0)**i
    return taylor_poly

# Calcular el polinomio de Taylor
taylor_poly = taylor_series(f, x0, n)

# Convertir las funciones simbólicas a funciones numéricas para graficar
f_lambdified = sp.lambdify(x, f, 'numpy')
taylor_lambdified = sp.lambdify(x, taylor_poly, 'numpy')

# Crear un rango de valores para graficar
x_vals = np.linspace(x0 - 2*np.pi, x0 + 2*np.pi, 400)
f_vals = f_lambdified(x_vals)
taylor_vals = taylor_lambdified(x_vals)

# Graficar la función original y el polinomio de Taylor
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label=f'Función original: {funcion_input}', color='blue')
plt.plot(x_vals, taylor_vals, label=f'Polinomio de Taylor (orden {n})', linestyle='--', color='red')

# Graficar las derivadas
for i in range(1, n+1):
    f_deriv = f.diff(x, i)
    f_deriv_lambdified = sp.lambdify(x, f_deriv, 'numpy')
    deriv_vals = f_deriv_lambdified(x_vals)
    plt.plot(x_vals, deriv_vals, label=f'Derivada {i}', linestyle=':')

# Etiquetas y leyenda
plt.title(f'Función y polinomio de Taylor de orden {n} alrededor de x0={x0}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.grid(True)

# Mostrar gráfica
plt.show()

# Mostrar el polinomio de Taylor
print(f'Polinomio de Taylor de orden {n} en x0={x0}:')
sp.pprint(taylor_poly)