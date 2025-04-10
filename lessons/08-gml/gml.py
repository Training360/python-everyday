import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


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
    ],  # Elírás javítva
    "PurchasedInsurance": ["No", "Yes", "Yes", "No", "No", "Yes", "Yes"],
}

df = pd.DataFrame(data)

# Label encoding
label_encoder_job = LabelEncoder()
label_encoder_insurance = LabelEncoder()

label_encoder_job.fit(df["JobType"])
label_encoder_insurance.fit(df["ExistingInsurance"])  # Elírás javítva

df["JobType"] = label_encoder_job.transform(df["JobType"])
df["ExistingInsurance"] = label_encoder_insurance.transform(
    df["ExistingInsurance"]
)  # Elírás javítva
df["PurchasedInsurance"] = label_encoder_insurance.fit_transform(
    df["PurchasedInsurance"]
)

X = df.drop("PurchasedInsurance", axis=1)
y = df["PurchasedInsurance"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Döntési fa modell finomhangolás
model = DecisionTreeClassifier(
    max_depth=3, min_samples_split=2, min_samples_leaf=1, random_state=42
)  # Paraméterek finomhangolása
model.fit(X_train, y_train)

# Modell kiértékelés
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Pontosság: {accuracy:.2f}")  # Helyesírás javítva

# Új ügyfél predikciója

new_customer = {
    "Age": [40],
    "Income": [80000],
    "JobType": label_encoder_job.transform(["Employee"]),
    "ExistingInsurance": label_encoder_insurance.transform(["No"]),
}

new_customer_df = pd.DataFrame(new_customer)
insurance_prediction = model.predict(new_customer_df)
print("Yes" if insurance_prediction[0] == 1 else "No")
