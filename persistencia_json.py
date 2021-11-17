#       1. crear un módulo (python file) nuevo llamado persistencia_json
#       2. en ese módulo crear una función que se llame "store" que acepta por "ventana" dos "argumentos":
#           1. una variable cualquiera
#           2. el nombre de un archivo
#           la funcion debe almacenar el contenido de la variable en el archivo usando json
#       3. en ese mismo modulo crear otra funcion que se llame "retrieve" que acepta por ventana el nombre de un archivo y devuelve el contenido
#       4. en el modulo "main", "importar" el módulo "persistencia_json" y usar las funciones definidas escribir en disco y leer del disco la lista de diccionarios como datos
#          de los coches
import json

def store(variable, nombrearchivo):
    variable = input(print("introduce la varibale cualquiera: "))
    nombrearchivo = input(print("introduce el nombre del archivo: "))
    json.dump(json.dumps(nombrearchivo), open(nombrearchivo, "w"))
def retrieve(nombrearchivo):
    return json.load
