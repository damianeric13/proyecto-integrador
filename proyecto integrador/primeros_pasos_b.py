
#FECHA     HORA  TEMP   HUM   PNM    DD    FF     NOMBRE

import json
datos_json=[]
def lector_txt():
    with open("datohorario20260825.txt", "r") as observaciones:
        for datos in observaciones:
            dato = datos.split(" ")
            datos_json.append({
                   "fecha": dato[1],
                    "hora": datos[2],
                    "temp": datos[3],
                    "humedad": datos[4],
                    "pnm": datos[5],
                    "dd": datos[6],
                    "ff": datos[7],
                    "nombre": datos[8]
                    })

def datos_json_01():
    with open ("datos/observaciones.json","w") as observaciones:
        json.dump(datos, observaciones, indent=2)
datos_json(datos_json)