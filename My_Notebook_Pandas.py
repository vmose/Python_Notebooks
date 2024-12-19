# %%
import numpy as np
import pandas as pd
#importing relevant libraries

# %%
from numpy.random import randn
np.random.seed(101)

# %%
index = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

# %%
pd.Series(data=my_list,index=index)

# %%
pd.Series(arr,index)

# %%
pd.Series(d)

# %%
playoffs ={1:'Lakers',2:'Clippers',3:'Nuggets'}
x=pd.Series(playoffs)
x

# %%
x[1]

# %%
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df

# %%
df.loc['A']

# %%
df['W']

# %%
df['new'] = df['W'] + df['Y']
df

# %%
df.drop('new',axis=1,inplace=True)

# %%
df[df['W']>0]

# %%
OrderBreakdown=pd.read_excel('P1-AmazingMartEU2.xlsx',sheet_name='OrderBreakdown')
OrderBreakdown

# %%
OrderBreakdown[OrderBreakdown['Profit']<0]

# %%
import seaborn as sb
sb.jointplot(data=OrderBreakdown,x='Sales',y='Profit',hue='Category',palette='coolwarm')

# %%
ListOfOrders=pd.read_excel('P1-AmazingMartEU2.xlsx',sheet_name='ListOfOrders')


# %%
SalesTargets=pd.read_excel('P1-AmazingMartEU2.xlsx',sheet_name='SalesTargets')
SalesTargets.head()

# %%
SalesTargets[SalesTargets['Month of Order Date']>'2013-01-01']

# %%

ListOfOrders.head()

# %%
ListOfOrders[ListOfOrders['Customer Name'].str.contains('Smith')==True]
#indexing similar to LIKE function in SQL

# %%
File=pd.read_csv('task_file.csv')
File

# %%
File.columns
# %%
x=File.groupby('d_date_id')
x.sum()[['unit_price', 'quantity',
       'sales_amount','discount_amount','price_w']]

# %%
orders=pd.read_csv('olist_orders_dataset.csv')
customers=pd.read_csv('olist_customers_dataset.csv')

# %%
Join=pd.merge(orders,customers,how='left',on='customer_id',sort='order_approved_at')
Join[['order_id', 'customer_id', 'order_status','order_approved_at', 'customer_city',
       'customer_state']]

# %%
orders.isnull()

# %%
sb.heatmap(orders.isnull())

# %%
orders.dropna(inplace=True)

# %%
sb.heatmap(orders.isnull())

# %%
