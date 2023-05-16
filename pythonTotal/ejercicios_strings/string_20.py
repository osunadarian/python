#Escribe un programa que tome un string y lo convierta en un string de tipo CamelCase

cadena = "nombre de variable roja"

lista = []

for palabra in cadena.split(" "):

    lista.append(palabra.capitalize())


variableCamelCase = "".join(lista)

