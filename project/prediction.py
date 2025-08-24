import pandas as pd
from sklearn.preprocessing import LabelEncoder  # Kategórikus értékek számokká alakítása
from sklearn.model_selection import (
    train_test_split,
)  # Adatfelosztás tanító és tesztelő halmazokra
from sklearn.metrics import accuracy_score  # Modell pontosságának kiértékelése
from sklearn.ensemble import RandomForestClassifier  # Gépi tanulási algoritmus


def preprocess_data(df):
    """Adatok előfeldolgozása, kategórikus változók átalakítása"""
    # Két LabelEncoder objektum létrehozása a különböző kategórikus változókhoz
    label_encoder_job = LabelEncoder()  # Munkakör típusok kódolására
    label_encoder_insurance = LabelEncoder()  # Biztosítás értékek kódolására

    # A LabelEncoder "megtanulja" a lehetséges érték-kategóriákat
    label_encoder_job.fit(
        df["JobType"]
    )  # Pl. "Employee" -> 0, "Self-Employed" -> 1, stb.
    label_encoder_insurance.fit(df["ExistingInsurance"])  # Pl. "Yes" -> 1, "No" -> 0

    # Az eredeti értékek felülírása a kódolt számértékekkel
    df["JobType"] = label_encoder_job.transform(df["JobType"])
    df["ExistingInsurance"] = label_encoder_insurance.transform(df["ExistingInsurance"])
    # Itt újra tanítjuk és rögtön transzformáljuk is az értékeket
    df["PurchasedInsurance"] = label_encoder_insurance.fit_transform(
        df["PurchasedInsurance"]
    )

    # Jellemzők (X) és célváltozó (y) szétválasztása
    X = df.drop("PurchasedInsurance", axis=1)  # Minden oszlop, kivéve a célváltozó
    y = df["PurchasedInsurance"]  # A célváltozó (amit előrejelezni akarunk)

    return (
        X,
        y,
        label_encoder_job,
        label_encoder_insurance,
    )  # Visszaadjuk a kódolókat is későbbi használatra


def split_data(X, y, test_size=0.3, random_state=42):
    """Adatok felosztása tanító és teszt halmazra"""
    # Az adatokat két részre osztjuk: tanítási (70%) és tesztelési (30%)
    # A random_state biztosítja, hogy mindig ugyanúgy osszuk fel az adatokat
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train, n_estimators=100, random_state=42):
    """RandomForest modell létrehozása és betanítása"""
    # Random Forest modell létrehozása (100 döntési fa kombinációja)
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)  # Modell betanítása a tanító adatokkal
    return model


def evaluate_model(model, X_test, y_test):
    """Modell kiértékelése"""
    y_pred = model.predict(X_test)  # Előrejelzés a teszt adatokon
    accuracy = accuracy_score(y_test, y_pred)  # Pontosság számítása (helyes/összes)
    print(f"Pontosság: {accuracy:.2f}")  # Pontosság kiírása (pl. 0.86 = 86%)
    return accuracy


def tranform_new_customer(new_customer, job_encoder, insurance_encoder):
    """Új ügyfél adatait átalakítja a modell bemenetéhez"""
    # A nyers ügyfél adatait DataFrame formátumba alakítjuk
    transformed_customer = {
        "Age": [
            new_customer["Age"],  # Életkor (szám, nem kell kódolni)
        ],
        "Income": [new_customer["Income"]],  # Jövedelem (szám, nem kell kódolni)
        "JobType": job_encoder.transform(
            [new_customer["JobType"]]
        ),  # Szöveget számmá kódolja
        "ExistingInsurance": insurance_encoder.transform(
            [new_customer["ExistingInsurance"]]  # Szöveget számmá kódolja
        ),
    }

    # DataFrame létrehozása a modell számára érthető formátumban
    new_customer_df = pd.DataFrame(transformed_customer)
    return new_customer_df


def predict(model, new_customer):
    """Új ügyfél biztosítási hajlandóságának előrejelzése"""
    new_customer_df = pd.DataFrame(new_customer)  # Biztosítjuk hogy DataFrame
    insurance_prediction = model.predict(new_customer_df)  # Előrejelzés készítése
    result = "Yes" if insurance_prediction[0] == 1 else "No"  # 1 -> "Yes", 0 -> "No"
    print(f"Az új ügyfél biztosítást vásárolna? {result}")
    return result


def predict_complete_pipeline(df, new_customer):
    """Teljes előrejelzési folyamat betanításától a predikcióig"""
    # 1. Előfeldolgozás: adatok kódolása és szétválasztása
    X, y, job_encoder, insurance_encoder = preprocess_data(df)

    # 2. Adatok felosztása tanító és teszt halmazokra
    X_train, X_test, y_train, y_test = split_data(X, y)

    # 3. Modell betanítása a tanító adatokon
    model = train_model(X_train, y_train)

    # 4. Modell kiértékelése a teszt adatokon
    evaluate_model(model, X_test, y_test)

    # 5. Új ügyfél adatainak átalakítása
    transformed_customer = tranform_new_customer(
        new_customer, job_encoder, insurance_encoder
    )

    # 6. Előrejelzés az új ügyfélre
    return predict(model, transformed_customer)
