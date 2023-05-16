#Escribe un programa que solicite al usuario una lista de 10 numeros enteros y determine cual es el numero
#mas grande de la lista

lista = []

for numero in range(10):
    
    numero = int(input(f"Digite el numero {numero}/10: "))
    lista.append(numero)

flag = False

for n in lista:

    if flag == False:
        mayor = n
        flag = True
    else:
        if n > mayor:
            mayor = n

print(f"El numero mayor de la lista {lista} es {mayor}.")