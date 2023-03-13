# Taller-1
## Desarrollo de taller #1;  Daniel Alejandro Archila Gómez {Programación de computadores}



***1. Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien)***




[![Quiz-python.png](https://i.postimg.cc/Bv0wDTw3/Quiz-python.png)](https://postimg.cc/rDfJ2rkZ)


***2.Realice un programa que lea tres números reales y determine cuál es el mayor.***

```ruby
a : float
b : float
c : float

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
if a > b and a > c:
    print("El primer número " + str(a) + "  es el mayor ")
elif b > a and b > c:
    print("El segundo número " + str(b) + " número es el mayor ")
else:
    print("El tercer número " + str(c) + " número es el mayor ")

```





[![Taller-1.png](https://i.postimg.cc/wT2y5gBG/Taller-1.png)](https://postimg.cc/GHBmd0GF)





***3.Realice un programa que lea un número enteros y determine si es par o impar.***


```ruby
n : int
n = int(input("Ingrese el número "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")
 ```
 
 
 
 
 [![Taller-11.png](https://i.postimg.cc/CKV3FTGw/Taller-11.png)](https://postimg.cc/sMw6cLHL)
 
 
 
***4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.***




```ruby
i : float
s : float
#El número mayor a evaluar debe ser el primero que se ingrese.

i = float(input("Ingrese el primer número"))
s = float(input("Ingrese el segundo número"))
if i % s == 0:
    print("El número " + str(i) + " es multiplo de " + str(s) )
else:
    print("El número " + str(i) + " no es multiplo de " + str(s) )
```




[![taller-13.png](https://i.postimg.cc/Rhnd6qmy/taller-13.png)](https://postimg.cc/rRMx7VKN)






***5.Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.***

```ruby
a : float
b : float
c : float

a = float(input(" Ingrese el primer número: "))
b = float(input(" Ingrese el segundo número: "))
c = float(input(" Ingrese el tercer número: "))

if a + b > c:
    print("La suma de " + str(a) + " y " + str(b) + " es mayor que "+ str(c))

elif a + b < c:
    print("La suma de " + str(a) + " y " + str(b) + " es menor que "+ str(c))
else: 
    if a + b == c:
        print("La suma de " + str(a) + " y " + str(b) + " es igual que "+ str(c))
 ```




[![taller-15.png](https://i.postimg.cc/Kjn9p4WL/taller-15.png)](https://postimg.cc/CnxHzMSL)






***6.Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.***




```ruby
letra = input("Ingresa una letra: ")

if len(letra) != 1:
    print("Error: Por favor ingresa una única letra.")
elif letra in 'aeiouAEIOU':
    print("La letra ingresada " + str(letra) + " es una vocal.")
else:
    print("La letra ingresada " + str(letra) + " es una consonante.")

```



[![taller-16.png](https://i.postimg.cc/CKwVGBc3/taller-16.png)](https://postimg.cc/Bj7ys69p)







***7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:***

°El promedio

°La mediana

°El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

°Ordenar los números de forma ascendente

°Ordenar los números de forma descendente

°La potencia del mayor número elevado al menor número

°La raíz cúbica del menor número






```ruby
# Solicitar los 5 números al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
d = float(input("Ingrese el cuarto número: "))
e = float(input("Ingrese el quinto número: "))

# Calcular el promedio
promedio = (a + b + c + d + e) / 5

# Calcular la mediana
lista_numeros = [a, b, c , d , e]
lista_numeros.sort()
if len(lista_numeros) % 2 == 0:
    mediana = (lista_numeros[len(lista_numeros)//2] + lista_numeros[len(lista_numeros)//2 - 1]) / 2
else:
    mediana = lista_numeros[len(lista_numeros)//2]

# Calcular el promedio multiplicativo
producto = a * b * c * d * e
promedio_multiplicativo = producto ** (1/5)

# Ordenar los números de forma ascendente
ascendente = sorted(lista_numeros)

# Ordenar los números de forma descendente
descendente = sorted(lista_numeros, reverse=True)

# Calcular la potencia del mayor número elevado al menor número
mayor = max(lista_numeros)
menor = min(lista_numeros)
potencia = mayor ** menor

# Calcular la raíz cúbica del menor número
raiz_cubica = abs(min(lista_numeros)) ** (1/3)

# Imprimir los resultados
print(f"El promedio de los números es: {promedio}")
print(f"La mediana de los números es: {mediana}")
print(f"El promedio multiplicativo de los números es: {promedio_multiplicativo}")
print(f"Los números ordenados de forma ascendente son: {ascendente}")
print(f"Los números ordenados de forma descendente son: {descendente}")
print(f"La potencia del mayor número ({mayor}) elevado al menor número ({menor}) es: {potencia}")
print(f"La raíz cúbica del menor número ({min(lista_numeros)}) es: {raiz_cubica}")
```



***8.Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.***

```ruby
s : float
s = float(input(" Insertar la frecuencia deseada: ")) 

if s < 3e9:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de radio" )
elif s < 3e12:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de microondas" )
elif s  < 4.3e14:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de infrrarrojo" )
elif s < 7.5e14:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de luz visible" )

elif s < 3e17:
    print("La frecuencia " + str(s) + " esta ubicada en ondas ultravioletas" )

elif s < 3e19:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de Rayos X" )
        
else:
    print("La frecuencia " + str(s) + " esta ubicada en ondas de rayos gamma" )
```



***9.Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.***




```ruby
a = (input("Inserte el nombre del pais en minuscula"))

if a == "argentina":
    print("La capital de " + str(a) + " es Buenos Aires" )
elif a == "bolivia":
    print("La capital de " + str(a) + " La Paz" )
elif a == "brasil":
    print("La capital de " + str(a) + " es Brasilia" )
elif a == "canada":
    print("La capital de " + str(a) + " es Ottawa" )
elif a == "chile":
    print("La capital de " + str(a) + " es Santiago de Chile" )
elif a == "colombia":
    print("La capital de " + str(a) + " es Bogotá" )
elif a == "costa rica":
    print("La capital de " + str(a) + " es San José" )
elif a == "cuba":
    print("La capital de " + str(a) + " es La Habana" )
elif a == "ecuador":
    print("La capital de " + str(a) + " Quito" )
elif a == "estados unidos" or a == "eeuu":
    print("La capital de " + str(a) + " es Washington" )
elif a == "guatemala":
    print("La capital de " + str(a) + " es Ciudad de Guatemala  " )
elif a == "honduras":
    print("La capital de " + str(a) + " es Tegucigalpa" )
elif a == "mexico":
    print("La capital de " + str(a) + " es Ciudad de México" )
elif a == "nicaragua":
    print("La capital de " + str(a) + " es Managua" )
elif a == "panama":
    print("La capital de " + str(a) + " es Ciudad de Panamá" )
elif a == "paraguay":
    print("La capital de " + str(a) + " es Asunción" )
elif a == "peru":
    print("La capital de " + str(a) + " es Lima" )
elif a == "puerto rico":
    print("La capital de " + str(a) + " es San Juan  " )
elif a == "república dominicana":
    print("La capital de " + str(a) + " es Santo Domingo" )
elif a == "uruguay":
    print("La capital de " + str(a) + " es Montevideo" )
elif a == "venezuela":
    print("La capital de " + str(a) + " es Caracas " )
else:
    print("País no identificado")
```





***10.Escriba un programa que dada una distancia calcule***
°El tiempo que le tomaría a la luz recorrer la distancia.

°El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.

°El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.

°El tiempo que le tomaría a Bolt recorrer la distancia.
