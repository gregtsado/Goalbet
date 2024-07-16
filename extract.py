import pandas as pd

def run_extraction():
    try:
        data1_20192020 = pd.read_csv(r'datasets\football\2019-2020\E0.csv')
        data2_20192020 = pd.read_csv(r'datasets\football\2019-2020\E1.csv')
        data3_20192020 = pd.read_csv(r'datasets\football\2019-2020\E2.csv')
        
        data1_20202021 = pd.read_csv(r'datasets\football\2020-2021\E0.csv')
        data2_20202021 = pd.read_csv(r'datasets\football\2020-2021\E1.csv')
        data3_20202021 = pd.read_csv(r'datasets\football\2020-2021\E2.csv')
        
        data1_20212022 = pd.read_csv(r'datasets\football\2021-2022\E0.csv')
        data2_20212022 = pd.read_csv(r'datasets\football\2021-2022\E1.csv')
        data3_20212022 = pd.read_csv(r'datasets\football\2021-2022\E2.csv')
        
        data1_20222023 = pd.read_csv(r'datasets\football\2022-2023\E0.csv')
        data2_20222023 = pd.read_csv(r'datasets\football\2022-2023\E1.csv')
        data3_20222023 = pd.read_csv(r'datasets\football\2022-2023\E2.csv')
        
        data1_20232024 = pd.read_csv(r'datasets\football\2023-2024\E0.csv')
        data2_20232024 = pd.read_csv(r'datasets\football\2023-2024\E1.csv')
        data3_20232024 = pd.read_csv(r'datasets\football\2023-2024\E2.csv')
          
        
        print('All Data extracted successfully')
    except Exception as e:
        print(f'An error occured:{e}')
        
run_extraction()