
# Simulador de Eventos de Seguridad Empresarial

## Descripción Técnica

El **Simulador de Eventos de Seguridad Empresarial** es un software basado en Python que permite la simulación de actividades válidas y amenazas internas en un entorno empresarial pequeño. Este simulador genera eventos que pueden ser usados para monitorear, analizar y estudiar sistemas de seguridad.

### Requisitos

- **Python 3.7+** instalado en el sistema.
- Dependencias estándar como `os`, `sys`, `json`, `random`, y `time`.
- Archivos de configuración JSON para definir la naturaleza de los eventos simulados.

### Estructura del Proyecto

- `main.py`: Archivo principal que coordina la ejecución de los eventos simulados.
- `utils.py`: Contiene funciones auxiliares como la generación de marcas de tiempo aleatorias y la carga del archivo de configuración.
- `valid_activity.py`: Genera eventos válidos como inicios de sesión exitosos, accesos a archivos normales y correos internos.
- `threat_activity.py`: Genera eventos sospechosos o maliciosos, como intentos de inicio de sesión fallidos y transferencias no autorizadas de datos.
- `config.json`: Archivo de configuración que define el comportamiento de la simulación.
- `logs/`: Carpeta donde se almacenan los logs generados.

### Funcionamiento del Software

1. **Carga de Configuración**:
   El archivo `config.json` es cargado al inicio de la ejecución. Este archivo permite configurar:
   - Los usuarios involucrados en la simulación.
   - Archivos y destinos involucrados.
   - Distribución de eventos válidos y amenazas.
   - Parámetros relacionados con los tiempos de simulación.

2. **Generación de Eventos**:
   Los eventos se dividen en dos categorías principales:
   - **Eventos válidos**: Estos eventos simulan el comportamiento normal de la empresa, como inicios de sesión y acceso a archivos por usuarios autorizados.
   - **Eventos de amenazas**: Simulan actividades maliciosas, como intentos de acceso a archivos sensibles, transferencias no autorizadas de archivos y correos electrónicos externos.

3. **Logs Generados**:
   Los eventos son almacenados en formato de texto dentro de la carpeta `logs`. Estos archivos contienen detalles sobre cada evento, incluyendo el usuario involucrado, la acción tomada, y la hora del evento.

### Archivo de Configuración (`config.json`)

El archivo `config.json` define los parámetros de la simulación. Los parámetros más relevantes incluyen:

- `users`: Define los usuarios del sistema.
- `files`: Lista de archivos a los que se accede en los eventos.
- `event_distribution`: Especifica el número de eventos válidos y amenazas generados.
- `date_range`: Rango de fechas y horas en las que se generan los eventos.
- `interval_distribution`: Define los intervalos entre la generación de eventos.

### Ejecución

1. **Preparar el entorno**: Asegúrate de tener Python 3 instalado. Luego, navega a la carpeta del proyecto en la terminal.
2. **Ejecutar el simulador**: Ejecuta el comando siguiente en tu terminal:
   
   ```bash
   python main.py
   ```

3. **Resultados**: Los logs de los eventos generados estarán en la carpeta `logs/`.

### Personalización

El comportamiento del simulador puede ajustarse a las necesidades del usuario modificando el archivo `config.json`. Esto permite:
- Cambiar los usuarios y archivos simulados.
- Definir el número de eventos de amenazas y válidos.
- Especificar las tasas de éxito para actividades sospechosas.

### Ejemplo de un evento en los logs

```txt
2024-01-03 14:22:34 | User=user1@company.com | Action=Failed Login | IP=192.168.1.5 | Location=Remote
2024-01-05 11:12:45 | User=admin@company.com | Action=File Read | File=Sensitive_File.txt | Unauthorized=True
```

### Notas Adicionales

- Este simulador no incluye la simulación en tiempo real, los eventos se generan en un rango de tiempo definido, pero no en tiempo real.
- La generación de los eventos puede personalizarse añadiendo más tipos de eventos o modificando los scripts de generación de logs.
