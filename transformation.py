import pandas as pd
from datetime import datetime
from extract import run_extraction


# run_extraction()
# Read in datasets
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


#Joining all datasets together

df_20192020 = pd.concat([data1_20192020, data2_20192020, data3_20192020])
df_20202021 = pd.concat([data1_20202021, data1_20202021, data1_20202021])
df_20212022 = pd.concat([data1_20212022, data2_20212022, data3_20212022])
df_20222023 = pd.concat([data1_20222023, data2_20222023, data3_20222023])
df_20232024 = pd.concat([data1_20232024, data2_20232024, data3_20232024])


df_final = pd.concat([df_20192020, df_20202021, df_20212022, df_20222023, df_20232024])

# Selecting Relevant features

df_final = df_final[['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam','FTHG', 'FTAG']]

# changing date datatype from object to datetime

date_formats = ["%d/%m/%Y", "%m/%d/%Y", "%Y-%m-%d"]

def parse_date(date_string):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    return pd.NaT 


df_final['Date'] = df_final['Date'].apply(parse_date)


# changing Time datatype from object to datetime
def convert_to_timedelta(time_string):
    hours, minutes = map(int, time_string.split(':'))
    return pd.Timedelta(hours=hours, minutes=minutes)



# Apply the function to the 'Time' column
df_final['Time'] = df_final['Time'].apply(convert_to_timedelta)

df_final.to_csv('datasets/goalbet.csv', index=False)

print('Data cleaning and transformation successfully complete')