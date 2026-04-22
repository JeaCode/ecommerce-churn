import pandas as pd
from typing import Tuple
from sklearn.model_selection import train_test_split

TARGET = "Churn"

def cargar_informacion(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def seleccionar_cols_feature(df: pd.DataFrame)-> pd.DataFrame:
    feature_cols = [
    "Tenure",
    "PreferedOrderCat",
    "MaritalStatus",
    "Complain",
]
    return df[feature_cols]

def get_X_y(df: pd.DataFrame):
    df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
    X = seleccionar_cols_feature(df);
    y = df[TARGET]
    return X,y

def hacer_train_test_split(X,y,test_size=0.2,random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size= test_size,
        random_state = random_state,
        stratify = y
    )
    return X_train, X_test, y_train, y_test

def preproceso_features(X: pd.DataFrame):
    cat_cols = X.select_dtypes(include=["object","category"]).columns
    num_cols = X.select_dtypes(include=["number"]).columns

    X_cat = pd.get_dummies(X[cat_cols], drop_first=True)
    X_num = X[num_cols]

    X_procesado = pd.concat([X_num,X_cat],axis=1)

    return X_procesado

if __name__ == "__main__":
    df = cargar_informacion("../../data/data_ecommerce_customer_churn.csv")
    X, y = get_X_y(df)
    X_train, X_test, y_train, y_test = hacer_train_test_split(X, y)

    print("Train size: ",X_train.shape[0])
    print("Test size: ",X_test.shape[0])
    print("Total size: ",df.shape[0])

    print("\nChurn distribution overall:")
    print(y.value_counts(normalize=True)*100)

    print("\nChurn distribution train: ")
    print(y_train.value_counts(normalize=True)*100)
    
    print("\nChurn distribution test: ")
    print(y_test.value_counts(normalize=True)*100)

