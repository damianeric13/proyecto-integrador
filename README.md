Grupo:
+Dinamite

Participantes:
+Cossy Ashlee Avril
+De La Guarda Damian

Informacion del proyecto:
el proyecto consta de varias partes la primera a partir de un .txt del servicio meteorologico tenemos que pasarlo a un .json, en esta parte del codigo crudo esperamos una salida de tipo diccionario en json, ademas de la organizacion de del .txt tenga una organizacion tipo dicionario dando los valores establecidos en el trabajo practico, con  las validaciones de FECHA,HORA,TEMP,HUM,PNM,DD,FF,NOMBRE, hasta los posibles datos invalidos que contenga el informe meteorologico

esperamos que la salida de jason sea algo similar a:
nombre_de_la_ciudad(NOMBRE):{
        datos_validos:[{
                "FECHA":
                "HORA":
                "TEMP":
                "HUM":
                "PNM":
                "DD":   
                "FF":}
                {
                "FECHA":
                "HORA":
                "TEMP":
                "HUM":
                "PNM":
                "DD":   
                "FF":}
                ]
        datos invalidos:en caso de un dato un invalido aparezca aca con su nombre(NOMBRE):["HORA":{    
                "TEMP": "veinticincogrados"
}]
esto seria la vista del .json esperada con todos los nombres de las ciudades y sus distintos tipos de datos y horarios cada ciudad tendria que tener hay que tener en cuenta que cada ciudad tiene varios registros en diferentes horarios.
