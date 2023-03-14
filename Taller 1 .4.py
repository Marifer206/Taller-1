#punto 4

i : float
s : float
#El número mayor a evaluar debe ser el primero que se ingrese.

i = float(input("Ingrese el primer número: "))
s = float(input("Ingrese el segundo número: "))
if i % s == 0:
    print("El número " + str(i) + " es multiplo de " + str(s) )
else:
    print("El número " + str(i) + " no es multiplo de " + str(s) )