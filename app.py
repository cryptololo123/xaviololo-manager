import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Xaviololo Manager",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Xaviololo Manager")
st.markdown("**Gestor para @xaviololo** — XRP, Bitcoin y finanzas en España. Sin humo.")

# Sidebar
st.sidebar.header("Opciones")
opcion = st.sidebar.radio(
    "Qué quieres hacer:",
    ["📊 Analizar CSV", "✍️ Generar Posts", "📈 Dashboard"]
)

# ======================
# ANALIZAR CSV
# ======================
if opcion == "📊 Analizar CSV":
    st.header("📊 Analizar tus CSV de Buffer / X")
    uploaded_file = st.file_uploader("Sube tu CSV de Buffer o X Analytics", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ CSV cargado: {len(df)} filas")
        st.dataframe(df.head(10))
        st.info("Más análisis automáticos (mejores horarios, temas, etc.) vendrán pronto.")

# ======================
# GENERADOR DE POSTS (MEJORADO)
# ======================
elif opcion == "✍️ Generar Posts":
    st.header("✍️ Generador de Posts")
    st.markdown("Crea contenido en tu estilo @xaviololo")
    
    tema = st.selectbox(
        "Tema del post:",
        ["XRP", "Bitcoin", "Finanzas personales España", "Inflación/Euríbor", "HODL y paciencia", "Familia + Crypto", "Otro"]
    )
    
    tipo = st.radio("Tipo de contenido:", ["Tweet simple", "Hilo (3-5 tweets)", "Idea para carrusel"])
    
    extra = st.text_area(
        "Instrucciones extra (opcional):",
        placeholder="Ej: tono motivador, mencionar familia, hablar de DCA, crítica suave al sistema...",
        height=100
    )
    
    if st.button("🚀 Generar Post"):
        with st.spinner("Generando prompt optimizado..."):
            prompt = f"""
Eres Xavi de @xaviololo. Escribe un post en español sobre **{tema}**.

Estilo:
- Educativo y sin humo
- Cercano, como hablando con amigos
- Toque personal (familia, vida real en España)
- Mensaje de paciencia, HODL, educación financiera