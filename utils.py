import json
import random
from datetime import datetime, timedelta

# Cargar la configuración del archivo config.json
# Este archivo contiene información sobre los usuarios, archivos, distribución de eventos, fechas y más.
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Convertir las cadenas de fecha (start_time y end_time) en objetos datetime
# Esto permite usar estas fechas para generar eventos en un rango de fechas específico.
start_time = datetime.strptime(config["date_range"]["start_time"], "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime(config["date_range"]["end_time"], "%Y-%m-%d %H:%M:%S")

# Función para generar una marca de tiempo aleatoria dentro del rango de fechas (start_time, end_time)
# Esta función se usa para dar a los eventos marcas de tiempo aleatorias pero dentro de un intervalo específico.
def generate_random_timestamp(start_time, end_time):
    delta = end_time - start_time
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_time + timedelta(seconds=random_seconds)
