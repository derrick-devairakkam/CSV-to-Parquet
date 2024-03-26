import csv
import unittest
import pandas as pd
import os

from csv_to_parquet import csv_to_parquet

# Define testcase class that inherits from unittest.testcase. This class contains inidividual test methods
class TestCSVtoParquet(unittest.TestCase):

    # This method is called before each test method. It sets up the env
    def setUp(self) -> None:
        # Create a sample csv file for testing
        self.csv_file = "test_input.csv"
        self.parquet_file = "test_output.parquet"
        self.test_data = {
            "Sport": ["Soccer", "Pickleball", "Tennis", "Weightlifting"],
            "Athleticism": [5, 2, 4, 3],
            "Accessibility": ["Low", "High", "High", "Excellent"]
        }
        self.df = pd.DataFrame(self.test_data)
        self.df.to_csv(self.csv_file, index=False)

    # This method is called after each test method. Cleans up the test env
    def tearDown(self) -> None:
        # Remove the files created from setup after testing
        os.remove(self.csv_file)
        os.remove(self.parquet_file)

    # Test methods must being with the word 'test'
    def test_csv_to_parquet(self) -> None:
        # Test csv to parquet conversion
        csv_to_parquet(self.csv_file, self.parquet_file)

        # Check if the parquet file was created
        self.assertTrue(os.path.exists(self.parquet_file))

        # Read parquet file back into dataframe
        df_parquet = pd.read_parquet(self.parquet_file)

        # Check if the dataframe contents are the same
        self.assertTrue(df_parquet.equals(self.df))

if __name__ == "__main__":
    unittest.main()
