datos_json=[]
import sys
import json
datos_json = []

def lector_txt(SMN):
    with open(SMN, "r", encoding="utf-8", errors="replace") as archivo:
#agrege un encoding para la lectura del .txt por que no podia leer
#ademas con el next se puede hacer un salto de linea lo que podria hacer con un contador.

        next(archivo)
        next(archivo)
        for linea in archivo:
            dato = linea.strip().split()
# en esta parte sale un error de IndexError por las lineas vacias.
# Tenemos que agregar una condicion para los datos que estan vacios.
# ademas validaciones para los demas datos que sean correctamente leidos e impresos
#
            try:
                datos_json.append({
                    "fecha": dato[0],
                    "hora": dato[1],
                    "temp": dato[2],
                    "humedad": dato[3],
                    "pnm": dato[4],
                    "dd": dato[5],
                    "ff": dato[6],
                    "nombre": dato[7]
                    })
            except IndexError:
                continue
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