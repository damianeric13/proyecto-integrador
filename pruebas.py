datos_json=[]
import sys
import json
datos_json = []

def lector_txt(SMN):
    with open(SMN, "r", encoding="utf-8", errors="replace") as archivo:

        next(archivo)
        next(archivo)
        for linea in archivo:
            dato = linea.strip().split()
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
            print()
lector_txt(sys.argv[1])
def guardar_json():
    with open("datos/observaciones.json", "w") as observaciones:
        json.dump(datos_json, observaciones, indent=2)
guardar_json()
#print(datos_json)
#def lector_txt():

#    with open('datohorario20260825.txt', 'r', encoding='utf-8', errors='replace') as archivo:
#       for linea in archivo:
#            dato = linea.strip().split()
#            print(dato)
#            return

#lector_txt()
#def lector_txt():
#    with open('datohorario20260825.txt', 'r', encoding='utf-8', errors='replace') as archivo:
 #       for linea in archivo:
  #          dato = linea.split(" ")
   #         dato = linea.strip(" ").strip("\n")
    #        return datos_json.append(dato)
#lector_txt()
            
      #  contenido = archivo.read()
        #contenido.split()
       # return datos_json.append(contenido)


