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


