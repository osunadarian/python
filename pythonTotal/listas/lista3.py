#Escribe un programa que solicite al usuario una lista de 5 palabras y las imprima en orden alfabetico

lista = []

for palabra in range(5):
    
    palabra = input(f"Digite la palabra {palabra}/5: ")
    lista.append(palabra)

print(f"La lista original es: {lista}.\nLa lista ordenada alfabeticamente es {lista.sort()}")


variable = lista.sort()
print(variable)