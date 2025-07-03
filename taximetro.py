import time

import logging


# Configuración del logging a archivo
logging.basicConfig(
    level=logging.DEBUG,  # Mostrar todos los niveles desde DEBUG en adelante
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje de lo
    filename='taximetro.log', # Archivo donde se almacenan los logs
    filemode='a' # Modo de apertura del archivo (a: append, w: write)
)

"""
DEBUG	Para cálculo interno de tarifa y tiempo (información para desarrollo)
INFO	Inicio/fin de trayecto, cambio de estado (Información funcionamiento normal)
WARNING	Entrada no válida del usuario 
ERROR	Entrada errónea o excepción controlada 
CRITICAL	Error inesperado grave (ej: interrupción o fallo total del programa)
"""

def calcular_tarifa(duracion, en_movimiento):
    """
    Calcula la tarifa según la duración y si el taxi está en movimiento o parado.
    """
    if duracion < 0:
        logging.error("Duración negativa detectada.")
        return 0.0

    if en_movimiento:
        tarifa_por_segundo = 0.05
        estado = "movimiento"
    else: 
        tarifa_por_segundo = 0.02
        estado = "parado"

 
    logging.debug(f"Duración: {duracion:.2f} s en {estado}. Tarifa parcial: {duracion * tarifa_por_segundo:.2f} €")
    return duracion * tarifa_por_segundo




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
    logging.info("Trayecto iniciado.")
    # Estado inicial del taxi


    estado_inicial = input("¿Está el taxi en movimiento? (s/n): ").lower()
    if estado_inicial not in ['s', 'n']:
        print("Entrada no válida. Usa 's' o 'n'.")
        logging.error(f"Estado inicial no válido: {estado_inicial}")
        return

    en_movimiento = estado_inicial == 's'
    tiempo_anterior = time.time()

    while True:
        comando = input("Introduce estado ('M' (movimiento) o 'P' (parado)) o 'stop': ").lower()
        tiempo_actual = time.time()
        duracion = tiempo_actual - tiempo_anterior
        tarifa_total += calcular_tarifa(duracion, en_movimiento)
        tiempo_anterior = tiempo_actual

        if comando == 'stop':
            print(f"\nTrayecto finalizado. Tarifa total: {tarifa_total:.2f} €\n")
            logging.info(f"Trayecto finalizado. Tarifa total: {tarifa_total:.2f} €")
            break
        elif comando == 'm':
            en_movimiento = True
            print(f"Taxi en movimiento. Tarifa acumulada: {tarifa_total:.2f} €")
            logging.info(f"Estado cambiado a movimiento. Tarifa: {tarifa_total:.2f} €")
        elif comando == 'p':
            en_movimiento = False
            print(f"Taxi parado. Tarifa acumulada: {tarifa_total:.2f} €")
            logging.info(f"Estado cambiado a parado. Tarifa: {tarifa_total:.2f} €")
        else:
            print("Entrada no válida. Usa 'M', 'P' o 'stop'.")
            logging.warning(f"Comando no reconocido: {comando}")

def ejecutar_taximetro():
    """
    Función principal del programa que gestiona el ciclo de vida.
    """
    bienvenida()
    while True:
        try:
            comando = input("Comando (start/exit): ").lower()   
            if comando == 'start':
                iniciar_trayecto()
            elif comando == 'exit':
                print("¡Hasta pronto! Gracias por usar el Taxímetro Digital de F5.")
                logging.info("Programa finalizado por el usuario.")
                break
            else:
                print("Comando no válido. Usa 'start' o 'exit'.")
                logging.warning(f"Comando inválido en menú principal: {comando}")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            logging.critical("Programa interrumpido por el usuario.")
            break

