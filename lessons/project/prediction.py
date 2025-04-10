import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


def preprocess_data(df):
    """Adatok előfeldolgozása, kategórikus változók átalakítása"""
    # Label encoding
    label_encoder_job = LabelEncoder()
    label_encoder_insurance = LabelEncoder()

    label_encoder_job.fit(df["JobType"])
    label_encoder_insurance.fit(df["ExistingInsurance"])

    df["JobType"] = label_encoder_job.transform(df["JobType"])
    df["ExistingInsurance"] = label_encoder_insurance.transform(df["ExistingInsurance"])
    df["PurchasedInsurance"] = label_encoder_insurance.fit_transform(
        df["PurchasedInsurance"]
    )

    X = df.drop("PurchasedInsurance", axis=1)
    y = df["PurchasedInsurance"]

    return X, y, label_encoder_job, label_encoder_insurance


def split_data(X, y, test_size=0.3, random_state=42):
    """Adatok felosztása tanító és teszt halmazra"""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train, n_estimators=100, random_state=42):
    """RandomForest modell létrehozása és betanítása"""
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Modell kiértékelése"""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Pontosság: {accuracy:.2f}")
    return accuracy


def tranform_new_customer(new_customer, job_encoder, insurance_encoder):
    """Új ügyfél adatait átalakítja a modell bemenetéhez"""
    transformed_customer = {
        "Age": [
            new_customer["Age"],
        ],
        "Income": [new_customer["Income"]],
        "JobType": job_encoder.transform([new_customer["JobType"]]),
        "ExistingInsurance": insurance_encoder.transform(
            [new_customer["ExistingInsurance"]]
        ),
    }

    new_customer_df = pd.DataFrame(transformed_customer)
    return new_customer_df


# Az első predict függvény marad ahogy van
def predict(model, new_customer):
    """Új ügyfél biztosítási hajlandóságának előrejelzése"""
    new_customer_df = pd.DataFrame(new_customer)
    insurance_prediction = model.predict(new_customer_df)
    result = "Yes" if insurance_prediction[0] == 1 else "No"
    print(f"Az új ügyfél biztosítást vásárolna? {result}")
    return result


# A második függvényt nevezzük át megfelelőbben
def predict_complete_pipeline(df, new_customer):
    """Teljes előrejelzési folyamat betanításától a predikcióig"""
    X, y, job_encoder, insurance_encoder = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    transformed_customer = tranform_new_customer(
        new_customer, job_encoder, insurance_encoder
    )
    return predict(model, transformed_customer)
