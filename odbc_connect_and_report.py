import pandas as pd
from sqlalchemy import create_engine
import yagmail

# Connect to PostgreSQL Server
#create database connection and email sender

user = yagmail.SMTP(user = sender,password = password)
engine = create_engine('postgresql://postgres:password@localhost/Mose')
db = engine.connect()

#define table and create output
accounts = pd.read_sql('select * from accounts',db)
print(accounts)
(accounts).to_excel(r'c:\Output\useraccounts.xlsx')

#send email
user.send(to=receiver,subject='test',contents='This is a test',
          attachments=r'c:\Output\useraccounts.xlsx')

#close the database connection
db.close()


import pandas as pd
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=mydatabase;UID=myusername;PWD=mypassword')

# Extract data using SQL query
sql_query = "SELECT * FROM mytable"
df = pd.read_sql(sql_query, conn)

# Transform data
df = df.dropna() # drop rows with missing values
df['date'] = pd.to_datetime(df['date']) # convert date column to datetime

# Load data into PostgreSQL database
import psycopg2

conn = psycopg2.connect(host="localhost", database="mydatabase", user="myusername", password="mypassword")
cur = conn.cursor()
cur.execute("CREATE TABLE mytable (id SERIAL PRIMARY KEY, date DATE, value FLOAT)")
conn.commit()

for i, row in df.iterrows():
    cur.execute("INSERT INTO mytable (date, value) VALUES (%s, %s)", (row['date'], row['value']))
    conn.commit()
    
cur.close()
conn.close()
