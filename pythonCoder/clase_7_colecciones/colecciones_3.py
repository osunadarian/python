# Definir el diccionario con las divisas y sus símbolos
divisas = {'Dolar': '$', 'Euro': '€', 'Libra': '£'}

# Solicitar al usuario que ingrese la divisa que desea visualizar
divisa = input('Ingrese la divisa que desea visualizar: ')

# Verificar si la divisa existe en el diccionario
if divisa in divisas:
    # Si la divisa existe, imprimir su símbolo
    print('El símbolo de', divisa, 'es', divisas[divisa])
else:
    # Si la divisa no existe, imprimir un mensaje de error
    print('La divisa', divisa, 'no se encuentra en la lista de divisas.')