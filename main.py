from helpers import get_postgres_engine
from modules.extract import run_extraction
from modules.load import load_csv_to_postgres
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text



engine = get_postgres_engine()

def main():
    
    """
    Main function to run the data pipeline modules
    parameters: None
    returns : None
    """
    
    run_extraction()

    load_csv_to_postgres('goalbet.csv', 'goalbet', engine, 'STG')


    session = sessionmaker(bind=engine)
    session = session()
    session.execute(text('CALL "STG".agg_goalbetdata()'))
    session.commit()
    
    print('pipeline executed successfully')
    
    print('Stored procedure executed successfully')
    

if __name__== '__main__':
    main()