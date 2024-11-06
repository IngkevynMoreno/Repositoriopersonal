import numpy as np

def biseccion(f, a, b, tol):
    """
    Método de Bisección basado en el Teorema de Bolzano.
    
    Argumentos:
    f -- La función continua f(x)
    a -- El extremo inferior del intervalo
    b -- El extremo superior del intervalo
    tol -- La tolerancia, define cuán precisa debe ser la solución
    
    Retorna:
    La raíz aproximada dentro del intervalo [a, b]
    """
    
    # Verificación inicial del Teorema de Bolzano
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("La función no cambia de signo en el intervalo dado, no se puede aplicar el método de bisección.")
    
    # Iteraciones del método
    while (b - a) / 2.0 > tol:
        # Punto medio del intervalo
        m = (a + b) / 2.0
        
        # Si f(m) es suficientemente pequeño, asumimos que es la raíz
        if np.abs(f(m)) < tol:
            return m
        
        # Aplicar el teorema de Bolzano para decidir el nuevo intervalo
        if np.sign(f(a)) == np.sign(f(m)):
            a = m  # La raíz está en [m, b]
        else:
            b = m  # La raíz está en [a, m]
    
    # Retornar el punto medio como la raíz aproximada
    return (a + b) / 2.0

# Función de prueba, por ejemplo: f(x) = x^2 - 4
f = lambda x: x**2 - 4

# Intervalo donde la función cambia de signo [1, 3] (Bolzano garantiza raíz aquí)
a = 1
b = 3

# Tolerancia
tol = 1e-5

# Aplicar el método de Bisección
raiz = biseccion(f, a, b, tol)

print("Raíz aproximada:", raiz)
print("Valor de f(raiz):", f(raiz))
