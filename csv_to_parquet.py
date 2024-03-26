import pandas as pd

def csv_to_parquet(csv_file, parquet_file):
    # Read csv file into dataframe
    df = pd.read_csv(csv_file)

    # Write dataframe to parquet file
    df.to_parquet(parquet_file, index=False)

if __name__ == "__main__":
    # Input csv file path
    csv_file = "/Users/derrickdevairakkam/Documents/Job/Torch AI /Coding assesment/automotive_data.csv"

    # Output parquet file path
    parquet_file = "/Users/derrickdevairakkam/Documents/Job/Torch AI /Coding assesment/output.parquet"

    # Convert csv to parquet
    csv_to_parquet(csv_file, parquet_file)
