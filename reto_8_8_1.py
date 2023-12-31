# -*- coding: utf-8 -*-
"""reto_8_8_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bfVChSzKqHZvBI2tZRkpPzwU1NzpLVup
"""

from math import exp, factorial

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((numero**i)/(factorial(i)))
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 10
  aprx: float = aprox_exp(numero, n)
  v_real : float = exp(numero)
  vabs : float = (abs(v_real - aprx)/v_real * 100)
  print("Aproximación :" +str(aprx))
  print("El valor real es " +str(v_real))
  print("Margen de error " +str(vabs)+ "%")