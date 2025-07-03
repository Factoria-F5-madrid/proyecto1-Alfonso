# Módulo time
import time

# Menú de bienvenida al usuario e instrucciones funcionamiento Taxímetro Digital
def bienvenida():
    print("Bienvenido al Taxímetro Digital de F5")
    print("Instrucciones:")
    print("- Escribe 'start' para iniciar el trayecto.")
    print("- Escribe 'stop' para detener el trayecto.")
    print("- Escribe 'exit' para salir del programa.")
    print()

# Función para iniciar el trayecto


def iniciar_trayecto():
    print("\nTrayecto iniciado.")
    tarifa_total = 0.0
    estado = input("¿Está el taxi en movimiento? (s/n): ").lower()

    print("Escribe 'parar' para finalizar trayecto.\n")
    inicio = time.time()



    while True:
        comando = input(">>> ").lower()
        if comando == 'parar':
            fin = time.time()
            duracion = fin - inicio

            if estado == 's':
                tarifa_total = duracion * 0.05
            else:
                tarifa_total = duracion * 0.02

            print(f"Trayecto finalizado. Tarifa total: {tarifa_total:.2f} €\n")
            break
        else:
            print("Comando no válido. Escribe 'parar' para finalizar trayecto.")

def main():
    bienvenida()
    while True:
        comando = input("Comando (start/exit): ").lower()
        if comando == 'start':
            iniciar_trayecto()
        elif comando == 'exit':
            print("¡Hasta pronto! Gracias por usar el Taxímetro Digital de F5.")
            break
        else:
            print("Comando no válido.")

if __name__ == "__main__":
    main()