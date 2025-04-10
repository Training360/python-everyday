import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def prepare_data(df):
    # Címkézés az eredeti kategórikus adatok megtartásával
    label_encoder_job = LabelEncoder()
    label_encoder_insurance = LabelEncoder()

    # Kategórikus változók számszerűsítése, de az eredeti értékek megtartása
    job_encoded = label_encoder_job.fit_transform(df["JobType"])
    existing_insurance_encoded = label_encoder_insurance.fit_transform(
        df["ExistingInsurance"]
    )
    purchased_insurance_encoded = label_encoder_insurance.fit_transform(
        df["PurchasedInsurance"]
    )

    # Számszerűsített értékek hozzáadása a DataFrame-hez
    df["JobType_encoded"] = job_encoded
    df["ExistingInsurance_encoded"] = existing_insurance_encoded
    df["PurchasedInsurance_encoded"] = purchased_insurance_encoded

    return df


def plot_age_income_purchase_scatter(df, save_to_path):
    """Életkor vs jövedelem szórásdiagram a biztosításvásárlás függvényében"""
    plt.figure(figsize=(10, 6))

    # Két csoport kiválasztása: vásárolt és nem vásárolt biztosítást
    purchased = df[df["PurchasedInsurance"] == "Yes"]
    not_purchased = df[df["PurchasedInsurance"] == "No"]

    # Szórásdiagram készítése
    plt.scatter(
        not_purchased["Age"],
        not_purchased["Income"],
        color="red",
        alpha=0.5,
        label="Nem vásárolt",
    )
    plt.scatter(
        purchased["Age"], purchased["Income"], color="blue", alpha=0.5, label="Vásárolt"
    )
    plt.title("Biztosításvásárlás az életkor és jövedelem függvényében", fontsize=14)
    plt.xlabel("Életkor (év)")
    plt.ylabel("Jövedelem")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_to_path)
    plt.close()
