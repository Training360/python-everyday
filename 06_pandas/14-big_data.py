import pandas as pd
import time


def process_csv_in_chunks(file_path, threshold, chunksize=1000):
    """Optimalizált feldolgozás: csak a szükséges oszlop beolvasása"""
    total_count = 0
    sum_values = 0

    # Csak a YearsCode oszlopot olvassuk be
    for chunk in pd.read_csv(file_path, chunksize=chunksize, usecols=["YearsCode"]):
        chunk["YearsCode"] = pd.to_numeric(chunk["YearsCode"], errors="coerce")
        filtered = chunk[
            (chunk["YearsCode"] > threshold) & (~chunk["YearsCode"].isna())
        ]
        total_count += len(filtered)
        sum_values += filtered["YearsCode"].sum()

    return total_count, sum_values


def calculate_average(total_count, sum_values):
    """Kiszámolja az átlagot a total_count és sum_values alapján."""
    return sum_values / total_count if total_count > 0 else 0


if __name__ == "__main__":
    start_time = time.time()
    # Paraméterek
    file_path = "./files/survey_results_public.csv"
    threshold = 10

    # Feldolgozás és eredmények kiszámítása
    total_count, sum_values = process_csv_in_chunks(file_path, threshold)
    average = calculate_average(total_count, sum_values)
    end_time = time.time()
    execution_time = end_time - start_time

    # Eredmény kiírása
    print(f"Total count: {total_count}")
    print(f"Sum of YearsCode: {sum_values}")
    print(f"Average YearsCode: {average:.2f}")
    print(f"Execution time: {execution_time:.2f} seconds")
