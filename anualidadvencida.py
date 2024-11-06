a = int(input())
p = int(input())
n = int(input())

vr = a/p
x = float((input()))/100
xin = x
xp = 0
rangotolsup= 0.0003
rangotolinf= 0

for i in range(10):
    xin = x
    va = ((((1 + x )**n) - 1) / x )
    x +=0.0001
    print(va)
    if va <= vr and va <= rangotolinf:
        x = xin
    elif va >= vr and va >= rangotolsup:
        x = xin
        xip = xp
        xp = x
    elif va >= vr and va >= rangotolinf:
        x +=    0.0001
    elif va >= vr and va >= rangotolinf:
        x -= 0.0001
        
print("el interes aproximado de la anualidad es: " , 100*x, "%")