#Escriba un programa que tome un tring y lo convierta en una lista de palabras en mayusculas 
#sin espacios en blanco al principio o al final

string = "    espacios en blanco     "

lista = string.strip()
lista = list(lista.upper())
print(lista)