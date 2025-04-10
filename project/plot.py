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


def plot_age_distribution(df, save_to_path):
    """Életkor szerinti biztosítási eloszlás"""
    plt.figure(figsize=(12, 6))

    # Adatok csoportosítása életkor szerint
    age_groups = df.groupby("Age")["PurchasedInsurance"].agg(
        Total="count",  # Összes ember ebben a korban
        Purchased=lambda x: (x == "Yes").sum(),  # Ebből hányan vásároltak biztosítást
    )

    # Diagram létrehozása
    plt.bar(
        age_groups.index, age_groups["Total"], color="lightgray", label="Összes ügyfél"
    )
    plt.bar(
        age_groups.index,
        age_groups["Purchased"],
        color="green",
        label="Biztosítást vásárolt",
    )

    # Diagram formázása
    plt.title("Életkor szerinti biztosítási eloszlás", fontsize=14)
    plt.xlabel("Életkor (év)", fontsize=12)
    plt.ylabel("Ügyfelek száma", fontsize=12)
    plt.grid(True, alpha=0.3, axis="y")
    plt.legend()
    plt.tight_layout()

    # Mentés és bezárás
    plt.savefig(save_to_path)
    plt.close()

    return save_to_path
