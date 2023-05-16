lista = [29, -5, -12, 17, 5, 12, 23, 16, 12, 5, -12, 17]
print(f"La lista original es: \n{lista}")

#borro numeros duplicados
lista = set(lista)
lista = list(lista)
print(f"Luego de eliminar los elementos duplicados, la lista quedo de la siguiente manera: \n{lista}")

#ordeno lista de mayor a menor
lista.sort(reverse=True)
print(f"Ahora, mostraremos la lista ordenada de mayor a mayor: \n{lista}")

#Suma de todos los numeros de la lista
print(f'La suma de todos los numeros de la lista da un total de: {sum(lista)}')

#Inserción del total a la lista
lista.insert(0, sum(lista))
print(f"Si añadimos al primer lugar [0] la suma de los numeros de la lista, queda:\n{lista}")

#Comparacion
if sum(lista[1:]) == lista[0]:
    print("La suma de todos los numeros (A excepción del primero) da como resultado el primer numero de la lista.")
else:
    print("La suma de todos los numeros (A excepción del primero) NO COINCIDE con el primer numero de la lista.")

