import dask.dataframe as dd
import time
import dask  # Added missing import

def process_with_dask(file_path, threshold):
    # Csak a szükséges oszlopot olvassuk be
    df = dd.read_csv(file_path, 
                    usecols=['YearsCode'],
                    dtype={'YearsCode': 'object'})
    
    # Konvertálás és szűrés
    df['YearsCode'] = dd.to_numeric(df['YearsCode'], errors='coerce')
    filtered = df[(df['YearsCode'] > threshold) & (~df['YearsCode'].isna())]
    
    # Egyszeri compute() hívással számítjuk ki mindkét értéket
    count, sum_val = dask.compute(
        filtered.YearsCode.count(),
        filtered.YearsCode.sum()
    )
    
    return count, sum_val

if __name__ == "__main__":
    start_time = time.time()
    file_path = "./lessons/files/survey_results_public.csv"
    threshold = 10

    total_count, sum_values = process_with_dask(file_path, threshold)

    # Most már scalar értékekkel dolgozunk
    average = sum_values / total_count if total_count > 0 else 0
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Total count: {total_count}")
    print(f"Sum of YearsCode: {sum_values}")
    print(f"Average YearsCode: {average:.2f}")
    print(f"Execution time: {execution_time:.2f} seconds")