#Escribe un programa que tome un string y reemplace todas las ocurrencias de una letra dada con otra letra

cadena = input("Digite una cadena: ").lower()
letra_a_buscar = input("Digite la letra a reemplazar: ").lower()
letra_a_reemplazar = input("Digite la letra a reemplazar: ")

cadena_modificada = cadena.replace(letra_a_buscar, letra_a_reemplazar)

print(f"La cadena original era:\n\n - {cadena}.\n\nLa cadena nueva ahora es:\n\n - {cadena_modificada}")