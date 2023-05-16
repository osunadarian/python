#Escriba una programa que tome un string y lo convierta en un string de titulo

cadena = "esto es un titulo de pelicula"

palabras = cadena.split()

titulo = []

for palabra in palabras:
    titulo.append(palabra.capitalize())


titulo_string = " ".join(titulo)
print(titulo_string)
