import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from agua import df_agua_balanceado, df_agua
from sklearn.model_selection import train_test_split

estrategias = {
    "Floresta Aleatória": RandomForestClassifier,
    "Árvore de Decisão": DecisionTreeClassifier,
    "Regressão Logística": LogisticRegression,
}

st.title("Modelo")

estrategia = str(st.selectbox("Selecione a estratégia", estrategias.keys()))
balanceado = st.checkbox("Dados balanceados", True)

with st.spinner("Carregando..."):
    df = df_agua_balanceado if balanceado else df_agua

    y = df["Potability"]
    x = df.drop(columns=["Potability"], axis=1)

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x,
        y,
        test_size=0.3,
        random_state=42,
    )

    modelo = estrategias[estrategia](random_state=42)
    modelo.fit(x_treino, y_treino)

    y_pred = modelo.predict(x_teste)
    acuracia = accuracy_score(y_teste, y_pred)

    if not "ultima_acuracia" in st.session_state:
        st.session_state["ultima_acuracia"] = acuracia

    delta = float(acuracia - st.session_state["ultima_acuracia"])
    st.session_state["ultima_acuracia"] = acuracia

    st.metric("Acurácia", f"{(acuracia * 100):.2f}%", f"{(delta * 100):.2f}%")
