# %% 
from google.cloud import bigquery
import pandas as pd
import os

# Set the path to your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Mosev\Documents\configs\resolute-oxygen-128509-517167c4b20c.json"

# Initialize BigQuery client
client = bigquery.Client()

# Query
query = """
SELECT
  title,
  SUM(views) AS views
FROM
  `bigquery-samples.wikipedia_benchmark.Wiki10B`
WHERE
  REGEXP_CONTAINS(title, r' Cloud ')
GROUP BY
  title
ORDER BY
  views DESC
LIMIT 
  10
"""

# Run query and convert to pandas DataFrame
query_job = client.query(query)
dataframe = query_job.to_dataframe()
print(dataframe)


# %%
