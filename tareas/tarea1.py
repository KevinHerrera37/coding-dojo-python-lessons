"""Escribir un programa que pregunte al usuario su edad
 y muestre por pantalla todos los años que ha cumplido
  (desde 1 hasta su edad)."""

def print_age():
    age=int(input("¿Cual es tu edad?  "))
    for n in range(1,age+1):
        print(n)

print_age()