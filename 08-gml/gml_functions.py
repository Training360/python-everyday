import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# RandomForestClassifier vs DecisionTreeClassifier összehasonlítása
# Mindkét modell döntési fa alapú, de jelentős különbségek vannak közöttük:

# RandomForestClassifier
#    Modul: sklearn.ensemble csomagban található
#    Működés: Több döntési fa együtteséből (ensemble) áll
#    Túltanulás elleni védelem: Erős, mivel minden fa más-más adatrészleten tanul
#    Pontosság: Általában magasabb
#    Számítási igény: Nagyobb
#    Értelmezhetőség: Nehezebb értelmezni a "fekete doboz" jelleg miatt
#    Használat: Komplex problémáknál, amikor a pontosság fontosabb
# DecisionTreeClassifier
#    Modul: sklearn.tree csomagban található
#    Működés: Egyetlen döntési fa
#    Túltanulás elleni védelem: Gyengébb, könnyen túltanul
#    Pontosság: Általában alacsonyabb
#    Számítási igény: Kisebb
#    Értelmezhetőség: Könnyen vizualizálható és értelmezhető
#    Használat: Egyszerűbb problémáknál, vagy amikor a modell értelmezhetősége fontos
# Melyik a jobb a biztosítási példához?
#    A RandomForestClassifier jobb választás ebben az esetben, mert:

# Jobban kezelné a biztosítási adatok komplexitását
# Robusztusabb az outlierek és zaj jelenlétében
# Pontosabb előrejelzést ad, ami ebben az üzleti esetben fontos
# A kódban már a RandomForestClassifier-t használod, ami megfelelő választás ehhez a problémához.


def create_data():
    """Teszt adatok létrehozása"""
    data = {
        "Age": [25, 30, 45, 50, 35, 40, 60],
        "Income": [50000, 60000, 100_000, 80000, 30000, 75000, 20000],
        "JobType": [
            "Employee",
            "Self-Employed",
            "Employee",
            "Retired",
            "Unemployed",
            "Employee",
            "Retired",
        ],
        "ExistingInsurance": [
            "No",
            "Yes",
            "No",
            "Yes",
            "No",
            "Yes",
            "No",
        ],
        "PurchasedInsurance": ["No", "Yes", "Yes", "No", "No", "Yes", "Yes"],
    }
    return pd.DataFrame(data)


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


def train_model(X_train, y_train, max_depth=3, random_state=42):
    """Döntési fa modell létrehozása és betanítása"""
    model = RandomForestClassifier(
        max_depth=max_depth,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=random_state,
    )
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Modell kiértékelése"""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Pontosság: {accuracy:.2f}")
    return accuracy


def predict_for_new_customer(
    model, age, income, job_type, existing_insurance, job_encoder, insurance_encoder
):
    """Új ügyfél biztosítási hajlandóságának előrejelzése"""
    new_customer = {
        "Age": [age],
        "Income": [income],
        "JobType": job_encoder.transform([job_type]),
        "ExistingInsurance": insurance_encoder.transform([existing_insurance]),
    }

    new_customer_df = pd.DataFrame(new_customer)
    insurance_prediction = model.predict(new_customer_df)
    result = "Yes" if insurance_prediction[0] == 1 else "No"
    print(f"Az új ügyfél biztosítást vásárolna? {result}")
    return result


def main():
    """Fő függvény, amely végrehajtja a teljes folyamatot"""
    # Teszt adatok létrehozása
    df = create_data()

    # Adatok előfeldolgozása
    X, y, job_encoder, insurance_encoder = preprocess_data(df)

    # Adatok felosztása
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Modell betanítása
    model = train_model(X_train, y_train)

    # Modell kiértékelése
    evaluate_model(model, X_test, y_test)

    # Új ügyfél előrejelzése
    predict_for_new_customer(
        model, 40, 80000, "Employee", "No", job_encoder, insurance_encoder
    )


if __name__ == "__main__":
    main()
