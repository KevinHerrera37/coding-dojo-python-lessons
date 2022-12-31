#"Hello" == "Mundo" #Igual = False
#"Hello" != "Mundo" #No es igual = True
#10 > 5 #Es mayor que
#3 < 6 #Es menor que
#10 >= 8 #Mayor o igual a que = True
#10 <= 8 #Menor igual a que = False
#and - Si ambas cosas son verdaderas ejecuta
#or - Si uno de los dos es verdadero ejecuta

minombre = "Dave Franco"
edad = 35

#Condicionales 

if minombre != "Ornella":
    print(minombre)
if minombre == "Dave Franco":
    print("Este si es mi nombre")
    #if es un condicional, "si" minombre es distinto a Ornella immprime minombre=Dave Franco


if minombre != "Ornella":
    print("Mi nombre es Ornella")
    #else es un condicional, si lo anterior no se cumple imprime lo que le indiques
else:
    print(minombre)

    

print("Fin del programa")