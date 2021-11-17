#   Modificar el proyecto del ejercicio de clase 8, realizando lo siguiente:
#       1. crear un módulo (python file) nuevo llamado persistencia_json
#       2. en ese módulo crear una función que se llame "store" que acepta por "ventana" dos "argumentos":
#           1. una variable cualquiera
#           2. el nombre de un archivo
#           la funcion debe almacenar el contenido de la variable en el archivo usando json
#       3. en ese mismo modulo crear otra funcion que se llame "retrieve" que acepta por ventana el nombre de un archivo y devuelve el contenido
#       4. en el modulo "main", "importar" el módulo "persistencia_json" y usar las funciones definidas escribir en disco y leer del disco la lista de diccionarios como datos
#          de los coches

import json

lista_coche = []
while True:
    marcacoche = input("marca coche: ")
    if marcacoche == "fin":
        break
    modelo = input("modelo: ")
    combustible = input("tipo combustible: ")
    cilindrada = input("cilindrada: ")
    linea= {}
    linea["marca coche: "] = marcacoche
    linea["modelo: "] = modelo
    linea["combustible: "] = combustible
    linea["cilindrada: "] = cilindrada
    lista_coche.append(linea)
print("Lista coche:\n", lista_coche)

json.dump(json.dumps(lista_coche), open("coches.txt", "w"))

lista_coches = []