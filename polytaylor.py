import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import sympy as sp
plt.style.use("bmh")

x = np.linspace( -np.pi , np.pi , 200)
y = np.zeros(len(x))



funcion = sp.sympify(input("introduzca la funcion en terminos de x: "))

xsym = sp.symbols('x')


ya = [funcion.evalf(subs={xsym: val}) for val in x]

labels = ["Primer grado" , "Tercer grado",
          "Quinto grado" , "Septimo grado",]

plt.figure(figsize = (10,8))


for n, label in zip(range(5), labels):
    y=y+((-1)**n*(x)**(2*n+1))/scipy.special.factorial(2*n+1)
    print(n)
    
    plt.plot(x,y, label = label)

plt.plot(x, ya, "k", label = "Funcion original")


plt.grid()
plt.title("Aproximacion de las series de taylor de orden superior")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()