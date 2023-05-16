cadena = input("Digite una cadena: ")

cadena_original = list(cadena)
cadena_minuscula = list(cadena.lower())


if cadena_original == cadena_minuscula:
    print("Todas las letras son minusculas")
else:
    print("No todas las letras son minusculas")