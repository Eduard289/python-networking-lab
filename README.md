
 Python Connectivity & Networking Lab
 
Este repositorio es un entorno de pruebas técnico para el desarrollo de arquitecturas Cliente-Servidor utilizando Python. Se enfoca en la eficiencia de recursos, la transferencia de flujos de datos y la gestión remota de sistemas.

Especificaciones Técnicas y Recursos
Los scripts están diseñados bajo principios de baja latencia y consumo mínimo de memoria, optimizados para su ejecución tanto en servidores de alto rendimiento (VPS) como en entornos limitados (Android/Pydroid 3).

1. Sistema de Comunicación API (01-Flask-API)
Implementación de un servidor RESTful para la gestión de estados y telemetría.

Protocolo: HTTP/1.1.

Serialización: JSON (JavaScript Object Notation).

Gestión de Recursos: * RAM: ~30-50 MB en estado idle.

Concurrencia: Basada en el servidor WSGI integrado de Flask (Werkzeug).

Utilidad: Ideal para la monitorización de procesos en segundo plano, envío de señales de control (start/stop) y validación de permisos de descarga en tiempo real.

2. Servidor de Stream de Archivos (02-File-Server)
Servidor de archivos estáticos y flujos de bytes basado en la biblioteca estándar de Python.

Módulo: http.server y socketserver.

Manejo de I/O: Implementa una lectura secuencial de archivos.

Networking: * Detección dinámica de interfaces de red local (LAN).

Soporte para peticiones GET y descarga directa.

Utilidad: Configuración instantánea de un nodo de distribución multimedia o de paquetes (APKs) dentro de una red Wi-Fi sin dependencias externas.

Dependencias y Requisitos del Sistema
Para garantizar la portabilidad entre sistemas operativos (PC, VPS y Android), el proyecto se apoya tanto en la biblioteca estándar de Python como en módulos externos especializados.

Módulos Externos (Requieren instalación)
Flask (Versión 3.0+): Utilizado para el enrutamiento avanzado, la lógica del servidor y el manejo de la interfaz API.

Requests (Versión 2.31+): Empleado en el lado del cliente para realizar peticiones HTTP y validar las respuestas del servidor.

Módulos Nativos (Incluidos en Python)
Socket: Encargado de la resolución de direcciones IP, la detección de interfaces de red y la gestión de sockets TCP/IP de bajo nivel.

Http.server: Proporciona la infraestructura básica para la gestión y el servicio de peticiones de archivos físicos a través de la red.

Paquetes externos  pip install flask requests

Guía de Implementación y Utilidades
Escenario A: Administración Remota (PC/VPS)
Ejecutar server.py para abrir un canal de comunicación.

Utilizar client.py para consultar el estado del buffer o la salud del proceso sin necesidad de acceder vía SSH.

Escenario B: Interconexión Móvil (Android/Pydroid 3)
Ejecutar servidor_archivos.py en el dispositivo móvil.

Desde cualquier PC en la misma red, acceder a la IP proporcionada para extraer logs, configuraciones o archivos multimedia de forma inalámbrica.

Roadmap de Desarrollo (Próximas Mejoras)
Implementación de Pipe-Pass-Through: Adaptación de los servidores para procesar flujos de datos en fragmentos (chunks) de 1MB para evitar el uso del disco duro.

Filtro de Seguridad (Gatekeeper): Lógica de interrupción para archivos ejecutables (.apk, .exe) que requiera confirmación manual del administrador.

Auto-Healing Script: Sistema de reintento automático para conexiones perdidas entre el VPS y el cliente local.

Este proyecto se distribuye bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.

#Interfaz Gráfica# 
Este repositorio es compatible con Streamlit. Para lanzar el Dashboard visual, deberías:

Instala Streamlit: pip install streamlit

Ejecuta la app: streamlit run app.py

Utilidad: Permite acceder desde tu movil a todo el contenido del pc (ver, consultar, transferir archivos sin cables y en la distacia. Permite, además,  gestionar el servidor de archivos y monitorizar el tráfico de datos desde cualquier smartphone conectado a la red.
