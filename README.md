
# 🚕 Proyecto Taxímetro Digital

Aplicación desarrollada en Python que **simula el funcionamiento de un taxímetro** desde la línea de comandos (CLI).  
Este proyecto forma parte de un proceso de aprendizaje con los siguientes **objetivos**:

---

## 🎯 Objetivos del proyecto

- Iniciarse en la programación funcional en **Python**
- Practicar el diseño modular y separación de lógica en módulos
- Familiarizarse con el uso de **Git** y **GitHub**
- Usar herramientas de control de versiones de forma profesional:
  - Uso de ramas (`main`, `dev`, `test`)
  - Uso de *issues*, *pull requests* y tablero **Kanban**
  - Uso de templates para issues y PRs
  - Estandarización de commits (`feat:`, `fix:`, `docs:`, etc.)

---

## 🧩 Funcionamiento del programa

El usuario puede:

1. Iniciar un trayecto (`start`)
2. Indicar si el taxi está en movimiento o parado (`M` o `P`)
3. Cambiar entre estados durante el trayecto
4. Finalizar trayecto (`stop`)
5. Consultar el precio acumulado
6. Guardar automáticamente cada trayecto en un historial (`historial_trayectos/historial.txt`)

### 💰 Tarifas

- 🚗 Movimiento: `0,05 €` por segundo  
- ⛔ Parado: `0,02 €` por segundo  

---

## 📁 Estructura del proyecto

```bash
taximetro-digital/
├── main.py                          # Punto de entrada principal
├── taximetro.py                     # Lógica de negocio del taxímetro
├── logs/
│   └── taximetro.log                # Registro de eventos y errores
├── historial_trayectos/
│   └── historial.txt                # Registro de trayectos pasados
├── tests/
│   ├── __init__.py
│   └── test_simulador.py           # Tests unitarios
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature_request.yml
│   │   └── style_request.yml
│   └── PULL_REQUEST_TEMPLATE.md    # Plantilla de Pull Requests
├── .gitignore
├── .gitattributes
└── README.md
```

---

## 🚀 Cómo ejecutar la aplicación

Desde la terminal, ejecuta:

```bash
python main.py
```

---

## ✅ Ejemplo de uso

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

## 🧪 Ejecución de tests

Los tests se ejecutan con `unittest` y validan el comportamiento de funciones clave como `calcular_tarifa`.

Desde la raíz del proyecto, ejecuta:

```bash
python -m unittest tests.test_simulador.py
```

O con el lanzador simplificado:

```bash
python run_tests.py
```

La salida del test es clara, con mensajes amigables que indican qué se está probando.

---

## 📌 Buenas prácticas usadas

- ✔️ Uso de `logging` para registrar actividad
- ✔️ Historial de trayectos guardado automáticamente
- ✔️ `.gitignore` configurado para evitar subir archivos temporales
- ✔️ Commit messages semánticos: `feat:`, `fix:`, `docs:`, `refactor:`
- ✔️ Separación clara de lógica y pruebas
- ✔️ Plantillas para Issues y Pull Requests

---

## 📋 Gestión del proyecto

Proyecto organizado en tablero **Kanban** dentro de GitHub con las columnas:

- Backlog
- Ready
- In progress
- In review
- Done

🔗 [Ver tablero Kanban del proyecto](https://github.com/orgs/Factoria-F5-madrid/projects/13/views/1)

---

## ✍️ Autor

Proyecto desarrollado por **Alfonso**  
Como parte del programa de formación de **Factoria F5 - Madrid**
