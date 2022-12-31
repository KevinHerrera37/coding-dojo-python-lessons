"""Escriba un programa que pregunte tu nombre
si tu nombre es Ornella imprima "mi nombre es Ornella"
si no que imprima mi nombre es el nombre que sea """

myname = (input("¿Cúal es tu nombre?: "))

if myname == "Ornella":
    print("Mi nombre es Ornella")
else:
    print(f'Mi nombre es {myname}')
    
"""Escriba un programa que pregunte mi edad
si tu edad es mayor a 20 imprima "Soy un viejo"
si es menor a 20 imprima "Soy pequeño"""
    
myage = int(input("¿Cúal es tu edad?:"))

if myage > 20:
    print("Soy un viejo")
else:
    print("Soy un peque:p")
    