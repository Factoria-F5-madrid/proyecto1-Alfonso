![Banner del proyecto](assets/banner.png)

#  Proyecto Taxímetro Digital

Este es un proyecto de una aplicación básica en Python que **simula el funcionamiento de un taxímetro** a través de la línea de comandos (CLI).  
Forma parte de un proceso de aprendizaje en donde con este ejercicio práctico se pretenden conseguir los siguientes **objetivos principales**:

---

##  Objetivos del proyecto

- Iniciarse en la programación funcional en **Python**
- Practicar la estructura y modularización de código.
- Familiarizarse con el uso de **Git** y **GitHub** desde el inicio del desarrollo.
- Adoptar buenas prácticas de control de versiones, incluyendo:
  - Uso de ramas (`main`, `dev`, `test`)
  - Convenciones para mensajes de `commit` (como `feat:`, `fix:`, `docs:`, `refactor:`)
  - Uso de *issues*, *pull requests* y tablero **Kanban**
  - Uso de templates para issues y PRs

---

##  Descripción del funcionamiento del programa

El programa permite:

1. Mostrar un mensaje de bienvenida
2. Iniciar un trayecto (`start`),
3. Indicar si el taxi está en movimiento (`M/m`) o parado (`P/p`)
4. Cambiar entre estados durante el trayecto (`M/m` = movimiento, `P/p` = parado).
5. Calcular el coste del trayecto a partir de las siguientes tarifas:
   - 📍 Parado: 0,02 € por segundo
   - 🚗 En movimiento: 0,05 € por segundo
4. Cambiar entre estados durante el trayecto 
5. Finalizar el trayecto ('stop') y mostrar la tarifa total.
6. Guardar automáticamente cada trayecto en un historial (`historial_trayectos/historial.txt`)
7. Existe un registro de log para comprobar la ejecución del programa


---

##  Estructura del proyecto

```bash
proyecto1-Alfonso/
├── main.py                          # Punto de entrada principal
├── taximetro.py                     # Lógica de negocio del taxímetro
├── logs/
│   └── taximetro.log                # Registro de eventos y errores
├── historial_trayectos/
│   └── historial.txt                # Registro de trayectos pasados
├── run_tests.py                     # Script ejecución de tests
├── simulador.py                     # Poder simular la ejecución de test
├── tests/
│   ├── __init__.py
│   └── test_simulador.py           # Tests unitarios
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature_request.yml
│   │   └── style_request.yml
│   └── PULL_REQUEST_TEMPLATE.md    # Plantilla de Pull Requests
├── .gitignore
└── README.md
```

Toda la lógica del negocio está encapsulada en el archivo `taximetro.py`, mientras que `main.py` sirve únicamente como punto de entrada.


---

##  Cómo ejecutar la aplicación

Desde la terminal, ejecutar:

```bash
python main.py
```

---

##  Ejemplo de uso

```bash
Bienvenido al Taxímetro Digital de F5
----------------------------------------
Comando (start/exit): start
¿Está el taxi en movimiento? (s/n): s
Introduce estado ('M' o 'P') o 'stop': m
Taxi en movimiento. Tarifa acumulada: 0.10 €
Introduce estado ('M' o 'P') o 'stop': p
Taxi parado. Tarifa acumulada: 0.16 €
Introduce estado ('M' o 'P') o 'stop': stop
Trayecto finalizado. Tarifa total: 0.24 €
```

---

##  Ejecución de tests

Los tests se ejecutan con `unittest` y validan el comportamiento de funciones clave como `calcular_tarifa`.

Desde la raíz del proyecto, ejecuta:

```bash
python -m unittest tests.test_simulador.py
```

O con el lanzador simplificado:

```bash
python run_tests.py
```

La salida del test es clara, con mensajes descriptivos y comprensibles que indican qué se está probando.

---

##  Buenas prácticas utilizadas

-  Uso de `logging` para registrar actividad
-  Historial de trayectos guardado automáticamente
-  `.gitignore` configurado para evitar subir archivos temporales
-  - Convención de commit messages incrementales (feat:, fix:, docs:, refactor)`
-  Separación clara de lógica y pruebas
-  Plantillas para Issues y Pull Requests


---


##  Mejoras

El proyecto se enmarca dentro de un proceso de aprendizaje, si bien podrían proporcionarse posibles mejoras al programa que lo hicieran más realista y usable:

- Establecimiento dinámico de tarifas variables por el usuario
- Conexión con base de datos para almacenar trayectos y dotarle un aspecto más profesional
- Control de accesos para añadir seguridad y usuarios
- Creación de una interfaz gráfica para hacerlo más visual y cómodo de usar (posibilidad de ampliar a una app móvil).
- Simulación más realista con paradas intermedias, distinto tipo de tarifas (diurna, nocturna, etc.).
- Ampliación de pruebas automáticas y manejo robusto de errores
- Mejorar la estructura del código para un mejor mantenimiento y ampliación en el futuro de la aplicación.


---

##  Gestión del proyecto

Proyecto organizado en tablero **Kanban** dentro de GitHub con las columnas:

- Backlog
- Ready
- In progress
- In review
- Done

🔗 [Ver tablero Kanban del proyecto](https://github.com/orgs/Factoria-F5-madrid/projects/13/views/1)


---

##  Autor

Proyecto desarrollado por **Alfonso**, como parte del programa de formación de **Factoria F5 - Madrid**
