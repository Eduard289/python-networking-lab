import streamlit as st
import os
import socket
import platform
import psutil # Necesitarás: pip install psutil

# Configuración de la página
st.set_page_config(page_title="Python Networking Lab", page_icon="🌐", layout="wide")

st.title("🌐 Centro de Control: Python Networking Lab")
st.markdown("---")

# --- BARRA LATERAL: INFORMACIÓN DE RED ---
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

with st.sidebar:
    st.header("📡 Información de Conexión")
    ip_actual = get_ip()
    st.success(f"**IP Local:** {ip_actual}")
    st.info(f"**Host:** {socket.gethostname()}")
    st.write(f"**Sistema:** {platform.system()}")
    st.markdown("---")
    st.write("Usa esta IP en el navegador de tu móvil para acceder al panel.")

# --- SECCIÓN 1: MONITOR DE RECURSOS (Para tu VPS/PC) ---
st.header("📊 Monitor de Recursos en Tiempo Real")
col1, col2, col3 = st.columns(3)

cpu_usage = psutil.cpu_percent()
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

col1.metric("CPU", f"{cpu_usage}%")
col2.metric("RAM", f"{ram_usage}%")
col3.metric("Disco", f"{disk_usage}%")

st.progress(ram_usage / 100, text="Carga de Memoria RAM")

# --- SECCIÓN 2: GESTOR DE ARCHIVOS Y SEGURIDAD ---
st.header("📁 Explorador de Archivos y Seguridad")

# Filtro de Seguridad (Tu idea de los APKs)
bloqueo_seguridad = st.checkbox("Activar filtro de seguridad (Bloqueo de ejecutables .apk / .exe)", value=True)

ruta_actual = os.getcwd()
archivos = os.listdir(ruta_actual)

for item in archivos:
    es_peligroso = item.endswith(('.apk', '.exe', '.msi'))
    
    col_file, col_btn = st.columns([3, 1])
    
    with col_file:
        if es_peligroso:
            st.warning(f"⚠️ {item} (Archivo ejecutable detectado)")
        else:
            st.write(f"📄 {item}")
            
    with col_btn:
        if es_peligroso and bloqueo_seguridad:
            st.button("Bloqueado", key=item, disabled=True)
        else:
            with open(os.path.join(ruta_actual, item), "rb") as f:
                st.download_button("Descargar", f, file_name=item, key=f"btn_{item}")

# --- SECCIÓN 3: LOGS DE ACTIVIDAD ---
st.header("📝 Registro de Actividad")
st.text_area("Eventos del servidor:", "Servidor iniciado correctamente...\nEsperando conexiones de clientes...", height=100)
