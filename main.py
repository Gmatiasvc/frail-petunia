import datetime
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Vanity_Color:
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    cyan = "\033[36m"
    white = "\033[37m"


class Comida:
    """Representa una comida registrada, con su tipo y calorías."""

    def __init__(self, tipo, calorias):
        self.tipo = tipo
        self.calorias = calorias


class ActividadFisica:
    """Representa una actividad física, con su tipo, duración y calorías quemadas."""

    def __init__(self, tipo_ejercicio, duracion_minutos, calorias_quemadas):
        self.tipo_ejercicio = tipo_ejercicio
        self.duracion_minutos = duracion_minutos
        self.calorias_quemadas = calorias_quemadas


class Pasos:
    """Representa los pasos caminados en un momento dado."""

    def __init__(self, cantidad_pasos):
        self.cantidad_pasos = cantidad_pasos


class Sueno:
    """Representa el registro de sueño, con horas y calidad subjetiva."""

    def __init__(self, horas_sueno, calidad_subjetiva):
        self.horas_sueno = horas_sueno
        self.calidad_subjetiva = calidad_subjetiva


class Agua:
    """Representa la cantidad de agua consumida."""

    def __init__(self, mililitros):
        self.mililitros = mililitros


class NutriFitLog:
    """
    Sistema integral de registro diario de salud personal.
    Permite registrar comidas, actividad física, pasos, sueño y consumo de agua.
    Genera un resumen diario con cálculos automáticos.
    """

    def __init__(self):
        self.registros_diarios = {
            "comidas": [],
            "actividad_fisica": [],
            "pasos": [],
            "sueno": [],
            "agua": [],
        }
        self.fecha_actual = datetime.date.today()

    def registrar_comida(self):
        """Permite al usuario registrar una comida."""
        print("\n--- Registrar Comida ---")
        tipo = input("Tipo de comida (desayuno, almuerzo, cena, snack): ").lower()
        while tipo not in ["desayuno", "almuerzo", "cena", "snack"]:
            print(
                "Tipo de comida inválido. Por favor, elige entre desayuno, almuerzo, cena o snack."
            )
            tipo = input("Tipo de comida (desayuno, almuerzo, cena, snack): ").lower()

        while True:
            try:
                calorias = float(input("Calorías ingeridas: "))
                if calorias < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número positivo para las calorías."
                )

        self.registros_diarios["comidas"].append(Comida(tipo, calorias))
        print("Comida registrada exitosamente.")

    def registrar_actividad_fisica(self):
        """Permite al usuario registrar una actividad física."""
        print("\n--- Registrar Actividad Física ---")
        tipo_ejercicio = input("Tipo de ejercicio (ej. correr, nadar, pesas): ")
        while True:
            try:
                duracion_minutos = int(input("Duración en minutos: "))
                if duracion_minutos < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número entero positivo para la duración."
                )

        while True:
            try:
                calorias_quemadas = float(input("Calorías quemadas: "))
                if calorias_quemadas < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número positivo para las calorías quemadas."
                )

        self.registros_diarios["actividad_fisica"].append(
            ActividadFisica(tipo_ejercicio, duracion_minutos, calorias_quemadas)
        )
        print("Actividad física registrada exitosamente.")

    def registrar_pasos(self):
        """Permite al usuario registrar los pasos caminados."""
        print("\n--- Registrar Pasos Caminados ---")
        while True:
            try:
                cantidad_pasos = int(input("Cantidad de pasos caminados: "))
                if cantidad_pasos < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número entero positivo para los pasos."
                )

        self.registros_diarios["pasos"].append(Pasos(cantidad_pasos))
        print("Pasos registrados exitosamente.")

    def registrar_sueno(self):
        """Permite al usuario registrar las horas de sueño y su calidad."""
        print("\n--- Registrar Horas de Sueño ---")
        while True:
            try:
                horas_sueno = float(input("Horas de sueño: "))
                if horas_sueno < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número positivo para las horas de sueño."
                )

        calidad_subjetiva = input(
            "Calidad subjetiva del descanso (ej. excelente, buena, regular, mala): "
        )
        self.registros_diarios["sueno"].append(Sueno(horas_sueno, calidad_subjetiva))
        print("Sueño registrado exitosamente.")

# Consultor: gmvenegasc@unitru.edu.pe

    def registrar_agua(self):
        """Permite al usuario registrar la cantidad de agua consumida."""
        print("\n--- Registrar Consumo de Agua ---")
        while True:
            try:
                mililitros = float(input("Cantidad de agua consumida en mililitros: "))
                if mililitros < 0:
                    raise ValueError
                break
            except ValueError:
                print(
                    "Entrada inválida. Por favor, ingresa un número positivo para los mililitros."
                )

        self.registros_diarios["agua"].append(Agua(mililitros))
        print("Consumo de agua registrado exitosamente.")

    def generar_resumen_diario(self):
        """Genera un resumen completo de los registros del día."""
        print(f"\n--- Resumen Diario para {self.fecha_actual} ---")

        # Resumen de comidas
        total_calorias_ingeridas = sum(
            comida.calorias for comida in self.registros_diarios["comidas"]
        )
        print(f"\nAlimentación: {total_calorias_ingeridas:.2f} calorías ingeridas.")
        if not self.registros_diarios["comidas"]:
            print("No se registraron comidas hoy.")
        else:
            for comida in self.registros_diarios["comidas"]:
                print(f"  - {comida.tipo.capitalize()}: {comida.calorias:.2f} calorías")

        # Resumen de actividad física
        total_calorias_quemadas = sum(
            act.calorias_quemadas for act in self.registros_diarios["actividad_fisica"]
        )
        total_duracion_ejercicio = sum(
            act.duracion_minutos for act in self.registros_diarios["actividad_fisica"]
        )
        print(
            f"\nActividad Física: {total_calorias_quemadas:.2f} calorías quemadas en {total_duracion_ejercicio} minutos."
        )
        if not self.registros_diarios["actividad_fisica"]:
            print("No se registraron actividades físicas hoy.")
        else:
            for act in self.registros_diarios["actividad_fisica"]:
                print(
                    f"  - {act.tipo_ejercicio.capitalize()}: {act.duracion_minutos} min, {act.calorias_quemadas:.2f} calorías"
                )

        # Resumen de pasos
        total_pasos = sum(
            paso.cantidad_pasos for paso in self.registros_diarios["pasos"]
        )
        print(f"\nPasos Caminados: {total_pasos} pasos.")
        if not self.registros_diarios["pasos"]:
            print("No se registraron pasos hoy.")

        # Resumen de sueño
        if self.registros_diarios["sueno"]:
            horas_sueno_promedio = sum(
                s.horas_sueno for s in self.registros_diarios["sueno"]
            ) / len(self.registros_diarios["sueno"])
            calidad_sueno_str = ", ".join(
                set(s.calidad_subjetiva for s in self.registros_diarios["sueno"])
            )
            print(
                f"\nSueño: {horas_sueno_promedio:.2f} horas en promedio. Calidad: {calidad_sueno_str}."
            )
        else:
            print("\nSueño: No se registró información de sueño hoy.")

        # Resumen de agua
        total_agua_ml = sum(agua.mililitros for agua in self.registros_diarios["agua"])
        print(f"\nHidratación: {total_agua_ml:.2f} ml de agua consumida.")
        if total_agua_ml < 2000:  # Recomendación general de 2 litros
            print(
                "  ¡Alerta! Considera beber más agua para alcanzar los 2 litros recomendados."
            )
        if not self.registros_diarios["agua"]:
            print("No se registró consumo de agua hoy.")

        # Balance calórico
        balance_calorico = total_calorias_ingeridas - total_calorias_quemadas
        print(f"\nBalance Calórico Neto: {balance_calorico:.2f} calorías.")
        if balance_calorico > 0:
            print("  Has consumido más calorías de las que quemaste hoy.")
        elif balance_calorico < 0:
            print("  Has quemado más calorías de las que consumiste hoy.")
        else:
            print("  Tu consumo y quema de calorías estuvieron equilibrados hoy.")

        print("\n--- Fin del Resumen ---")

        input(
            Vanity_Color.blue + "Presiona Enter para continuar..." + Vanity_Color.white
        )

    def mostrar_menu(self):
        """Muestra el menú principal de la aplicación."""
        print(Vanity_Color.cyan + "\n--- NutriFit Log ---" + Vanity_Color.white)
        print("1. Registrar Comida")
        print("2. Registrar Actividad Física")
        print("3. Registrar Pasos Caminados")
        print("4. Registrar Horas de Sueño")
        print("5. Registrar Consumo de Agua")
        print("6. Generar Resumen Diario")
        print("7. Salir")
        print("0. Limpiar Pantalla")

    def ejecutar(self):
        clear_screen()
        """Ejecuta el bucle principal de la aplicación."""
        print(f"Bienvenido a NutriFit Log para hoy, {self.fecha_actual}.")
        while True:
            self.mostrar_menu()
            print(
                Vanity_Color.green
                + "Selecciona una opción del menú:"
                + Vanity_Color.white
            )
            opcion = input(Vanity_Color.yellow + " $ " + Vanity_Color.white).strip()
            if opcion == "0":
                clear_screen()
            elif opcion == "1":
                self.registrar_comida()
            elif opcion == "2":
                self.registrar_actividad_fisica()
            elif opcion == "3":
                self.registrar_pasos()
            elif opcion == "4":
                self.registrar_sueno()
            elif opcion == "5":
                self.registrar_agua()
            elif opcion == "6":
                self.generar_resumen_diario()
            elif opcion == "7":
                print("Gracias por usar NutriFit Log. ¡Que tengas un buen día!")
                break
            else:
                print("Opción inválida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    app = NutriFitLog()
    app.ejecutar()
