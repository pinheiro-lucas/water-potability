import streamlit as st
from sklearn.utils import resample
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from data import df_water_tratado

strategies = {
    "Floresta Aleatória": RandomForestClassifier,
    "Árvore de Decisão": DecisionTreeClassifier,
    "Regressão Logística": LogisticRegression,
}

st.title("Modelo")

strategy = str(st.selectbox("Selecione a estratégia", strategies.keys()))

from sklearn.model_selection import train_test_split

y = df_water_tratado["Potability"]
x = df_water_tratado.drop(columns=["Potability"], axis=1)

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3,
    random_state=42,
)

with st.spinner("Carregando..."):
    model = strategies[strategy](random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    if not "last_accuracy" in st.session_state:
        st.session_state["last_accuracy"] = 0

    if st.session_state["last_accuracy"] == 0:
        st.session_state["last_accuracy"] = accuracy

    delta = float(accuracy - st.session_state["last_accuracy"])
    st.session_state["last_accuracy"] = accuracy

    st.metric("Acurácia", f"{(accuracy * 100):.2f}%", f"{(delta * 100):.2f}%")
