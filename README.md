# Evaluacion2 – Geolocalización con GraphHopper (Python)

Proyecto de la Evaluación Parcial N°2 de CUY6142 (Duoc UC).
Script en Python que consume la API de GraphHopper (Geocoding + Routing) para calcular
la ruta entre dos ubicaciones. Esta versión está modificada para:

- Mostrar todos los mensajes al usuario en español.
- Mostrar distancias y tiempos con un máximo de dos decimales.
- Permitir salir del programa escribiendo `s` o `salir`.
- Imprimir la narrativa del viaje (indicaciones paso a paso) en español (`locale=es`).

## Requisitos

- Python 3
- Librería `requests` (`pip3 install requests`)
- Una API key de GraphHopper (https://graphhopper.com)

## Cómo ejecutarlo

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Abraham21-C/Evaluacion2.git
   cd Evaluacion2
   ```
2. Abrir `graphhopper_es.py` y reemplazar el valor de `key` por tu API key.
3. Ejecutar:
   ```bash
   python3 graphhopper_es.py
   ```
4. Ingresar el perfil de vehículo (`car`, `bike` o `foot`), el origen y el destino.
   Escribir `s` o `salir` en cualquier pregunta para terminar.

## Ejemplo

```
Ingrese un perfil de vehículo de la lista (s o salir para terminar): car
Ubicación de origen (s o salir para terminar): Huechuraba, Chile
Destino (s o salir para terminar): Biblioteca Nacional de Chile, Santiago
```