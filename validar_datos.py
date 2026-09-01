def validar_fecha(fecha):
    fecha = fecha.strip()
    if len(fecha) != 8:
        return False

    dia_texto = fecha[0:2]
    mes_texto = fecha[2:4]
    anio_texto = fecha[4:8]

    if not (dia_texto.isdigit() and mes_texto.isdigit() and anio_texto.isdigit()):
        return False

    dia = int(dia_texto)
    mes = int(mes_texto)
    anio = int(anio_texto)

    if mes < 1 or mes > 12 or anio < 1:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

def validar_hora(hora):
    if hora.isnumeric():
        hora_entera = int(hora)
        if hora_entera < 0 or hora_entera > 23:
            return False
        return True
    return False

def numeros_validos(valor, valor_minimo, valor_maximo):
    try:
        numero = float(valor)
        if valor_minimo <= numero <= valor_maximo:
            return True
        return False
    except ValueError:
        return False

def validar_temperatura(temperatura):
    return numeros_validos(temperatura, -10, 40)

def validar_humedad(humedad):
    return numeros_validos(humedad, 0, 100)

def validar_pnm(presion):
    return numeros_validos(presion, 900, 1040)

def validar_dd(direccion):
    return numeros_validos(direccion, 0, 360)

def validar_ff(velocidad):
    return numeros_validos(velocidad, 0, 200)

def validar_estacion(nombre):
    return len(nombre.strip()) > 0