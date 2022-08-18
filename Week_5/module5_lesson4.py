import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:opensource@localhost:5432/demo_db', pool_recycle = -1)
df = pd.read_csv('/Users/bukola/Downloads/Movies.csv')
print(df)

# Write data into the table in sqllite database
df.to_sql('movies_data', engine)


