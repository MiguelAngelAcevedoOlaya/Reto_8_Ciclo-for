# -*- coding: utf-8 -*-
"""reto_8_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lQIaDQSQRYih7nLL_IPeUYKmaMefywuw
"""

numero = int(input("Ingrese el numero que desees: "))
if numero % 2 == 0:
  print("Los pares menores o iguales a " +str(numero)+ " son:")
  for numero in range(numero, 1 ,-2):
    print(numero)
else:
  numero = numero - 1
  print("Los pares menores o iguales a " +str(numero + 1)+ " son:")
  for numero in range(numero, 1 ,-2):
    print(numero)