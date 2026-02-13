import streamlit as st
import os
import socket
import platform
import psutil

# 1. Configuración de la página (Debe ser lo primero)
st.set_page_config(
    page_title="Python Networking Lab", 
    page_icon="🌐", 
    layout="wide"
)

# 2. Estilos personalizados para mejorar la visualización
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Centro de Control: Python Networking Lab")
st.markdown("---")

# 3. Lógica para obtener la IP Local
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No requiere conexión real, solo detecta la interfaz activa
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# --- BARRA LATERAL: INFORMACIÓN DEL SISTEMA ---
with st.sidebar:
    st.header("📡 Conectividad")
    ip_actual = get_ip()
    st.success(f"**IP Local:** {ip_actual}")
    st.info(f"**Host:** {socket.gethostname()}")
    st.write(f"**SO:** {platform.system()} {platform.release()}")
    st.markdown("---")
    st.write("Panel de administración para gestión de archivos y telemetría de red.")

# --- SECCIÓN 1: MONITOR DE RECURSOS ---
st.header("📊 Monitor de Recursos (Hardware)")
col1, col2, col3 = st.columns(3)

# Datos de psutil
cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

col1.metric("Carga CPU", f"{cpu_usage}%")
col2.metric("Uso RAM", f"{ram_usage}%")
col3.metric("Espacio Disco", f"{disk_usage}%")

st.progress(ram_usage / 100, text="Ocupación de Memoria RAM")

# --- SECCIÓN 2: GESTOR DE ARCHIVOS Y SEGURIDAD ---
st.header("📁 Explorador de Archivos y Seguridad")

# Opción para pedir permiso o bloquear archivos (Basado en tus preferencias)
bloqueo_seguridad = st.checkbox(
    "Activar filtro de seguridad (Bloqueo de ejecutables .apk / .exe)", 
    value=True,
    help="Si está activo, impide la descarga de archivos potencialmente peligrosos."
)

ruta_actual = os.getcwd()
items = os.listdir(ruta_actual)

st.subheader("Contenido de la raíz del proyecto:")

for item in items:
    ruta_completa = os.path.join(ruta_actual, item)
    
    # Verificamos que sea un ARCHIVO para evitar el IsADirectoryError
    if os.path.isfile(ruta_completa):
        es_peligroso = item.endswith(('.apk', '.exe', '.msi'))
        
        col_file, col_btn = st.columns([3, 1])
        
        with col_file:
            if es_peligroso:
                st.warning(f"⚠️ {item} (Acceso Restringido)")
            else:
                st.write(f"📄 {item}")
                
        with col_btn:
            # Lógica de seguridad: si es peligroso y el filtro está activo, se bloquea
            if es_peligroso and bloqueo_seguridad:
                st.button("🚫 Bloqueado", key=f"lock_{item}", disabled=True)
            else:
                with open(ruta_completa, "rb") as f:
                    st.download_button(
                        label="Descargar", 
                        data=f, 
                        file_name=item, 
                        key=f"btn_{item}",
                        type="primary" if not es_peligroso else "secondary"
                    )
    
    # Si es una CARPETA, solo se muestra el nombre
    else:
        st.write(f"📁 **Directorio:** {item}")

# --- SECCIÓN 3: LOGS DE ACTIVIDAD ---
st.markdown("---")
st.header("📝 Consola de Eventos")
st.code(f"Servidor activo en: {ip_actual}\nEstado: Esperando peticiones de cliente...\nFiltro de seguridad: {'ACTIVO' if bloqueo_seguridad else 'DESACTIVADO'}")
