
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from model.sql_model import BASE
db_user:str="postgres"
db_port:int=5432
db_host:str="localhost"

db_password:str="Diamond0343!@"
encoded_password = quote(db_password)

uri:str=f"postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/todo_db"
engine=create_engine(uri)
BASE.metadata.create_all(bind=engine)

#session
session=sessionmaker(bind=engine,
                     autoflush=True)
db_session=session()
try:
    connection=engine.connect()
    connection.close()
    print( "ping,Connected")
except Exception as e:
    print(f'Error:{str(e)}')