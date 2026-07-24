from inferencia.reglas import (
    calcular_peso,
    determinar_nivel,
    obtener_rasgo_dominante,
    obtener_rasgo_a_mejorar
)

from conocimiento.pregutas import PREGUNTAS


class MotorInferencia:

    def calcular_promedios(self, respuestas_usuario):

        resultados = {}

        rasgos = [
            "Apertura",
            "Responsabilidad",
            "Extroversion",
            "Amabilidad",
            "Estabilidad Emocional"
        ]

        for rasgo in rasgos:

            preguntas_rasgo = []

            for pregunta in PREGUNTAS:

                if pregunta["rasgo"] == rasgo:

                    respuesta = respuestas_usuario[pregunta["id"]]

                    peso = calcular_peso(
                        respuesta,
                        pregunta["tipo"]
                    )

                    preguntas_rasgo.append(peso)

            promedio = round(sum(preguntas_rasgo) / len(preguntas_rasgo), 2)

            resultados[rasgo] = {
                "promedio": promedio,
                "nivel": determinar_nivel(promedio)
            }

        return resultados

    def obtener_resultado_final(self, resultados):

        promedios = {}

        for rasgo in resultados:
            promedios[rasgo] = resultados[rasgo]["promedio"]

        dominante = obtener_rasgo_dominante(promedios)

        mejorar = obtener_rasgo_a_mejorar(promedios)

        return {
            "resultados": resultados,
            "dominante": dominante,
            "mejorar": mejorar
        }