import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Xaviololo Manager",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Xaviololo Manager")
st.markdown("**Gestor para @xaviololo** — XRP, Bitcoin y finanzas en España. Sin humo.")

st.sidebar.header("Opciones")
opcion = st.sidebar.radio(
    "Qué quieres hacer:",
    ["📊 Analizar CSV", "✍️ Generar Posts", "📈 Dashboard"]
)

if opcion == "📊 Analizar CSV":
    st.header("📊 Analizar tus CSV de Buffer / X")
    uploaded_file = st.file_uploader("Sube tu CSV de Buffer o X Analytics", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ CSV cargado: {len(df)} filas")
        st.dataframe(df.head(10))

elif opcion == "✍️ Generar Posts":
    st.header("✍️ Generador de Posts")
    st.markdown("Crea contenido en tu estilo @xaviololo")
    
    tema = st.selectbox("Tema del post:", ["XRP", "Bitcoin", "Finanzas personales España", "Inflación/Euríbor", "HODL y paciencia", "Familia + Crypto", "Otro"])
    tipo = st.radio("Tipo de contenido:", ["Tweet simple", "Hilo (3-5 tweets)", "Idea para carrusel"])
    extra = st.text_area("Instrucciones extra (opcional):", placeholder="Ej: tono motivador, mencionar familia...", height=100)
    
    if st.button("🚀 Generar Post"):
        prompt = f"""Eres Xavi de @xaviololo. Escribe un post en español sobre {tema}.

Estilo: educativo, sin humo, cercano, toque personal (familia, España).
Tipo: {tipo}
Extra: {extra}

Genera SOLO el texto del post listo para Buffer."""
        
        st.text_area("📋 Prompt listo para Grok:", prompt, height=300)
        st.success("¡Copia este prompt y pégalo en Grok!")

else:
    st.header("📈 Dashboard")
    st.info("Sube un CSV para ver métricas.")

st.sidebar.markdown("---")
st.sidebar.markdown("**Xaviololo Manager v0.2**")