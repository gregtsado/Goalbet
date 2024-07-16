from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(override=True)

def get_postgres_engine():
    
    """
    Constructs a SQLalchemy engine object for Postgres DB from .env file
    
    Paremeters: None
    
    Returns:
    -sqlachemy engine (sqlalchemy.engine.Engine)
    """

   
    engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
                            user = os.getenv('pg_user'),
                            password = os.getenv('pg_password'),
                            host = os.getenv('pg_host'),
                            port = os.getenv('pg_port'),
                            dbname = os.getenv('pg_dbname')
                                 )
                        )
    
    return engine