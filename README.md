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
    print("El segundo " + str(b) + " número es el mayor ")
else:
    print("El tercer " + str(c) + " número es el mayor ")
```






***3.Realice un programa que lea un número enteros y determine si es par o impar.***


```ruby
n : int
n = int(input("Ingrese el número "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")
 ```
 
 
 
 
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



***5.Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.


