import pandas as pd
import time


def process_csv_in_chunks(file_path, threshold, chunksize=1000):
    """
    Optimalizált feldolgozás: csak a szükséges oszlopot olvassa be,
    és generátorként visszaadja az eredményeket.
    """
    # Csak a YearsCode oszlopot olvassuk be
    for chunk in pd.read_csv(file_path, chunksize=chunksize, usecols=["YearsCode"]):
        chunk["YearsCode"] = pd.to_numeric(chunk["YearsCode"], errors="coerce")
        filtered = chunk[
            (chunk["YearsCode"] > threshold) & (~chunk["YearsCode"].isna())
        ]
        yield len(filtered), filtered["YearsCode"].sum()


def calculate_average(total_count, sum_values):
    return sum_values / total_count if total_count > 0 else 0


if __name__ == "__main__":
    start_time = time.time()
    file_path = "./files/survey_results_public.csv"
    threshold = 10
    total_count = 0
    sum_values = 0

    # Lusta kiértékelés: csak akkor dolgozunk fel egy chunkot,
    # amikor a generátor következő elemét kérjük
    for count, chunk_sum in process_csv_in_chunks(file_path, threshold):
        total_count += count
        sum_values += chunk_sum

    average = calculate_average(total_count, sum_values)
    end_time = time.time()
    execution_time = end_time - start_time

    # Végeredmény kiírása
    print(f"\nVégeredmény:")
    print(f"Total count: {total_count}")
    print(f"Sum of YearsCode: {sum_values}")
    print(f"Average YearsCode: {average:.2f}")
    print(f"Execution time: {execution_time:.2f} seconds")
