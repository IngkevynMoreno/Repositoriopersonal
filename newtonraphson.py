import sympy as sp

x = sp.symbols('x')
f = sp.sympify(input("funcion:" ))


f_deriv = sp.diff(f, x)
print("La derivada de", f, "es =", f_deriv)

x1 = -1
tol= 0.01
     
for i in range(10):
    f_val = f.evalf(subs={x: x1})
    f_deriv_val = f_deriv.evalf(subs={x: x1})
    
    x_new = float(x1 - f_val / f_deriv_val)
    
    if abs(x_new - x1) < tol:
        break
    
    x1 = x_new

print(f"La raíz es {x_new:.6f} con {i + 1} iteraciones")




