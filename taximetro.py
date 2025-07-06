# Taxímetro Digital de F5
# Este programa simula un taxímetro digital que calcula tarifas basadas en el tiempo de trayecto
# y el estado del taxi (en movimiento o parado).
# Autor: Alfonso Bermúdez

# import time para manejar el tiempo de trayecto
import time

# import os para manejar el sistema de archivos (logs)
import os

# import logging para manejar el registro de eventos (logs)
import logging

# Crear el directorio de logs si no existe
if not os.path.exists('logs'):
    os.makedirs('logs')

# Crear el directorio de historial_trayectos si no existe
# Nota: historial_trayectos se usa para almacenar los detalles de los trayectos
if not os.path.exists('historial_trayectos'):
    os.makedirs('historial_trayectos')


# import datetime para manejar fechas y horas
# Nota: datetime se usa para registrar la fecha y hora de los trayectos en el historial
from datetime import datetime



# Configuración del logging a archivo
logging.basicConfig(
    level=logging.DEBUG,  # Mostrar todos los niveles desde DEBUG en adelante
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje de lo
    filename='logs/taximetro.log', # Archivo donde se almacenan los logs
    filemode='a' # Modo de apertura del archivo (a: append, w: write)
)

"""
DEBUG	Para cálculo interno de tarifa y tiempo (información para desarrollo)
INFO	Inicio/fin de trayecto, cambio de estado (Información funcionamiento normal)
WARNING	Entrada no válida del usuario 
ERROR	Entrada errónea o excepción controlada 
CRITICAL	Error inesperado grave (ej: interrupción o fallo total del programa)
"""

#
def calcular_tarifa(duracion, en_movimiento):
    """
    Calcula la tarifa según la duración y si el taxi está en movimiento o parado.
    """
    # Validación de la duración, asegurando que sea un número positivo
    if duracion < 0:
        logging.error("Duración negativa detectada.")
        return 0.0

    # Determinar la tarifa por segundo cuando el taxi está en movimiento o parado
    if en_movimiento:
        tarifa_por_segundo = 0.05
        estado = "movimiento"
    else: 
        tarifa_por_segundo = 0.02
        estado = "parado"

    # Calcular la tarifa 
    logging.debug(f"Duración: {duracion:.2f} s en {estado}. Tarifa parcial: {duracion * tarifa_por_segundo:.2f} €")
    return duracion * tarifa_por_segundo



# función de bienvenida que muestra un mensaje inicial y las instrucciones
def bienvenida():
    """
    Muestra un mensaje de bienvenida e instrucciones.
    """
    print("Bienvenido al Taxímetro Digital de F5")
    print("-" * 40)
    print("Instrucciones:")
    print(" - Escribe 'start' para iniciar un trayecto")
    print(" - Escribe 'stop' para finalizar el trayecto")
    print(" - Durante el trayecto, introduce 'M/m' (movimiento) o 'P/p' (parado)")
    print(" - Tarifa: 0.05 €/seg en movimiento, 0.02 €/seg parado")
    print(" - Escribe 'exit' para salir del programa")
    print("-" * 40)


# función que inicia el trayecto, gestiona el tiempo y la tarifa
def iniciar_trayecto():
    """
    Gestiona el trayecto: tiempo, tarifa e interacción con el usuario.
    """
    tarifa_total = 0.0
    duracion_total_mov = 0.0
    duracion_total_parado = 0.0
    print("\nTrayecto iniciado. Escribe 'stop' para finalizar.\n")
    logging.info("Trayecto iniciado.")
    
    '''# Estado inicial del taxi
    estado_inicial = input("¿Está el taxi en movimiento? (s/n): ").lower()
    if estado_inicial not in ['s', 'n']:
        print("Entrada no válida. Usa 's' o 'n'.")
        logging.error(f"Estado inicial no válido: {estado_inicial}")
        return
    '''
    # Bucle para validar correctamente la entrada
    # Mensaje inicial según el estado del taxi
    # Mientras se cumpla condición
    while True:
        estado_inicial = input("¿Está el taxi en movimiento? (s/n): ").lower()
        if estado_inicial in ['s', 'n']:
            break
        else:
            print("Entrada no válida. Usa 's' o 'n'.")
            logging.warning(f"Estado inicial no válido: {estado_inicial}")


    # Convertir el estado inicial a booleano 's' para en movimiento
    en_movimiento = estado_inicial == 's'
    tiempo_anterior = time.time()

    # Mensaje inicial según el estado del taxi
    # Mientras se cumpla condición 
    while True:
        comando = input("Introduce estado ('M/m' (movimiento) o 'P/p' (parado)) o 'stop': ").lower()
        tiempo_actual = time.time()

        # Calcular la duración del trayecto
        duracion = tiempo_actual - tiempo_anterior

        # Calcular la tarifa total con la tarifa acumulada
        tarifa_total += calcular_tarifa(duracion, en_movimiento)
        
        if en_movimiento:
            duracion_total_mov += duracion
        else:
            duracion_total_parado += duracion

        tiempo_anterior = tiempo_actual

        
        if comando == 'stop':
            print(f"\nTrayecto finalizado. Tarifa total: {tarifa_total:.2f} €\n")
            logging.info(f"Trayecto finalizado. Tarifa total: {tarifa_total:.2f} €")
            guardar_en_historial(tarifa_total, duracion_total_mov, duracion_total_parado)
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
            print("Entrada no válida. Usa 'M/m', 'P/p' o 'stop'.")
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

def guardar_en_historial(tarifa_total, duracion_movimiento, duracion_parado):
    """
    Guarda los detalles del trayecto en un archivo historial.txt
    """
    try:
        with open("historial_trayectos/historial.txt", "a", encoding="utf-8") as file:
            file.write("=== Nuevo trayecto ===\n")
            file.write(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Tiempo en movimiento: {duracion_movimiento:.2f} s\n")
            file.write(f"Tiempo parado: {duracion_parado:.2f} s\n")
            file.write(f"Tarifa total: {tarifa_total:.2f} €\n\n")
        logging.info("Trayecto guardado en historial.txt")
    except Exception as e:
        logging.error(f"No se pudo guardar el trayecto en el historial: {e}")

