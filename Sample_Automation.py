import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
Warehouse = 'postgresql'
User = 'postgres'
Password = 'password'
Server  = 'localhost'
Schema = 'dvdrental'

engine = create_engine(f'{Warehouse}://{User}:{Password}@{Server}/{Schema}',pool_recycle=3500) 
# can be modified to incorporate the drivers used in the connection for instance ?driver=ODBC+Driver+18+for+SQL+Server

try:
    engine.connect()
    print('Connection successful')
except SQLAlchemyError as e:
    print(f'Error: {e}')
Connection successful
db=engine.connect()
df=pd.read_sql("""
SELECT
  p.customer_id,
  CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
  SUM(p.amount) AS total_amount
FROM
  payment p
  LEFT JOIN customer c ON p.customer_id = c.customer_id
GROUP BY
  p.customer_id, customer_name
ORDER BY
  total_amount DESC;
 """, db,index_col=None)

df.to_excel(r'C:\\Output\\Customer_Rankings.xlsx')
# export can than be emailed and automated using available OS task schedulers
  
