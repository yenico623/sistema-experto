from servicios.cuestionario import Cuestionario
from inferencia.motor import MotorInferencia
from servicios.reporte import Reporte


def main():

    cuestionario = Cuestionario()
    motor = MotorInferencia()
    reporte = Reporte()

    respuestas = cuestionario.realizar_cuestionario()

    resultados = motor.calcular_promedios(respuestas)

    resultado_final = motor.obtener_resultado_final(resultados)

    reporte.generar_reporte(resultado_final)


if __name__ == "__main__":
    main()