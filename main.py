import os
import sys
import random
from time import sleep
from valid_activity import simulate_valid_logins, simulate_valid_file_access, simulate_valid_emails
from threat_activity import simulate_threat_logins, simulate_threat_file_access, simulate_threat_file_transfers, simulate_threat_emails
from utils import start_time, end_time, generate_random_timestamp

# Asegurarse de que Python busque en el directorio actual los módulos necesarios.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Cargar la configuración desde config.json
# Aquí es donde se define la distribución de eventos, archivos, usuarios y configuraciones de amenazas.
import json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Crear la carpeta "logs" si no existe.
# Todos los eventos generados se guardarán en esta carpeta.
if not os.path.exists("logs"):
    os.makedirs("logs")

# Esta función determina si el evento ocurre durante el horario laboral especificado.
def is_work_hours():
    work_start = datetime.strptime(config["time_settings"]["work_hours_start"], "%H:%M").time()
    work_end = datetime.strptime(config["time_settings"]["work_hours_end"], "%H:%M").time()
    current_time = datetime.now().time()
    return work_start <= current_time <= work_end

# Función principal para generar eventos mixtos (tanto válidos como amenazas)
def generate_mixed_events():
    # Calcular el número total de eventos según lo especificado en config.json
    total_events = sum(config["event_distribution"][event]["valid"] + config["event_distribution"][event]["threat"] for event in config["event_distribution"])
    
    # Definir los intervalos mínimos y máximos entre eventos
    min_interval = config["interval_distribution"]["min_interval"]
    max_interval = config["interval_distribution"]["max_interval"]

    # Iterar para generar el número total de eventos
    for _ in range(total_events):
        # Generar un evento aleatorio: 70% de probabilidad de que sea válido y 30% de que sea una amenaza
        if random.random() < 0.7:
            # Generar un evento válido
            simulate_valid_logins(1)
            simulate_valid_file_access(1)
            simulate_valid_emails(1)
        else:
            # Generar una amenaza
            simulate_threat_logins(1)
            simulate_threat_file_access(1)
            simulate_threat_file_transfers(1)
            simulate_threat_emails(1)
        
        # Introducir un intervalo aleatorio entre eventos, usando los valores configurados.
        sleep(random.uniform(min_interval, max_interval))

# Ejecutar la función principal para iniciar la simulación.
generate_mixed_events()
