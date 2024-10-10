
# Simulador de Eventos de Seguridad Empresarial

## Descripción General

El **Simulador de Eventos de Seguridad Empresarial** es un software diseñado para generar y monitorear eventos de seguridad en un entorno simulado de una empresa pequeña. Este simulador puede crear registros tanto de actividades válidas como de intentos de amenazas internas, como inicios de sesión fallidos, accesos no autorizados a archivos sensibles y transferencias de datos no permitidas.

## Objetivo del Software

Este simulador está diseñado para servir como una herramienta que permita a las organizaciones:
- Simular diferentes tipos de eventos de seguridad.
- Probar sistemas de monitoreo en un entorno controlado.
- Generar datos históricos para analizar la respuesta ante amenazas internas y actividades normales.

## Principales Funcionalidades

1. **Generación de eventos válidos:**
   - Inicios de sesión exitosos.
   - Accesos a archivos normales.
   - Correos electrónicos internos válidos.

2. **Generación de amenazas internas:**
   - Intentos de inicio de sesión fallidos.
   - Accesos no autorizados a archivos sensibles.
   - Transferencias no autorizadas de archivos sensibles.
   - Correos electrónicos con archivos sensibles enviados a direcciones externas.

## Configuración

El comportamiento del simulador puede personalizarse a través de un archivo de configuración (`config.json`), que define:
- El número de eventos válidos y amenazas a simular.
- Los usuarios y archivos involucrados en la simulación.
- Las fechas y tiempos de los eventos generados.
- La tasa de éxito o fallo de ciertas actividades sospechosas, como la escalada de privilegios o el envío de archivos externos.

## Aplicación del Simulador

Este software es útil para equipos de TI y seguridad en organizaciones que buscan:
- Probar sistemas de detección de amenazas en un entorno simulado.
- Analizar el comportamiento de seguridad en una empresa pequeña.
- Entrenar a equipos de respuesta ante incidentes con escenarios simulados.
