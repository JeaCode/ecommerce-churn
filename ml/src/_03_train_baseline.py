# ml/src/03_train_baseline.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

from ml.src._02_preprocessing import cargar_informacion, get_X_y, preproceso_features  # o ajusta según tu estructura

def train_baseline_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    
    df = cargar_informacion("data/data_ecommerce_customer_churn.csv")
    X, y = get_X_y(df)
    X_procesado = preproceso_features(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_procesado, y, test_size=0.2, random_state=42, stratify=y
    )

    model = train_baseline_model(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Accuracy:", acc)
    print("F1:", f1)
    print("Confusion matrix:\n", cm)
    print("\nClassification report:\n", classification_report(y_test, y_pred))