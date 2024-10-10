
## Documentación del archivo `config.json`

Este archivo define la configuración del simulador de eventos de seguridad empresarial, estableciendo parámetros como los usuarios involucrados, la distribución de eventos, el horario laboral, y las configuraciones relacionadas con amenazas.

### Secciones del archivo

#### 1. **Usuarios (`users`)**

```json
"users": [
  {"email": "admin@company.com", "role": "admin"},
  {"email": "user1@company.com", "role": "employee"},
  {"email": "user2@company.com", "role": "employee"},
  {"email": "user3@company.com", "role": "contractor"}
]
```

- **Descripción**: Esta sección define los usuarios que participarán en la simulación.
  - **email**: Dirección de correo del usuario.
  - **role**: El rol que el usuario tiene dentro de la empresa (`admin`, `employee`, `contractor`).

#### 2. **Correos electrónicos externos (`external_emails`)**

```json
"external_emails": ["external_user@gmail.com", "external_server@external.com"]
```

- **Descripción**: Lista de correos electrónicos externos no autorizados. Se utilizan en las simulaciones de amenazas para representar correos a destinatarios fuera de la organización.

#### 3. **Archivos (`files`)**

```json
"files": {
  "valid": ["Project_Plan.docx", "Report_2024.pdf", "Client_List.csv"],
  "sensitive": ["Sensitive_File.txt", "HR_Documents.docx", "Financial_Report.xls"]
}
```

- **Descripción**: Define los archivos involucrados en la simulación, divididos en dos categorías:
  - **valid**: Archivos de uso común dentro de la empresa.
  - **sensitive**: Archivos sensibles que requieren mayor control de acceso.

#### 4. **Destinos externos (`external_destinations`)**

```json
"external_destinations": ["usb_drive_1", "cloud_storage_1", "external_server_1"]
```

- **Descripción**: Lista de destinos externos no autorizados donde podrían transferirse archivos sensibles (por ejemplo, almacenamiento en la nube o servidores externos). Se utilizan para simular transferencias de archivos hacia ubicaciones no seguras.

#### 5. **Distribución de eventos (`event_distribution`)**

```json
"event_distribution": {
  "login": {"valid": 100, "threat": 50},
  "file_access": {"valid": 100, "threat": 50},
  "file_transfer": {"valid": 50, "threat": 30},
  "emails": {"valid": 100, "threat": 30}
}
```

- **Descripción**: Define cuántos eventos válidos y cuántas amenazas se generarán para cada tipo de actividad.
  - **login**: Inicios de sesión (100 válidos y 50 intentos de amenazas).
  - **file_access**: Acceso a archivos (100 válidos y 50 accesos no autorizados).
  - **file_transfer**: Transferencias de archivos (50 válidas y 30 intentos no autorizados).
  - **emails**: Correos electrónicos (100 válidos y 30 correos con archivos enviados a externos).

#### 6. **Configuración del horario laboral (`time_settings`)**

```json
"time_settings": {
  "work_hours_start": "09:00",
  "work_hours_end": "17:00",
  "off_hours_activity_rate": 0.2
}
```

- **Descripción**: Establece el horario laboral y la tasa de actividad fuera de este.
  - **work_hours_start**: Hora de inicio de la jornada laboral.
  - **work_hours_end**: Hora de fin de la jornada laboral.
  - **off_hours_activity_rate**: Define el porcentaje de eventos que ocurren fuera del horario laboral. Por ejemplo, un valor de `0.2` indica que el 20% de los eventos ocurren fuera de las horas laborales.

#### 7. **Rango de fechas (`date_range`)**

```json
"date_range": {
  "start_time": "2024-01-01 00:00:00",
  "end_time": "2024-01-07 23:59:59"
}
```

- **Descripción**: Define el rango de fechas y horas en las que se generarán los eventos de la simulación.
  - **start_time**: Fecha y hora de inicio de la simulación.
  - **end_time**: Fecha y hora de finalización de la simulación.

#### 8. **Configuración de amenazas (`threat_settings`)**

```json
"threat_settings": {
  "privilege_escalation_success_rate": 0.3,
  "email_external_attachment_rate": 0.5
}
```

- **Descripción**: Configura parámetros específicos de amenazas para determinar el éxito de ciertas acciones maliciosas.
  - **privilege_escalation_success_rate**: La tasa de éxito para intentos de escalada de privilegios. Un valor de `0.3` indica que el 30% de los intentos de escalada serán exitosos.
  - **email_external_attachment_rate**: La tasa de éxito para el envío de archivos adjuntos a correos externos. Un valor de `0.5` indica que el 50% de los correos con archivos adjuntos a destinatarios externos se enviarán con éxito.

#### 9. **Distribución de intervalos (`interval_distribution`)**

```json
"interval_distribution": {
  "min_interval": 0.1,
  "max_interval": 0.5
}
```

- **Descripción**: Define los intervalos de tiempo entre eventos generados.
  - **min_interval**: El tiempo mínimo (en segundos) entre eventos consecutivos.
  - **max_interval**: El tiempo máximo (en segundos) entre eventos consecutivos.

---

### Resumen General

Este archivo `config.json` establece las reglas para generar eventos dentro del simulador de seguridad empresarial. Cada sección controla un aspecto diferente de la simulación, permitiendo personalizar el comportamiento de los eventos válidos y de amenazas. Al modificar los valores dentro de este archivo, se puede ajustar cómo se comporta el sistema en términos de seguridad, frecuencia de eventos y amenazas potenciales.

Para ajustar el simulador según los requisitos de una empresa específica, se recomienda modificar estos parámetros basados en el tamaño de la empresa, su nivel de riesgo y las necesidades de seguridad.
