import pandas as pd
from sqlalchemy.orm import sessionmaker


# def load_csv_to_postgres(table_name, engine, schema):
#     """
#     Loads data from a csv file to a postgres DB table
    
#     Parameters:
#     -table_name(str): a postgres table
#     -engine (sqlalchemy.engine): an SQL alchemy eninge object
#     -schema (str): a postgres DB schema
#     """
    
#     df = pd.read_csv('datasets\goalbet.csv')
    
#     return engine

#     df.to_sql(table_name, con = engine, if_exists='replace', index=False, schema=schema)
    
#     print(f'{len(df)} rows loaded to staging successfully')
    
# # def exec_procedure(engine):
# #     session = sessionmaker(bind=engine)
# #     session = session()
# #     session.execute('CALL "STG".agg_trip_data()')
# #     session.commit()
    
#     print('Stored procedure executed successfully')
    
    
    
import pandas as pd

def load_csv_to_postgres(csv_file_path, table_name, engine, schema):
    '''
    load data from a csv file to datatframe to postgres database table
 
    parameters:
    - csv_file_path (str): path to the csv file
    - table_name(str): postgres database table
    _ engine(sqlalchemy.engine): sqlalchemy engine object
    _ schema(str): a postgress DB schema
    '''
    csv_file_path =r'datasets\goalbet.csv'
    
    #read csv to pandas and to sql
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, schema=schema)

    print(f'{len(df)}rows loaded to staging successfully')
    
