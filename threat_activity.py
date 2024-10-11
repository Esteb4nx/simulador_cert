from datetime import datetime
import random
from utils import generate_random_timestamp, start_time, end_time, work_start, work_end, config

# Esta función genera un intento fallido de inicio de sesión (amenaza)
def generate_threat_login_event():
    users = ['user1', 'user2', 'user3']
    action = 'Failed'
    location = 'Remote'
    user = random.choice(users)
    ip_address = f"192.168.1.{random.randint(1, 254)}"

    # Usar el parámetro off_hours_activity_rate desde config.json
    out_of_hours_chance = config["time_settings"]["off_hours_activity_rate"]

    log_time = generate_random_timestamp(start_time, end_time)
    current_time = log_time.time()

    # Verificar si el evento ocurre fuera del horario laboral usando off_hours_activity_rate
    if random.random() < out_of_hours_chance:
        while current_time >= work_start and current_time <= work_end:
            # Forzar que ocurra fuera del horario laboral si la probabilidad es menor
            log_time = generate_random_timestamp(start_time, end_time)
            current_time = log_time.time()
        out_of_hours = True
    else:
        out_of_hours = False

    log_entry = f"{log_time} | User={user} | Action={action} | Location={location} | IP={ip_address} | OutOfHours={out_of_hours}"
    
    with open("logs/login_logs.txt", "a") as file:
        file.write(log_entry + "\n")


# Esta función genera un acceso no autorizado a archivos sensibles
def generate_threat_file_access_event():
    users = ['user1', 'user2', 'user3']
    actions = ['Read', 'Delete']
    sensitive_files = ['Sensitive_File.txt', 'HR_Documents.docx', 'Financial_Report.xls']
    user = random.choice(users)
    action = random.choice(actions)
    file_accessed = random.choice(sensitive_files)

    # Usar el parámetro off_hours_activity_rate desde config.json
    out_of_hours_chance = config["time_settings"]["off_hours_activity_rate"]

    log_time = generate_random_timestamp(start_time, end_time)
    current_time = log_time.time()

    # Verificar si el evento ocurre fuera del horario laboral usando off_hours_activity_rate
    if random.random() < out_of_hours_chance:
        while current_time >= work_start and current_time <= work_end:
            log_time = generate_random_timestamp(start_time, end_time)
            current_time = log_time.time()
        out_of_hours = True
    else:
        out_of_hours = False

    log_entry = f"{log_time} | User={user} | Action={action} | File={file_accessed} | Unauthorized=True | OutOfHours={out_of_hours}"
    
    with open("logs/file_access_logs.txt", "a") as file:
        file.write(log_entry + "\n")


# Esta función genera una transferencia no autorizada de archivos sensibles a destinos externos
def generate_threat_file_transfer_event():
    users = ['user1', 'user2', 'user3']
    actions = ['Upload', 'Download']
    sensitive_files = ['Sensitive_File.txt', 'Company_Data.csv', 'Project_Plan.pdf']
    external_destinations = ['usb_drive_1', 'cloud_storage_1', 'external_server_1']
    user = random.choice(users)
    action = random.choice(actions)
    destination = random.choice(external_destinations)
    file_transferred = random.choice(sensitive_files)

    # Usar el parámetro off_hours_activity_rate desde config.json
    out_of_hours_chance = config["time_settings"]["off_hours_activity_rate"]

    log_time = generate_random_timestamp(start_time, end_time)
    current_time = log_time.time()

    # Verificar si el evento ocurre fuera del horario laboral usando off_hours_activity_rate
    if random.random() < out_of_hours_chance:
        while current_time >= work_start and current_time <= work_end:
            log_time = generate_random_timestamp(start_time, end_time)
            current_time = log_time.time()
        out_of_hours = True
    else:
        out_of_hours = False

    log_entry = f"{log_time} | User={user} | Action={action} | File={file_transferred} | Destination={destination} | Unauthorized=True | OutOfHours={out_of_hours}"
    
    with open("logs/file_transfer_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Esta función genera correos electrónicos con archivos sensibles enviados a direcciones externas
def generate_threat_email_event():
    internal_users = ['admin@company.com', 'user1@company.com', 'user2@company.com', 'user3@company.com']  # Usuarios internos
    external_emails = ['external_user@gmail.com', 'external_server@external.com']  # Destinatarios externos no autorizados
    sensitive_files = ['Sensitive_File.txt', 'HR_Documents.docx', 'Financial_Report.xls']  # Archivos sensibles
    user_from = random.choice(internal_users)
    user_to = random.choice(external_emails)
    file_sent = random.choice(sensitive_files)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | From={user_from} | To={user_to} | FileAttached={file_sent} | Action=EmailSent | Unauthorized=True"
    
    # Guardar el evento en el archivo de log
    with open("logs/email_logs.txt", "a") as file:
        file.write(log_entry + "\n")


# Nuevas Funcionalidades Adicionales:

# Esta función genera accesos fuera del horario laboral (amenaza)
def generate_out_of_hours_access_event():
    users = ['user1', 'user2', 'user3']
    action = 'Access After Hours'
    location = 'Remote'
    user = random.choice(users)
    ip_address = f"192.168.1.{random.randint(1, 254)}"

    # Generar un timestamp fuera del horario laboral
    while True:
        log_time = generate_random_timestamp(start_time, end_time)
        current_time = log_time.time()
        
        # Verificar si el tiempo está fuera del rango laboral (antes del inicio o después del fin de horario laboral)
        if current_time < work_start or current_time > work_end:
            break

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | Location={location} | IP={ip_address} | OutOfHours=True"
    
    # Guardar el evento en el archivo de log
    with open("logs/out_of_hours_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Simular la instalación de software no autorizado
def generate_unauthorized_software_installation_event():
    users = ['user1', 'user2', 'user3']
    software = ['Unauthorized_Software_v1.0', 'Malware_Tool.exe', 'UnknownApp.pkg']
    user = random.choice(users)
    installed_software = random.choice(software)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action=Install Software | Software={installed_software} | Unauthorized=True"
    
    # Guardar el evento en el archivo de log
    with open("logs/software_installation_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Simular el uso de dispositivos externos (USB, discos duros externos)
def generate_usb_device_use_event():
    users = ['user1', 'user2', 'user3']
    device = ['USB_Drive_1', 'External_HDD_1', 'Portable_SSD']
    action = 'Copy to External Device'
    user = random.choice(users)
    file_transferred = random.choice(['Sensitive_File.txt', 'HR_Documents.docx', 'Financial_Report.xls'])
    device_used = random.choice(device)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | File={file_transferred} | Device={device_used} | Unauthorized=True"
    
    # Guardar el evento en el archivo de log
    with open("logs/usb_device_logs.txt", "a") as file:
        file.write(log_entry + "\n")


# Funciones para generar múltiples eventos de amenazas de cada tipo
def simulate_threat_logins(count=50):
    for _ in range(count):
        generate_threat_login_event()

def simulate_threat_file_access(count=50):
    for _ in range(count):
        generate_threat_file_access_event()

def simulate_threat_file_transfers(count=50):
    for _ in range(count):
        generate_threat_file_transfer_event()

def simulate_threat_emails(count=50):
    for _ in range(count):
        generate_threat_email_event()

def simulate_out_of_hours_access(count=20):
    for _ in range(count):
        generate_out_of_hours_access_event()

def simulate_unauthorized_software_installation(count=10):
    for _ in range(count):
        generate_unauthorized_software_installation_event()

def simulate_usb_device_use(count=15):
    for _ in range(count):
        generate_usb_device_use_event()
