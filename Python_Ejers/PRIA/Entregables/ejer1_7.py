import math

print("Introduce los cocientes(A,B,C) deseasdos para una ecuación de segundo grado separados por comas: ")
print("(Ax²+Bx+C=0)")

try:
    a,b,c=input().split(",")
    a,b,c=int(a),int(b),int(c)

except:
    print("Valores no validos")
    exit()

discriminante=b**2-4*a*c
if discriminante < 0:
    print("La ecuación introducida no tiene soluciones reales")
    exit()

x1=(b+math.sqrt(discriminante))/(2*a)
x2=(b-math.sqrt(discriminante))/(2*a)

print("x1:",round(x1,2),"\nx2:",round(x2,2))