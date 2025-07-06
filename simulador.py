import time
from taximetro import calcular_tarifa

class SimuladorTaxi:
    """
    Simula el comportamiento de un trayecto de taxi
    utilizando comandos en vez de entradas interactivas (input).
    """
    def __init__(self):
        self.en_movimiento = False
        self.tarifa_total = 0.0
        self.iniciado = False
        self.inicio = None

    def run(self, comando):
        """
        Ejecuta una acción según el comando recibido.
        """
        comando = comando.lower()

        if comando == "start":
            if self.iniciado:
                return "❌ El trayecto ya ha sido iniciado."
            self.iniciado = True
            self.inicio = time.time()
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
            # Simula 1 segundo de espera y calcula la tarifa
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
