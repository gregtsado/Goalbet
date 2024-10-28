import pandas as pd
from datetime import datetime
from extract import run_extraction


# Selecting Relevant features

df_final = pd.read_csv('datasets/years_data.csv' , dtype={'Time': str})

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
df_final['Time'] = pd.to_datetime(df_final['Time']).dt.time
df_final.head()


# df_final.to_csv('datasets/goalbet.csv', index=False)

print('Data cleaning and transformation successfully complete')