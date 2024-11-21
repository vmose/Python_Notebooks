#reading data from db
import pandas as pd
from sqlalchemy import create_engine

# Create an engine instance
#within quotes type out the servertype://user:password@serverIP/server

Engine = create_engine('postgresql://postgres:password@localhost/Mose',pool_recycle=3600)
# Connect to PostgreSQL server
dbConnection= Engine.connect()

# Read data from PostgreSQL database table and load into a DataFrame instance

df = pd.read_sql("select * from airbnb_listing", dbConnection)
#pd.set_option('display.expand_frame_repr', False);

# Print the DataFrame
print(df)

# Close the database connection
dbConnection.close()

pd.DataFrame(df.groupby('neighbourhood').sum()['price'])

df.groupby('neighbourhood_group').mean()['price']

import seaborn as sb
sb.heatmap(df.isnull(),cbar=None)
