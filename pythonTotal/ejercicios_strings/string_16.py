#Escriba un programa que tome un tring y lo convierta en una lista de palabras en minusculas 
#sin espacios en blanco al principio o al final

string = "    ESPACIOS EN BLANCO"

lista = string.strip()
lista = list(lista.lower())
print(lista)


