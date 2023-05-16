cadena = input("Digite una cadena: ")

cadena_original = list(cadena)
cadena_mayuscula = list(cadena.upper())


if cadena_original == cadena_mayuscula:
    print("Todas las letras son mayusculas")
else:
    print("No todas las letras son mayusculas")