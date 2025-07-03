import time

def calcular_tarifa(duracion, en_movimiento):
    """
    Calcula la tarifa según la duración y si el taxi está en movimiento o parado.
    """

    if en_movimiento:
        tarifa_por_segundo = 0.05
    else: 
        tarifa_por_segundo = 0.02
    tarifa_total = duracion * tarifa_por_segundo
    return tarifa_total


def bienvenida():
    """
    Muestra un mensaje de bienvenida e instrucciones.
    """
    print("Bienvenido al Taxímetro Digital de F5")
    print("-" * 40)
    print("Instrucciones:")
    print(" - Escribe 'start' para iniciar un trayecto")
    print(" - Escribe 'stop' para finalizar el trayecto")
    print(" - Durante el trayecto, introduce 'M' (movimiento) o 'P' (parado)")
    print(" - Tarifa: 0.05 €/seg en movimiento, 0.02 €/seg parado")
    print(" - Escribe 'exit' para salir del programa")
    print("-" * 40)

def iniciar_trayecto():
    """
    Gestiona el trayecto: tiempo, tarifa e interacción con el usuario.
    """
    tarifa_total = 0.0
    print("\nTrayecto iniciado. Escribe 'stop' para finalizar.\n")
    estado_inicial = input("¿Está el taxi en movimiento? (s/n): ").lower()
    en_movimiento = True if estado_inicial == 's' else False
    tiempo_anterior = time.time()

    while True:
        comando = input("Introduce estado ('M' (movimiento) o 'P' (parado)) o 'stop': ").lower()
        tiempo_actual = time.time()
        duracion = tiempo_actual - tiempo_anterior
        tarifa_total += calcular_tarifa(duracion, en_movimiento)
        tiempo_anterior = tiempo_actual

        if comando == 'stop':
            print(f"\nTrayecto finalizado. Tarifa total: {tarifa_total:.2f} €\n")
            break
        elif comando == 'm':
            en_movimiento = True
            print(f"Taxi en movimiento. Tarifa acumulada: {tarifa_total:.2f} €")
        elif comando == 'p':
            en_movimiento = False
            print(f"Taxi parado. Tarifa acumulada: {tarifa_total:.2f} €")
        else:
            print("Entrada no válida. Usa 'M', 'P' o 'stop'.")

def ejecutar_taximetro():
    """
    Función principal del programa que gestiona el ciclo de vida.
    """
    bienvenida()
    while True:
        comando = input("Comando (start/exit): ").lower()
        if comando == 'start':
            iniciar_trayecto()
        elif comando == 'exit':
            print("¡Hasta pronto! Gracias por usar el Taxímetro Digital de F5.")
            break
        else:
            print("Comando no válido. Usa 'start' o 'exit'.")
