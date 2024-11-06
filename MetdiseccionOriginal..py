import numpy as np
from numpy import sin, cos, tan 
import math

def mt_seccion(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Los números a y b no se encuentran en medio de la raíz")

    m = (a + b) / 2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return mt_seccion(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)): 
        return mt_seccion(f, a, m, tol)

# ingrese la función
f = lambda x: np.log(1/x)

r1 = mt_seccion(f, 0.5, 4, 0.1) 
print("r1", r1)

r01 = mt_seccion(f, 0.5, 4, 0.01)
print("r01", r01)
print("f(r1)=", f(r1))
print("f(r01)", f(r01))
