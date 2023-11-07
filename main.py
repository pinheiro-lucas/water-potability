import streamlit as st
import pandas as pd

base = pd.read_csv("data/water_potability.csv")

st.set_page_config(page_title="Potabilidade da água",
                   page_icon="💦",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={
                       'Get Help': 'https://github.com/pinheiro-lucas/water-potability',
                       'Report a bug': "https://github.com/pinheiro-lucas/water-potability",
                       'About': "Teste"
                   })

st.title("Potabilidade da água")
st.header(f"{len(base.index)} amostras carregadas")

tipo = st.selectbox("Selecione o tipo de amostras", ["Todas", "Potáveis", "Não potáveis"])
soma = base["Potability"].value_counts()

if tipo == "Todas":
    with st.spinner("Carregando gráfico..."):
        st.header("Quantidade de amostras")
        st.bar_chart({"Não potáveis": soma[0], "Potáveis": soma[1]})

with st.expander("Amostra dos dados brutos"):
    st.dataframe(base)

st.balloons()