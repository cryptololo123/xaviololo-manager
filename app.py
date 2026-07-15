import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Xaviololo Manager", page_icon="🚀", layout="wide")

st.title("🚀 Xaviololo Manager")
st.markdown("**Gestor para @xaviololo** — XRP, Bitcoin y finanzas en España. Sin humo.")

st.sidebar.header("Opciones")
opcion = st.sidebar.radio("Qué quieres hacer:", ["📊 Analizar CSV", "✍️ Generar Posts", "📈 Dashboard"])

if opcion == "📊 Analizar CSV":
    st.header("📊 Analizar tus CSV de Buffer / X")
    uploaded_file = st.file_uploader("Sube tu CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Cargado: {len(df)} filas")
        st.dataframe(df.head(10))

elif opcion == "✍️ Generar Posts":
    st.header("✍️ Generador de Posts")
    tema = st.selectbox("Tema del post:", ["XRP", "Bitcoin", "Finanzas España", "Inflación/Euríbor", "HODL y paciencia", "Otro"])
    extra = st.text_area("Instrucciones extra (opcional):", placeholder="Ej: tono motivador, mencionar familia...")
    if st.button("🚀 Generar Post"):
        st.text_area("Prompt listo para Grok:", f"Genera un post en estilo @xaviololo sobre {tema}. {extra}", height=300)

else:
    st.header("📈 Dashboard")
    st.info("Sube un CSV en la sección Analizar para ver estadísticas.")

st.sidebar.markdown("---\n**Xaviololo Manager v0.1** para @xaviololo")