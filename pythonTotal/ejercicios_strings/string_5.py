#Escribe un programa que tome un string y cuente cuantas veces aparece una subcadena dada

cadena = input("Digite una cadena: ")

palabra_buscada = input("Digite una palabra para ver cuantas ocurrencias tiene en el texto: ").lower()

contador = cadena.lower().count(palabra_buscada)

if contador == 1:
    print(f"La palabra '{palabra_buscada}' aparece {contador} vez.")
else:
    print(f"La palabra '{palabra_buscada}' aparece {contador} veces.")
