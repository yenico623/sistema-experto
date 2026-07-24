from conocimiento.pregutas import PREGUNTAS


class Cuestionario:

    def realizar_cuestionario(self):

        respuestas = {}

        print("\n===================================")
        print(" CUESTIONARIO DE PERSONALIDAD")
        print("===================================")
        print("Responda cada pregunta con un número del 1 al 5.\n")
        print("1 = Totalmente en desacuerdo")
        print("2 = En desacuerdo")
        print("3 = Ni de acuerdo ni en desacuerdo")
        print("4 = De acuerdo")
        print("5 = Totalmente de acuerdo\n")

        for pregunta in PREGUNTAS:

            while True:

                try:

                    print(f"{pregunta['id']} - {pregunta['pregunta']}")

                    respuesta = int(input("Respuesta: "))

                    if respuesta >= 1 and respuesta <= 5:

                        respuestas[pregunta["id"]] = respuesta
                        print()
                        break

                    else:
                        print("Debe ingresar un número entre 1 y 5.\n")

                except ValueError:

                    print("Ingrese únicamente números del 1 al 5.\n")

        return respuestas