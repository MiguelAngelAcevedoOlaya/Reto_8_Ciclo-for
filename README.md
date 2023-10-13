# RETO # 8 PROGRAMACIÓN

### PUNTO 1

#### Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

Para este codigo utlice las condiciones de range y ciclo for en el que en un rango de [a,b,1) y de en uno en uno. para luego en el print pedirle que me imprima i con su cuadrado con el siguiente texto: i " y su cuadrado es " i**2

```
for i in range(1, 101, 1): 
  print(str(i)+ " y su cuadrado es " +str(i**2))
```

### PUNTO 2

#### Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

Utilice el mismo metodo que en el codigo anterior pero cambiando que i en vez de subir de uno en uno subira de dos en dos, en un rango de 2 hasta 1000, de esta manera en el print se solicitara el numero i que seran todos los pares.

Luego pondre otro codigo igual al enterior, cambiando el rando desde 1 hasta 1000, de esta manera al imprimir los i, seran todos los números imapres.

```
for i in range(2, 1000, 2): 
  print(i, "Es par")
print("Hasta aqui van los pares")
for i in range(1, 1000, 1): 
  print(i, "Es impar")
print("Hasta aqui van los impares")
```

### PUNTO 3

#### Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

En este punto le pedi al usuario que ingrese un número aleatorio natural, luego estableci un codigo if en el que si el residuo al dividir el número entre dos es 0 , osea es par establezca un codigo for con rango que disminuya de dos en dos hasta que el numero sea igual a 2, y me imprima la variable. La impresión sera la lista de todos los números pares incluido el numero, de forma descendete hasta dos.

En caso de que el residuo no sea 0, primero le restare uno al numero natural, para que sea par, y establecer un codigo for con rango que lo reduzca de 2 en 2 hasta que sea igual a 2 y me imprima la variable, en este caso me imprimira todos los numeros pares menores al numero impreso, de forma descendete hasta 2.

```
numero = int(input("Ingrese el numero natural que desees: "))
if numero % 2 == 0:
  print("Los pares menores o iguales a " +str(numero)+ " son:")
  for numero in range(numero, 1 ,-2):
    print(numero)
else:
  numero = numero - 1
  print("Los pares menores o iguales a " +str(numero + 1)+ " son:")
  for numero in range(numero, 1 ,-2):
    print(numero)  
```

### PUNTO 4

#### Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

En primer lugar le solicite al usuario que ingresa el número natural que deseara, estableci la variable inicio como entero igual a 1, y la variable fact como entero igual a 1, estableci un codigo for en el que mientras inicio sea mayor o igual a 1 hasta que sea igual al numero ingresado por el usuario, establezca otro codigo for en el que mientras i sea mayor a 1 hasta que sea igual a la variable inicio + 1, multiplique factorial por i. Luego de cerrar el ciclo for de adentro imprima el numero y su factorial y luego reinicie la variable factorial a 1.

Esto establece un codigo que para cada número saque su número factorial hasta que el codigo sea igual al numero que ingreso el usuario, por lo que necestairemos dos ciclos for, uno que sea el de todos los números que necesitamos, y el otro que determine el factorial del número. Y al terminar el segun ciclo reinicie la variable factorial a 1 para que no quede guardado el dato del anterior número.

```
numero = int(input("Ingrese un numero natural: "))
inicio : int = 1
fact : int = 1
for inicio in range(1, numero + 1,1):
  for i in range(1, inicio +1):
    fact = fact*i
  print("Fatorial de " +str(inicio)+ " es " +str(fact))
  fact = 1
```

### PUNTO 5

#### Calcular el valor de 2 elevado a la potencia n usando ciclos for

Para este punto establezco la variable num_c como entero igual a 2 que sera la base de la potencia, luego le pido al usuario que ingresa la potencia a la que desea elevar dos, ademas una variable extra que sera igual a 2, esta la usaremos como variable auxiliar para el ciclo. Establecemos el ciclo for en el que mientras una variable i este entre 1 y la potencia, la variable num_c sera igual a ella misma multiplicada por la variable auxiliar. Entonces esto permitira que si la potencia sea muy grande, la variable num_c subira de manera exponencial con factor 2 y se multiplique por la variable auxuliar que siempre sera igual a 2. Imitando la función de la potencia.
```
num_c : int = 2
potencia = int(input("Ingresa el número que desees: "))
numero : int = 2
for i in range(1, potencia, 1):
  num_c = num_c *numero
print("2 elevado a la potencia " +str(potencia)+ " es igual a " +str(num_c))
```
### PUNTO 6

#### Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

Para este punto le pedi al usuario que ingresa dos valores, uno real que seria la base, y otro entero, que seria el exponente, usamos una tercera variable que sera igual a la variable del número real. Utilizamos el codigo for, con las mismas caracterisitcas que usamos en el punto 5, solo que cambiamos el 2, que era una constante, por una variable de libre elección para el usuario

```
numero_b = float(input("Ingresa un número real: "))
numero_a = int(input("Ingresa un número natural: "))
b = numero_b
for i in range(1,numero_a):
  numero_b = numero_b * b
print("El numero " +str(b)+" elevado a la potencia " +str(numero_a)+ " es : " +str(numero_b))  
```

### PUNTO 7

#### Diseñe un programa que muestre las tablas de multiplicar del 1 al 9

Se establece un ciclo for de los numeros de uno a diez, en el que para cada número se establezca otro for, tambien de 1 a 10, que multiplique el número del primer ciclo por el del segundo y asi hasta terminar el ciclo 2, en el que la variable multipliación = num(ciclo1) * f(ciclo2) e imprima el siguiente texto "str(num)+ " x " +str(f)+ " = " +str(multiplicacion)"
Esto dara que para cada número del ciclo 1, imprima su tabla de multiplicar (gracias al ciclo 2)

```
for num in range(1,11):
  for f in range(1,11):
    multiplicacion = num * f 
    print(str(num)+ " x " +str(f)+ " = " +str(multiplicacion))
  print("Fin de la tabla")
```

### PUNTO 8

#### Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

Para este punto importamos expoencial y factorial de la libreria math, establecimos la función con la variable numero como flotante y n como entero. Una variable dentro de la función llamada suma = 0, que usaremos para el ciclo for, minetras la variable i este entre 0 y (n +1)  usamos la serie de Maclaurin que se ira sumando porgresivamente a la variable suma hasta que deje de cumplirse el ciclo.

Luego le damos valor a las variables necesarias, y sacamos el valor real al elevar el número a cierto exponente, y establecimos un ciclo while que determine cuando el margen de error es inferior al 0.1%, ese sera el nuevo valor de n que utliziremos, corriendo nuevamente la función, dandonos el valor aproximado y el real.

```
from math import exp, factorial

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((numero**i)/(factorial(i)))
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_exp(numero, n)
  v_real : float = exp(numero)

while((abs(v_real - aprx)/v_real * 100)>0.1):
  aprx: float = aprox_exp(numero, n)
  n += 1
print("Para que el margen de error sea menor a 0.1  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```

### PUNTO 9

#### Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

Para este punto importamos seno y factorial de la libreria math, establecimos la función con la variable numero como flotante y n como entero. Una variable dentro de la función llamada suma = 0, que usaremos para el ciclo for, minetras la variable i este entre 0 y (n +1)  usamos la serie de Maclaurin que se ira sumando porgresivamente a la variable suma hasta que deje de cumplirse el ciclo.

Luego le damos valor a las variables necesarias, y sacamos el valor real del numero en la función seno , y establecimos un ciclo while que determine cuando el margen de error es inferior al 0.1%, ese sera el nuevo valor de n que utliziremos, corriendo nuevamente la función, dandonos el valor aproximado y el real.

```
from math import sin, factorial

def aprox_sin(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = (((-1)**i)*((numero**(2*i+1))/(factorial(2*i+1))))
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_sin(numero, n)
  v_real : float = sin(numero)

while((abs(v_real - aprx)/v_real * 100)>0.1):
  aprx: float = aprox_sin(numero, n)
  n += 1
print("Para que el margen de error sea menor a 0.1  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```

### PUNTO 10

#### Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```
from math import factorial
from numpy import arctan

def aprox_arctg(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = (((-1)**i)*((numero**(2*i+1))/(2*i+1)))
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_arctg(numero, n)
  v_real : float = arctan(numero)

while((abs(v_real - aprx)/v_real * 100)>0.1):
  aprx: float = aprox_arctg(numero, n)
  n += 1
print("Para que el margen de error sea menor a 0.1  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```
