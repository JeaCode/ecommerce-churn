import pandas as pd
from typing import Tuple

TARGET = "Churn"
def separar_features_target_df(df: pd.DataFrame)->Tuple[pd.DataFrame,pd.Series]:
    y = df[TARGET]
    X = df.drop(columns=[TARGET])
    return X,y

def cargar_informacion(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

COLS_FEATURES = [
    "Tenure",
    "PreferedOrderCat",
    "MaritalStatus",
    "Complain",
]

def seleccionar_cols_feature(df: pd.DataFrame)-> pd.DataFrame:
    return df[COLS_FEATURES]

def preprocesamiento(df: pd.DataFrame)->Tuple[pd.DataFrame,pd.Series]:
    y = df[TARGET]
    X = seleccionar_cols_feature(df)
    return X,y

if __name__ == "__main__":
    df = cargar_informacion("data/data_ecommerce_customer_churn.csv")
    X, y = separar_features_target_df(df)
    print("X shape: ",X.shape)
    print("y shape: ",y.shape)

