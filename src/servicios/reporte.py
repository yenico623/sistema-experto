from conocimiento.perfiles import PERFILES
from conocimiento.recomendaciones import RECOMENDACIONES


class Reporte:

    def obtener_perfil(self, rasgo, nivel):

        for perfil in PERFILES:
            if perfil["rasgo"] == rasgo and perfil["nivel"] == nivel:
                return perfil

        return None

    def obtener_recomendacion(self, rasgo, nivel):

        for recomendacion in RECOMENDACIONES:
            if (
                recomendacion["rasgo"] == rasgo
                and recomendacion["nivel"] == nivel
            ):
                return recomendacion

        return None

    def generar_reporte(self, resultado):

        resultados = resultado["resultados"]

        rasgo_dominante = resultado["dominante"]
        rasgo_mejorar = resultado["mejorar"]

        nivel_dominante = resultados[rasgo_dominante]["nivel"]
        nivel_mejorar = resultados[rasgo_mejorar]["nivel"]

        perfil = self.obtener_perfil(
            rasgo_dominante,
            nivel_dominante
        )

        recomendacion_dominante = self.obtener_recomendacion(
            rasgo_dominante,
            nivel_dominante
        )

        recomendacion_mejorar = self.obtener_recomendacion(
            rasgo_mejorar,
            nivel_mejorar
        )

        if rasgo_dominante == rasgo_mejorar:
            recomendacion_mejorar = None

        print("\n" + "=" * 60)
        print("        SISTEMA EXPERTO - PERFIL DE PERSONALIDAD")
        print("=" * 60)

        print("\nPERFIL OBTENIDO\n")

        print(f"Rasgo dominante : {rasgo_dominante}")
        print(f"Nivel           : {nivel_dominante}")
        print(f"Perfil          : {perfil['perfil']}")

        print("\nDescripción:")
        print(perfil["descripcion"])

        print("\n" + "-" * 60)
        print("\nFORTALEZA PRINCIPAL\n")

        print(recomendacion_dominante["recomendacion"])

        print("\n" + "-" * 60)
        print("\nASPECTO A MEJORAR\n")

        if recomendacion_mejorar is None:
            print("No se identificó un rasgo significativamente inferior.")
            print("El perfil obtenido es equilibrado entre todos los rasgos.")
        else:
            print(f"Rasgo : {rasgo_mejorar}")
            print(f"Nivel : {nivel_mejorar}")

            print("\nRecomendación:")
            print(recomendacion_mejorar["recomendacion"])

        print("\n" + "=" * 60)

        return {
            "resultados": resultados,
            "perfil": perfil,
            "recomendacion_dominante": recomendacion_dominante,
            "recomendacion_mejorar": recomendacion_mejorar
        }