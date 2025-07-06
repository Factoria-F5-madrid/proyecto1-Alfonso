# Importamos el módulo unittest para crear pruebas automáticas
import time

# Importamos la función que vamos a probar del módulo taximetro
from taximetro import calcular_tarifa

class SimuladorTaxi:
    """
    Clase que simula el comportamiento de un taxímetro.
    Esta clase permite aceptar comandos,
    Permite controlar el taxi con comandos simples ('start', 'move', 'wait 1', etc.),
    facilitando así la escritura de tests automáticos.
    """

    def __init__(self):
        # Variables internas que almacenan el estado del taxi
        self.en_movimiento = False
        self.tarifa_total = 0.0
        self.iniciado = False
        self.inicio = None

    def run(self, comando):
        """
        Ejecuta un comando para simular una acción del taxi.
        """

        comando = comando.lower()  # Asegura que el comando sea en minúsculas

        if comando == "start":
            if self.iniciado:
                return "❌ El trayecto ya ha sido iniciado."  # No se puede volver a iniciar
            self.iniciado = True
            self.inicio = time.time()  # Guardamos el momento del inicio
            return "✅ Trayecto iniciado correctamente."

        elif comando == "move":
            if not self.iniciado:
                return "❌ Error: inicia el trayecto antes de mover el taxi."
            self.en_movimiento = True
            return "➡️ Taxi ahora en movimiento."

        elif comando == "stop":
            if not self.iniciado:
                return "❌ Error: no puedes parar si el trayecto no ha comenzado."
            self.en_movimiento = False
            return "🅿️ Taxi ahora está parado."

        elif comando == "wait 1":
            # Simula 1 segundo de espera con time.sleep()
            # y calcula la tarifa acumulada en ese segundo
            time.sleep(1)
            duracion = 1
            self.tarifa_total += calcular_tarifa(duracion, self.en_movimiento)
            return f"⏱️ 1 segundo registrado. Tarifa actual: {self.tarifa_total:.2f} €"

        elif comando == "end":
            if not self.iniciado:
                return "❌ No hay trayecto en curso para finalizar."
            self.iniciado = False
            return f"🛑 Trayecto finalizado. Tarifa total: {self.tarifa_total:.2f} €"

        elif comando == "quit":
            return "👋 Saliendo del simulador."

        else:
            return "❓ Comando no reconocido."