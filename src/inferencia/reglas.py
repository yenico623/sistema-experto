
def calcular_peso(respuesta, tipo):
    if tipo == "Directa":
        return respuesta

    elif tipo == "Inversa":
        return 6 - respuesta


def determinar_nivel(promedio):
    if 1.00 <= promedio <= 2.49:
        return "Bajo"

    elif 2.50 <= promedio <= 3.99:
        return "Medio"

    elif 4.00 <= promedio <= 5.00:
        return "Alto"

def obtener_rasgo_dominante(promedios):
    return max(promedios, key=promedios.get)


def obtener_rasgo_a_mejorar(promedios):
    return min(promedios, key=promedios.get)