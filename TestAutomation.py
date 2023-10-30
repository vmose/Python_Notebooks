import pandas as pd
import yagmail
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:password@localhost/Mose')
db=engine.connect()
user = yagmail.SMTP(user='1030297@cuea.edu',password='cuea2020')
df=pd.read_sql('select * from bank',db)
(df).to_csv(r'C:\Output\test.csv')
user.send(to='vicmose.vm@gmail.com',
    subject='test2',
    contents='test',
    attachments=(r'C:\Output\test.csv'),
    cc='lemose98@gmail.com')