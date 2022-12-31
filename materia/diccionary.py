diccionario =  {"Name":"Pedro", "Apellido":"Perez", "Dirección":"Santiago"}

#update añade un indice más al diccionario

diccionario.update({"Tlf":"+569333333"})

#values solamente trae los valores del diccionario, es necesario hacerlo en otra variable.

test = diccionario.values()

#pop borra un indice y los valores

diccionario.pop("Name")

print(diccionario)

print(test)

#set cambia el orden de los valores

seteo = {"a","b","c","d"}

#add añade un valor a set

seteo.add("f")

print(seteo)

