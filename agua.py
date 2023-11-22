import pandas as pd
from sklearn.utils import resample
from sklearn.utils import shuffle

df_agua_null = pd.read_csv("data/water_potability.csv", sep=",")

df_agua = df_agua_null
df_agua.fillna(df_agua.mean(), inplace=True)

agua_potavel_balanceado = resample(
    df_agua[df_agua["Potability"] == 1],
    replace=True,
    n_samples=1998,
)
df_agua_balanceado = pd.concat(
    [
        df_agua[df_agua["Potability"] == 0],
        agua_potavel_balanceado,
    ]
)
df_agua_balanceado = shuffle(df_agua_balanceado)
df_agua_balanceado = pd.DataFrame(df_agua_balanceado)
