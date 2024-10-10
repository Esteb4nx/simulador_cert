import random
from utils import generate_random_timestamp, start_time, end_time

# Esta función genera un intento fallido de inicio de sesión (amenaza)
def generate_threat_login_event():
    users = ['user1', 'user2', 'user3']  # Usuarios involucrados en la amenaza
    action = 'Failed'  # Intento fallido
    location = 'Remote'  # Ubicación remota
    user = random.choice(users)
    ip_address = f"192.168.1.{random.randint(1, 254)}"
    
    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | Location={location} | IP={ip_address}"
    
    # Guardar el evento en el archivo de log
    with open("logs/login_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Esta función genera un acceso no autorizado a archivos sensibles
def generate_threat_file_access_event():
    users = ['user1', 'user2', 'user3']
    actions = ['Read', 'Delete']  # Acciones posibles para amenazas
    sensitive_files = ['Sensitive_File.txt', 'HR_Documents.docx', 'Financial_Report.xls']  # Archivos sensibles involucrados
    user = random.choice(users)
    action = random.choice(actions)
    file_accessed = random.choice(sensitive_files)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | File={file_accessed} | Unauthorized=True"
    
    # Guardar el evento en el archivo de log
    with open("logs/file_access_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Esta función genera una transferencia no autorizada de archivos sensibles a destinos externos
def generate_threat_file_transfer_event():
    users = ['user1', 'user2', 'user3']
    actions = ['Upload', 'Download']  # Tipos de transferencia
    sensitive_files = ['Sensitive_File.txt', 'Company_Data.csv', 'Project_Plan.pdf']  # Archivos sensibles
    external_destinations = ['usb_drive_1', 'cloud_storage_1', 'external_server_1']  # Destinos no autorizados
    user = random.choice(users)
    action = random.choice(actions)
    destination = random.choice(external_destinations)
    file_transferred = random.choice(sensitive_files)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | File={file_transferred} | Destination={destination} | Unauthorized=True"
    
    # Guardar el evento en el archivo de log
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
