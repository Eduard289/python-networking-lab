import streamlit as st
import os
import socket
import platform
import psutil

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Python Networking Lab", 
    page_icon="🌐", 
    layout="wide"
)

# Estilos personalizados para un acabado profesional
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    footer {visibility: hidden;}
    .footer-text {
        text-align: center;
        color: #9ea0a4;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Centro de Control: Python Networking Lab")
st.markdown("---")

# 2. LÓGICA DE RED
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

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.header("📡 Conectividad")
    ip_actual = get_ip()
    st.success(f"**IP Servidor:** {ip_actual}")
    st.info(f"**Host:** {socket.gethostname()}")
    
    st.markdown("---")
    st.write("Gestión remota de archivos y monitorización de hardware.")
    
    # SECCIÓN ROADMAP: PRÓXIMA IMPLEMENTACIÓN
    st.markdown("---")
    st.subheader("🚀 Roadmap")
    st.warning("Próximas fechas desarrollaremos **App Nativa** con esta herramienta.")
    st.caption("Pronto disponible en repositorios Open Source (F-Droid/GitHub).")
    
    st.markdown("---")
    st.write(f"**SO:** {platform.system()}")

# --- SECCIÓN 1: MONITOR DE RECURSOS (HARDWARE) ---
st.header("📊 Monitor de Recursos")
col1, col2, col3 = st.columns(3)

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

col1.metric("Carga CPU", f"{cpu_usage}%")
col2.metric("Uso RAM", f"{ram_usage}%")
col3.metric("Espacio Disco", f"{disk_usage}%")
st.progress(ram_usage / 100, text="Ocupación de Memoria RAM")

# --- SECCIÓN 2: GESTIÓN DE ARCHIVOS (EXPLORADOR Y SUBIDA) ---
st.header("📁 Gestión de Archivos")

tab1, tab2 = st.tabs(["📂 Explorador / Descargas", "📤 Subir al Servidor"])

ruta_actual = os.getcwd()

with tab1:
    st.subheader("Archivos en el PC/Servidor")
    # Filtro de seguridad para archivos sensibles (como APKs) [cite: 2026-02-13]
    bloqueo_seguridad = st.checkbox("Bloqueo de seguridad (.apk / .exe)", value=True)
    
    items = os.listdir(ruta_actual)
    for item in items:
        ruta_completa = os.path.join(ruta_actual, item)
        
        if os.path.isfile(ruta_completa):
            es_peligroso = item.endswith(('.apk', '.exe', '.msi'))
            col_f, col_b = st.columns([3, 1])
            
            with col_f:
                if es_peligroso:
                    st.warning(f"⚠️ {item} (Acceso Restringido)")
                else:
                    st.write(f"📄 {item}")
            
            with col_b:
                if es_peligroso and bloqueo_seguridad:
                    st.button("🚫", key=f"lock_{item}", disabled=True, help="Descarga bloqueada por seguridad")
                else:
                    with open(ruta_completa, "rb") as f:
                        st.download_button("Descargar", f, file_name=item, key=f"btn_{item}")
        else:
            st.write(f"📁 **Directorio:** {item}")

with tab2:
    st.subheader("Enviar archivo al ordenador")
    st.info("Sube archivos desde tu móvil para guardarlos en el servidor.")
    archivo_subido = st.file_uploader("Seleccionar archivo", type=None)
    
    if archivo_subido is not None:
        try:
            with open(os.path.join(ruta_actual, archivo_subido.name), "wb") as f:
                f.write(archivo_subido.getbuffer())
            st.success(f"✅ ¡Archivo '{archivo_subido.name}' guardado correctamente!")
            if st.button("Actualizar Explorador"):
                st.rerun()
        except Exception as e:
            st.error(f"Error al guardar: {e}")

# --- SECCIÓN 3: LOGS Y CONSOLA ---
st.markdown("---")
st.code(f"Estado: Activo\nIP de acceso: {ip_actual}\nFiltro de Seguridad: {'ACTIVO' if bloqueo_seguridad else 'DESACTIVADO'}")

# --- PIE DE PÁGINA (FOOTER) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <div class='footer-text'>
        Desarrollado por <b>Jose Luis Asenjo</b><br>
        Esta app permite la gestión remota de archivos entre dispositivos.<br><br>
        Para cualquier duda: <a href='mailto:asenjo.jose@hotmail.com'>asenjo.jose@hotmail.com</a>
    </div>
    """, 
    unsafe_allow_html=True
)
