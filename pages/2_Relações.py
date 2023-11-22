import streamlit as st
import altair as alt
from agua import df_agua

st.title("Relações")

base = df_agua
corr = base.corr().reset_index().melt("index")

col1, col2 = st.columns(2)

heatmap = alt.Chart(corr).encode(
    x="index:N",
    y="variable:N",
).mark_rect().encode(
    color="value:Q"
)
text = alt.Chart(base).mark_text(baseline="middle").encode(
    x="index:N",
    y="variable:N",
    text=alt.Text("value:Q", format=".2f"),
    color=alt.condition(
        alt.datum.value > 0.5,
        alt.value("white"),
        alt.value("black")
    ),
)

with col1:
    st.header("Matriz de correlação")
    st.altair_chart(heatmap + text)

histogram_chart = alt.Chart(base).mark_bar().encode(
    alt.X('ph:Q', bin=True),
    alt.Y('count():Q')
).interactive()

with col2:
    st.header("Histograma de pH")
    st.altair_chart(histogram_chart)
