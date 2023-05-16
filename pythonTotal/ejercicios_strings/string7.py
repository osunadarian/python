#Escribe un programa que tome un string y elimine todas las ocurrencias de una letra dada


cadena = input("Digite una cadena: ").lower()
letra_a_eliminar = input("Digite la letra a reemplazar: ").lower()

cadena_modificada = cadena.replace(letra_a_eliminar, "")

print(f"La cadena original era:\n\n - {cadena}.\n\nLa cadena nueva ahora es:\n\n - {cadena_modificada}")