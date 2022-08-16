
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:opensource@localhost:5432/demo_db', pool_recycle = -1)
db_engine = engine.connect()
# print('engine created successfully')
# print(type(db_engine))

def db_query(query:str, db_conn:sqlalchemy.engine.base.Connection) ->pd.DataFrame:
    df = pd.read_sql(query, db_conn)
    print(df)

db_query('SELECT course_id, title, description FROM courses LIMIT 5', db_engine)
db_engine.close()