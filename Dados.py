import streamlit as st
import altair as alt
from agua import df_agua

base = df_agua
medidas = {
    "ph": "Quantidade de PH",
    "Hardness": "Quantidade de cálcio e magnésio dissolvido",
    "Solids": "Quantidade de partículas sólidas",
    "Chloramines": "Quantidade de derivados de amônia e aminas orgânicas",
    "Sulfate": "Quantidade de sulfato",
    "Conductivity": "Condutividade",
    "Organic_carbon": "Quantidade de carbono",
    "Trihalomethanes": "Quantidade de trihalometanos (THMs)",
    "Turbidity": "Turbidez",
}

st.set_page_config(
    page_title="Potabilidade da água",
    page_icon="💦",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "https://github.com/pinheiro-lucas/water-potability",
    },
)

st.title("Potabilidade da água")
st.header(f"{len(base.index)} amostras carregadas")

tipo = st.selectbox(
    "Selecione o tipo de amostras", ["Todas", "Potáveis", "Não potáveis"]
)
soma = base["Potability"].value_counts()

if tipo == "Todas":
    with st.spinner("Carregando gráfico..."):
        st.header("Quantidade de amostras")
        col1, col2, col3 = st.columns(3)
        medidas1 = dict(list(medidas.items())[:3])
        medidas2 = dict(list(medidas.items())[3:6])
        medidas3 = dict(list(medidas.items())[6:])

        with col1:
            for k, v in medidas1.items():
                st.altair_chart(
                    alt.Chart(base)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col2:
            for k, v in medidas2.items():
                st.altair_chart(
                    alt.Chart(base)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col3:
            for k, v in medidas3.items():
                st.altair_chart(
                    alt.Chart(base)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

if tipo == "Potáveis":
    potaveis = base[base["Potability"] == 1]
    st.header(f"{len(potaveis.index)} amostras potáveis")

    with st.spinner("Carregando gráfico..."):
        st.header("Quantidade de amostras")
        col1, col2, col3 = st.columns(3)
        medidas1 = dict(list(medidas.items())[:3])
        medidas2 = dict(list(medidas.items())[3:6])
        medidas3 = dict(list(medidas.items())[6:])

        with col1:
            for k, v in medidas1.items():
                st.altair_chart(
                    alt.Chart(potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col2:
            for k, v in medidas2.items():
                st.altair_chart(
                    alt.Chart(potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col3:
            for k, v in medidas3.items():
                st.altair_chart(
                    alt.Chart(potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

if tipo == "Não potáveis":
    nao_potaveis = base[base["Potability"] == 0]
    st.header(f"{len(nao_potaveis.index)} amostras não potáveis")

    with st.spinner("Carregando gráfico..."):
        st.header("Quantidade de amostras")
        col1, col2, col3 = st.columns(3)
        medidas1 = dict(list(medidas.items())[:3])
        medidas2 = dict(list(medidas.items())[3:6])
        medidas3 = dict(list(medidas.items())[6:])

        with col1:
            for k, v in medidas1.items():
                st.altair_chart(
                    alt.Chart(nao_potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col2:
            for k, v in medidas2.items():
                st.altair_chart(
                    alt.Chart(nao_potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

        with col3:
            for k, v in medidas3.items():
                st.altair_chart(
                    alt.Chart(nao_potaveis)
                    .mark_bar()
                    .encode(alt.X(k, bin=True, title=v), y=alt.Y("count()", title=""))
                    .interactive()
                )

with st.expander("Amostra dos dados brutos"):
    st.dataframe(base, use_container_width=True)
