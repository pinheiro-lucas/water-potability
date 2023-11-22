import streamlit as st
import altair as alt
from agua import df_agua

st.title("Gráficos de dispersão")
st.header("Relação entre variáveis e potabilidade")

base = df_agua
corr = base.corr().reset_index().melt("index")

variaveis = ['Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Dividir as variáveis em grupos de 3 para colocar em cada coluna
grupos_variaveis = [variaveis[i:i+3] for i in range(0, len(variaveis), 3)]

for grupo in grupos_variaveis:
    for i in range(len(grupo)):
        for j in range(i+1, len(grupo)):
            scatter_chart = alt.Chart(base).mark_circle().encode(
                x=alt.X(grupo[i] + ':Q', title=grupo[i]),
                y=alt.Y(grupo[j] + ':Q', title=grupo[j]),
            ).interactive()

            st.header(f"{grupo[i]} x {grupo[j]}")
            st.altair_chart(scatter_chart)