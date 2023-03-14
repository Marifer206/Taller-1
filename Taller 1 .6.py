#punto 6
letra = input("Ingresa una letra: ")

if len(letra) != 1:
    print("Error: Por favor ingresa una única letra.")
elif letra in 'aeiouAEIOU':
    print("La letra ingresada " + str(letra) + " es una vocal.")
else:
    print("La letra ingresada " + str(letra) + " es una consonante.")
