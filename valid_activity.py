import random
from utils import generate_random_timestamp, start_time, end_time

# Esta función genera un evento válido de inicio de sesión
def generate_valid_login_event():
    users = ['admin@company.com', 'user1@company.com', 'user2@company.com', 'user3@company.com']  # Usuarios definidos en config.json
    action = 'Success'  # Acción exitosa
    location = 'Local'  # Localización (en la empresa)
    user = random.choice(users)  # Seleccionar un usuario aleatorio
    ip_address = f"192.168.1.{random.randint(1, 254)}"  # Dirección IP simulada
    
    # Generar un timestamp aleatorio dentro del rango definido
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | Location={location} | IP={ip_address}"
    
    # Guardar el evento en el archivo de log correspondiente
    with open("logs/login_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Esta función genera un evento válido de acceso a archivos
def generate_valid_file_access_event():
    users = ['admin', 'user1', 'user2', 'user3']  # Usuarios involucrados
    actions = ['Read', 'Write']  # Acciones posibles
    files = ['Project_Plan.docx', 'Report_2024.pdf', 'Client_List.csv']  # Archivos válidos
    user = random.choice(users)
    action = random.choice(actions)
    file_accessed = random.choice(files)

    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | User={user} | Action={action} | File={file_accessed}"
    
    # Guardar el evento en el archivo de log
    with open("logs/file_access_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Esta función genera un evento válido de envío de correos electrónicos internos
def generate_valid_email_event():
    users = ['admin@company.com', 'user1@company.com', 'user2@company.com', 'user3@company.com']  # Usuarios internos
    subjects = ['Meeting Update', 'Project Plan', 'Report Submission', 'Client Feedback']  # Asuntos de correo
    user_from = random.choice(users)
    user_to = random.choice([user for user in users if user != user_from])  # Asegurarse de que el remitente y destinatario no sean el mismo
    subject = random.choice(subjects)
    
    # Generar un timestamp aleatorio
    log_time = generate_random_timestamp(start_time, end_time)

    # Crear el registro del evento
    log_entry = f"{log_time} | From={user_from} | To={user_to} | Subject={subject} | Action=EmailSent"
    
    # Guardar el evento en el archivo de log
    with open("logs/email_logs.txt", "a") as file:
        file.write(log_entry + "\n")

# Funciones para generar múltiples eventos válidos de cada tipo
def simulate_valid_logins(count=100):
    for _ in range(count):
        generate_valid_login_event()

def simulate_valid_file_access(count=100):
    for _ in range(count):
        generate_valid_file_access_event()

def simulate_valid_emails(count=100):
    for _ in range(count):
        generate_valid_email_event()
