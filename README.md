# JhacksonPalacios1025761634

# Calculadora de Edad

Proyecto en Python que calcula la edad en años cumplidos a partir de una fecha de nacimiento. Fue creado para el taller evaluativo de **Aplicaciones y Servicios Web** (ITM) con el fin de practicar integración continua (CI/CD) con GitHub Actions.

## ¿Qué hace?

- `calcular_edad(fecha_nacimiento, hoy=None)`: devuelve la edad en años cumplidos. Si no se envía `hoy`, usa la fecha actual del sistema.
- `es_mayor_de_edad(fecha_nacimiento, hoy=None)`: devuelve `True` si la persona tiene 18 años o más.
- `main.py`: programa interactivo que pide la fecha en formato `AAAA-MM-DD` e imprime la edad.

## Estructura del proyecto

```
.
├── .github/
│   └── workflows/
│       └── ci.yml        # Flujo de CI/CD (GitHub Actions)
├── edad.py               # Lógica del cálculo de edad
├── main.py               # Programa interactivo
├── test_edad.py          # Pruebas automáticas con pytest
├── requirements.txt      # Dependencias (pytest)
└── README.md
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python main.py
```

## Cómo correr las pruebas

```bash
pytest
```

Las pruebas cubren estos casos:

- Persona que ya cumplió años en el año actual.
- Persona que aún no ha cumplido años.
- Persona que cumple años exactamente hoy.
- Nacidos el 29 de febrero (año bisiesto).
- Fecha de nacimiento en el futuro (debe lanzar `ValueError`).
- Verificación de mayoría de edad.

Todas usan una **fecha de referencia fija** (`26 de noviembre de 2026`), de modo que el resultado sea siempre el mismo sin importar cuándo se ejecuten.

## Integración continua (CI/CD)

El archivo `.github/workflows/ci.yml` configura un flujo de GitHub Actions que se ejecuta **automáticamente en cada push a la rama `main`**. El flujo realiza estos pasos:

1. Descarga el código del repositorio (`actions/checkout`).
2. Configura Python 3.12 (`actions/setup-python`).
3. Instala las dependencias con `pip install -r requirements.txt`.
4. Ejecuta las pruebas con `pytest`.

Si alguna prueba falla, el flujo se marca en rojo ❌; si todas pasan, en verde ✅.

## Historial de commits de la actividad

| Commit | Cambio | Qué prueba del CI |
|---|---|---|
| Inicial | `edad.py`, `test_edad.py`, `requirements.txt` | Base del proyecto |
| Agrega ci.yml | Flujo de GitHub Actions | Primera ejecución automática |
| Agrega es_mayor_de_edad | Nueva función y su test | El CI ejecuta el nuevo test |
| Agrega programa principal | `main.py` | El CI sigue pasando con el nuevo archivo |
| Agrega README | Este documento | El CI se ejecuta en cada cambio |