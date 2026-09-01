datos_json=[]
import sys
import json
from validar_datos import validar_fecha, validar_hora, validar_humedad, validar_temperatura, validar_pnm, validar_dd, validar_ff, validar_estacion

datos_json = []

def lector_txt(SMN):
    datos_validos = []
    datos_invalidos = []
    with open(SMN, "r", encoding="utf-8", errors = "replace") as archivo:
#agrege un encoding para la lectura del .txt por que no podia leer
#ademas con el next se puede hacer un salto de linea lo que podria hacer con un contador.
        next(archivo)
        next(archivo)
        for linea in archivo:
# en esta parte sale un error de IndexError por las lineas vacias.
# Tenemos que agregar una condicion para los datos que estan vacios.
# ademas validaciones para los demas datos que sean correctamente leidos e impresos
#
            try:
                dato = linea.strip().split()

                nombre_estacion = " ".join(dato[7:]) # reconstrui el nombre de la estacion para que el split no "rompa" el nombre

                if  validar_fecha(dato[0]) and validar_hora(dato[1]) and validar_temperatura(dato[2]) and validar_humedad(dato[3]) and validar_pnm(dato[4]) and validar_dd(dato[5]) and validar_ff(dato[6]) and validar_estacion(nombre_estacion):
                    datos_validos.append({
                        "fecha" : dato[0],
                        "hora" : dato[1],
                        "temp" : (dato[2]),
                        "humedad" : (dato[3]),
                        "pnm" : (dato[4]),
                        "dd" : (dato[5]),
                        "ff" : (dato[6]),
                        "estacion" : nombre_estacion
                    })
                else:
                    datos_invalidos.append({
                        "linea_original" : linea.strip(),
                        "razon" : "DATO INVÁLIDO O VACÍO"
                    })
#                datos_json.append({
#                    "fecha": dato[0],
#                    "hora": dato[1],
#                    "temp": dato[2],
#                    "humedad": dato[3],
#                    "pnm": dato[4],
#                    "dd": dato[5],
#                    "ff": dato[6],
#                    "nombre": dato[7]
#                    })
            except IndexError:
                continue
        return{"validos" : datos_validos, "invalidos" : datos_invalidos}
lector_txt(sys.argv[1])

def write_txt():
#escribe el la lista con los diccionarios en un .txt 
    with open("datos/observaciones.txt", "w") as observaciones:
        for lineas in datos_json:
            observaciones.write(str(lineas)+ "\n")
write_txt()
def guardar_json():
# guarda la lista con los diccionarios en json
    with open("datos/observaciones.json", "w") as observaciones:
        json.dump(datos_json, observaciones, indent=2)
guardar_json()