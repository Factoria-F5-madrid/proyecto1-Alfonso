# 🚕 Proyecto Taxímetro Digital

Este es un proyecto básico de una aplicación en Python que **simula el funcionamiento de un taxímetro** a través de la línea de comandos (CLI).  
Forma parte de un ejercicio práctico con los siguientes **objetivos principales**:

---

## 🎯 Objetivos del proyecto

- Iniciarse en la programación de una aplicación funcional en **Python**.
- Practicar la estructura y modularización de código.
- Familiarizarse con el uso de **Git** y **GitHub** desde el inicio del desarrollo.
- Adoptar buenas prácticas de control de versiones, incluyendo:
  - Uso de ramas (opcionalmente)
  - Convenciones para mensajes de `commit` (como `feat:`, `fix:`, `docs:`, `refactor:`)

---

## 🧩 Descripción del funcionamiento

El programa permite:

1. Mostrar un mensaje de bienvenida.
2. Iniciar un trayecto simulando un taxi en movimiento o parado.
3. Calcular el coste del trayecto:
   - 📍 Parado: 0,02 € por segundo
   - 🛣️ En movimiento: 0,05 € por segundo
4. Cambiar entre estados durante el trayecto (`M` = movimiento, `P` = parado).
5. Finalizar el trayecto y mostrar la tarifa total.

Toda la lógica del negocio está encapsulada en el archivo `taximetro.py`, mientras que `main.py` sirve únicamente como punto de entrada.

---

## 📁 Estructura del proyecto

```
proyecto1-Alfonso/
├── main.py              # Punto de entrada, ejecuta el taxímetro
├── taximetro.py         # Lógica principal de la aplicación
└── README.md            # Este archivo de documentación
```

---

## 🚀 Ejecución

Desde tu terminal, ejecuta:

```bash
python main.py
```

---

## ✅ Ejemplo de uso

```
Comando (start/exit): start
¿Está el taxi en movimiento? (s/n): s
Introduce estado (M/P) o 'stop': m
Taxi en movimiento. Tarifa acumulada: 0.25 €
Introduce estado (M/P) o 'stop': p
Taxi parado. Tarifa acumulada: 0.34 €
Introduce estado (M/P) o 'stop': stop
Trayecto finalizado. Tarifa total: 0.41 €
```

---

## 📌 Buenas prácticas Git utilizadas

- `feat:` para nuevas funcionalidades
- `fix:` para correcciones de errores
- `docs:` para documentación
- `refactor:` para reorganización de código
- Commits realizados de forma incremental y con sentido

---

## ✍️ Autor

Desarrollado por **Alfonso** como parte del proyecto de aprendizaje en **Factoria F5 Madrid**.


