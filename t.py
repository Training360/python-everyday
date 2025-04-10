import pandas as pd
import random

# Generating synthetic data similar to the given format
random.seed(42)

# Define the structure for data generation
job_types = ["Employee", "Self-Employed", "Retired"]
existing_insurance_options = ["No", "Yes"]
purchased_insurance_options = ["No", "Yes"]

# Generate synthetic data
data = {
    "Age": [random.randint(18, 70) for _ in range(100000)],
    "Income": [random.randint(20000, 100000) for _ in range(100000)],
    "JobType": [random.choice(job_types) for _ in range(100000)],
    "ExistingInsurance": [random.choice(existing_insurance_options) for _ in range(100000)],
    "PurchasedInsurance": [random.choice(purchased_insurance_options) for _ in range(100000)],
}
print(data)


# CSV-be mentés
csv_path = 'c:\\Projects\\TRAINING360\\python-everyday\\lessons\\08-gml\\insurance_data_100k.csv'
df = pd.DataFrame(data)
df.to_csv(csv_path, index=False)

