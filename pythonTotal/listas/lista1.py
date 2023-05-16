#Escribe un programa que solicite al usuario 5 numeros enteros y los almacene en una lista

lista = []

for numero in range(5):
    
    numero = int(input("Digite un numero: "))
    lista.append(numero)

print(lista)