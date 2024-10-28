import pandas as pd
import requests
from io import StringIO
import os

years = [2324, 2223, 2122, 2021, 1920, 1819, 1718, 1617, 1516, 1415]
leagues = ['E0', 'E1', 'E2']

# Initialize an empty list to store dataframes
all_data = []

def run_extraction():
    
    for year in years:
        for league in leagues:
            url = f'https://www.football-data.co.uk/mmz4281/{year}/{league}.csv'
            print(f"Fetching data from {url}")
            
            try:
                # Send a GET request to fetch the raw CSV data
                response = requests.get(url)
                response.raise_for_status()  # Check that the request was successful

                # Read the CSV data into a DataFrame
                data = pd.read_csv(StringIO(response.text))

                # Add a column to track the year and league
                data['Year'] = year
                data['League'] = league

                # Append the dataframe to the list
                all_data.append(data)
            except requests.exceptions.RequestException as e:
                print(f"Failed to fetch data for {year} {league}: {e}")
                
    os.makedirs('../datasets', exist_ok=True)

# Save the concatenated DataFrame to the 'datasets' folder
    all_data_df = pd.concat(all_data, ignore_index=True)

# Save the concatenated DataFrame to a CSV file
    all_data_df.to_csv('datasets/years_data.csv', index=False)
    
        
run_extraction()
