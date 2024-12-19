# %%
""" 
Kiva, a non-profit organization,
stands as a beacon of hope for entrepreneurs in developing nations,
facilitating micro-lending to fuel thei ambitions. 
Leveraging the Kiva dataset on Kaggle, 
we embark on a journey to unveil the profound impact of micro-lending initiatives on entrepreneurial endeavors in these regions.
"""

# %%
import requests
import pandas as pd

query = """
{
  lend {
    loans(filters: {status: fundraising}, sortBy: newest) {
      values {
        id
        name
        loanAmount
        activity
        sector
        use
        raisedDate
        terms
        borrowerCount
      }
    }
  }
}
"""

# Set the API endpoint and headers
url = "https://gateway.production.kiva.org/graphql"
headers = {"Content-Type": "application/json"}

# Build the request body with the query
data = {"query": query}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  data = response.json()
  
  # Access loan information
  loan_data = data["data"]["lend"]["loans"]
  
  # print(f"Loan ID: {loan_data['id']}")
  # print(f"Loan Name: {loan_data['name']}")
  # print(f"Loan Amount: {loan_data['amount']}")
  df=pd.DataFrame(loan_data['values'], columns=['id', 'name', 'activity','sector','use','raisedDate','terms','borrowerCount','loanAmount'])
  print(df)
else:
  print(f"Error: {response.status_code}")

# %%
# importing the relevant datasets
import pandas as pd
kiva_loans = pd.read_csv(r'C:\Users\hp\Desktop\kiva_datasets\kiva_loans.csv',parse_dates=['posted_time','disbursed_time','funded_time'])
kiva_mpi_region_locations = pd.read_csv(r'C:\Users\hp\Desktop\kiva_datasets\kiva_mpi_region_locations.csv')
loan_theme_ids = pd.read_csv(r'C:\Users\hp\Desktop\kiva_datasets\loan_theme_ids.csv')
loan_themes_by_region = pd.read_csv(r'C:\Users\hp\Desktop\kiva_datasets\loan_themes_by_region.csv')

# %%
# Display dataset 1
kiva_loans.head()

# %%
# Display dataset 2
kiva_mpi_region_locations.head()

# %%
# Display dataset 3
loan_theme_ids.head()

# %%
# Display dataset 4
loan_themes_by_region.head()

# %%
# Get the mean and median of the loans

kiva_loans['Time_Detail'] = (kiva_loans.funded_time - kiva_loans.disbursed_time).dt.days

mean=kiva_loans['Time_Detail'].mean()
median=kiva_loans['Time_Detail'].median()

print(mean)
print(median)

# %%
#Display information in a histogram
plt.figure(figsize=(10,6))
plt.hist(kiva_loans['Time_Detail'],bins=100)
plt.axvline(mean, linestyle='dashed', label=f'The mean distribution time is {mean} days', color='green')
plt.axvline(median, linestyle='dashed',label=f'The median distribution time is {median} days',color='red')
plt.title('Disbursment Histogram')
plt.xlabel('No of Days')
plt.ylabel('Count')
plt.legend()
plt.show()

# %%
#Create Partner Performance Index Metric
union= kiva_loans.merge(kiva_mpi_region_locations, on=['country','region'],how='left')
PII=union.groupby('partner_id').mean()['MPI']
PII=((PII-PII.min())/(PII.max()-PII.min()))*100
PII=pd.DataFrame(PII)
PII=PII.sort_values('MPI',ascending=False)
PII=PII.iloc[:10]
PII

# %%
#Display information in a barchart

PII.plot(kind='bar',width=0.8,figsize=(10,6),color='orange')
plt.title('Partner Impact Index')
plt.xlabel('Partner ID')
plt.xticks(rotation=45)
plt.ylabel('Partner Impact Index')
plt.show()

# %%
# show distribution by sector
sector=kiva_loans.groupby('sector').sum()[['funded_amount', 'loan_amount']]
sector=sector.sort_values('funded_amount',ascending=False)
sector

# %%
#Display information in a barchart
import matplotlib.pyplot as plt
sector.plot(kind='bar', width=0.8, figsize=(10,6), color=['skyblue','coral'])
plt.title('Sector Analysis')
plt.xlabel('Sections')
plt.xticks(rotation=45)
plt.ylabel('Values (000,000)')
plt.show()

# %%

#display distribution by repayment interval
repayment_interval = kiva_loans.groupby('repayment_interval').count()['id']
repayment_interval = repayment_interval.sort_values(ascending=False)

plt.figure(figsize=(8, 6), facecolor='white') 
plt.pie(repayment_interval, labels=repayment_interval.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.title('Repayment Interval Distribution')  

plt.show()

# %%
#display distribution coubt by country

country = kiva_loans.groupby('country').count()['id']
country = country.sort_values(ascending=False)
country = country.iloc[:10]
country.plot(kind='bar', width=0.8, figsize=(10,6), color='red')
plt.title('Countries')
plt.xlabel('Countries')
plt.xticks(rotation=45)
plt.ylabel('Count of Loans')
plt.show()

# %%
#display distribution coubt by gender

borrower_genders = kiva_loans.groupby('borrower_genders').count()['id']

borrower_genders = borrower_genders.sort_values(ascending=False)

borrower_genders = borrower_genders.iloc[:2]

plt.figure(figsize=(8, 6), facecolor='white') 
plt.pie(borrower_genders, labels=borrower_genders.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.title('borrower_genders Distribution')  

plt.show()

