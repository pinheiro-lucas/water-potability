import pandas as pd
import streamlit as st
from sklearn.utils import resample
from sklearn.utils import shuffle
from sklearn.metrics import accuracy_score

df_water = pd.read_csv("data/water_potability.csv", sep=",")

df_water_tratado = df_water
df_water_tratado.fillna(df_water_tratado.mean(), inplace=True)
potable_water_balanced = resample(
    df_water_tratado[df_water_tratado["Potability"] == 1], replace=True, n_samples=1998
)
df_water_tratado = pd.concat(
    [
        df_water_tratado[df_water_tratado["Potability"] == 0],
        potable_water_balanced,
    ]
)
df_water_tratado = shuffle(df_water_tratado)
df_water_tratado["Potability"].value_counts()
df_water_tratado.corr()["Potability"].sort_values()
df_water_tratado = pd.DataFrame(df_water_tratado)
