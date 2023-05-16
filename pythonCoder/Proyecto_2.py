# Definir un diccionario con los datos de varios alumnos, el primer dato es la edad, las listas son notas de exámenes.

alumnos = {

"Juan": (18, [7, 8, 9]),

"Maria": (20, [9, 9, 9]),

"Pedro": (19, [8, 7, 5]),

"Ana": (21, [8, 8, 7])

}

# 1. Imprimir la edad y el promedio de notas de cada alumno (usar for)
# 2. Obtener el nombre del alumno con la nota promedio más alta
# 3. Obtener una lista de los nombres de los alumnos mayores de edad
# 4. Verificar si algún alumno tiene una nota menor a 6

diccionario_alumnos = dict(alumnos)

# comprobacion tipo de dato de variable diccionario_alumnos
# print(type(diccionario_alumnos))

promedio_mas_alto = 0
alumnos_mayores = []
alumnos_nota_baja = []

for nombre, valores in diccionario_alumnos.items():

    promedio = sum(valores[1]) / len(valores[1])
    print(f"{nombre} tiene {valores[0]} años y un promedio de nota de {promedio}.")
    
    if promedio > promedio_mas_alto:
        promedio_mas_alto = promedio
        alumno_mejor_promedio = nombre

    if valores[0] >= 18:
        alumnos_mayores.append(nombre)

    for valor in valores[1]:
        if valor < 6:
            alumnos_nota_baja.append(nombre)



print(f"\n-> El alumno con promedio más alto es: {alumno_mejor_promedio} con {promedio_mas_alto}")
print('-> Los alumnos mayores de edad son', ", ".join(alumnos_mayores))







