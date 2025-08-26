#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
#Enter your Coinmarketcap API key Here
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',  # 👈 replace with your API key
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[4]:


type(data)


# In[10]:


import pandas as pd

# This allows you to see all the columns, not just like 15
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# Careful: If the API returns a huge dataset (like thousands of rows),
# showing all rows may freeze Jupyter. A safer choice is:
pd.set_option('display.max_rows', 50)   # show 50 rows
pd.set_option('display.max_columns', 50)  # show 50 columns


# In[11]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[12]:


# Select only important columns
df_clean = df[[
    'name',
    'symbol',
    'quote.USD.price',
    'quote.USD.volume_24h',
    'quote.USD.market_cap',
    'quote.USD.percent_change_1h',
    'quote.USD.percent_change_24h',
    'quote.USD.percent_change_7d',
    'timestamp'
]]

# Show the cleaned table
print(df_clean.head())


# In[13]:


# Show all rows and columns without wrapping
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)   # <---- stops wrapping
pd.set_option('display.colheader_justify', 'center')  # prettier headers


# In[14]:


print(df.head(15))   # or just df.head(15) in Jupyter


# In[15]:


df[['name','symbol','quote.USD.price','quote.USD.market_cap']].head(10)


# In[16]:


# Clean up column names or Simplify Column Names
df.columns = df.columns.str.replace("quote.USD.", "", regex=False)
df.columns = df.columns.str.replace(".", "_", regex=False)

print(df.columns)


# In[24]:


#To make it more readable, let’s bring important columns in front:
df = df[['name', 'symbol', 'price', 'market_cap', 'volume_24h', 
         'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'timestamp']]
print(df.head(10))


# In[25]:


import os
import json
import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def api_runner():
    global df
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '15',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',  # 👈 replace with your API key
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return
    
    # Create DataFrame
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')

    # Append to global DataFrame
    try:
        df = df._append(df2, ignore_index=True)
    except NameError:
        df = df2  # if df not defined, initialize it

    # Save to CSV
    file_path = r'C:\Users\Yogender\Documents\Python Scripts\API.csv'
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
    else:
        df2.to_csv(file_path, mode='a', header=False, index=False)

    return df


# In[26]:


import os 
from time import time
from time import sleep

for i in range(333):     # Run 333 times (about 5.5 hours if sleeping 1 min each loop)
    api_runner()         # call the API function you defined earlier
    print('API Runner completed')
    sleep(60)            # wait for 60 seconds before the next call
exit()


# In[27]:


import os
import json
import pandas as pd
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from time import sleep

# =========================
# API RUNNER FUNCTION
# =========================
def api_runner():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    parameters = {
        'start': '1',
        'limit': '15',   # Top 15 cryptos
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',  # 👈 replace with your API key
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print("Error:", e)
        return None  

    # Normalize JSON → DataFrame
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

    # Save to CSV
    file_path = r"C:\Users\Yogender\Documents\Python Scripts\API.csv"
    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False, header=True)
    else:
        df.to_csv(file_path, mode='a', index=False, header=False)

    return df


# =========================
# MAIN LOOP
# =========================
if __name__ == "__main__":
    for i in range(333):  # about 5.5 hours
        df = api_runner()
        if df is not None:
            print(f"[{i+1}/333] API Runner completed at {df['timestamp'].iloc[0]}")
        else:
            print(f"[{i+1}/333] API Runner failed.")
        sleep(60)  # wait 1 minute


# In[ ]:


df72 = pd.read_csv(r'C:\Users\Yogender\Documents\Python Scripts\API.csv')
df72


# In[ ]:


#Load your CSV
import pandas as pd

df72 = pd.read_csv(r"C:\Users\Yogender\Documents\Python Scripts\API.csv")
print(df72.head())
print(df72.columns)


# In[28]:


df


# In[29]:


import matplotlib.pyplot as plt

# Make a copy before filling NaN
df_missing = pd.read_csv(r'C:\Users\Yogender\Documents\Python Scripts\API.csv')

missing = df_missing.isnull().sum()

if missing.sum() > 0:
    plt.figure(figsize=(10,5))
    missing[missing > 0].plot(kind='bar')
    plt.title("Missing Values per Column (before filling)")
    plt.ylabel("Count of NaNs")
    plt.show()
else:
    print("✅ No missing values found in dataset!")


# In[30]:


import pandas as pd

# Load data
df72 = pd.read_csv(r'C:\Users\Yogender\Documents\Python Scripts\API.csv')

# Replace NaN values with something meaningful
df72 = df72.fillna("Data inaccessible by API")

# Double-check if any missing values remain
missing_after = df72.isnull().sum()

if missing_after.sum() == 0:
    print("✅ No missing values found in dataset after replacement.")
else:
    print("⚠️ Still some missing values remain:")
    print(missing_after[missing_after > 0])


# In[31]:


df72.head(10)


# In[32]:


#save the cleaned dataset as a new CSV so you can re-use it later:

df72.to_csv(r'C:\Users\Yogender\Documents\Python Scripts\API_cleaned.csv', index=False)
print("✅ Cleaned dataset saved as API_cleaned.csv")


# In[33]:


# --- DATA PROFILING / SUMMARY REPORT ---

print("📊 DATASET SUMMARY 📊\n")

# Shape of dataset
print(f"Total Rows: {df72.shape[0]}")
print(f"Total Columns: {df72.shape[1]}\n")

# Unique values count
print("🔹 Unique Values per Column:\n")
print(df72.nunique())
print("\n")


# In[48]:


# Clean column names (remove "quote.USD." prefix)
df72.columns = df72.columns.str.replace("quote.USD.", "", regex=False)

# Convert timestamp column to datetime if not already
df72['timestamp'] = pd.to_datetime(df72['timestamp'])


# In[49]:


#Daily % Change Distribution
import seaborn as sns

plt.figure(figsize=(10,6))
sns.boxplot(data=df72, x="name", y="percent_change_24h")
plt.title("24h % Change Distribution by Coin")
plt.xticks(rotation=45)
plt.show()


# In[51]:


import matplotlib.pyplot as plt

# Select top 5 coins by market cap
top_coins = df72.nlargest(5, 'market_cap')['name'].tolist()

# Plot Trading Volume Over Time
plt.figure(figsize=(10,6))
for coin in top_coins:
    subset = df72[df72['name'] == coin]
    plt.plot(subset['timestamp'], subset['volume_24h'], label=coin)

plt.title("Top 5 Cryptos Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume (USD)")
plt.legend()
plt.show()



# In[52]:


# Format float values for better readability
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# --- TREND ANALYSIS OVER MULTIPLE TIMEFRAMES ---
# Group data by coin and calculate mean % change across timeframes
df3 = df.groupby('name', sort=False)[[
    'quote.USD.percent_change_1h',
    'quote.USD.percent_change_24h',
    'quote.USD.percent_change_7d',
    'quote.USD.percent_change_30d',
    'quote.USD.percent_change_60d',
    'quote.USD.percent_change_90d'
]].mean()

# Reshape dataset (wide → long format)
df4 = df3.stack().to_frame(name='values').reset_index()

# Rename columns for clarity
df4 = df4.rename(columns={'level_1': 'percent_change'})

# Replace long API column names with cleaner labels
df4['percent_change'] = df4['percent_change'].replace({
    'quote.USD.percent_change_1h': '1h',
    'quote.USD.percent_change_24h': '24h',
    'quote.USD.percent_change_7d': '7d',
    'quote.USD.percent_change_30d': '30d',
    'quote.USD.percent_change_60d': '60d',
    'quote.USD.percent_change_90d': '90d'
})

# --- VISUALIZATION ---
plt.figure(figsize=(12,6))
sns.pointplot(x='percent_change', y='values', hue='name', data=df4)
plt.title('Cryptocurrency Performance Trends Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Timeframe', fontsize=12)
plt.ylabel('Average % Change', fontsize=12)
plt.legend(title='Cryptocurrency', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# In[55]:


# Save cleaned dataset
df72.to_csv(r"C:\Users\Yogender\Documents\Python Scripts\crypto_trends.csv", index=False)
df72.to_excel(r"C:\Users\Yogender\Documents\Python Scripts\crypto_trends.xlsx", index=False)

print("✅ Cleaned dataset saved as 'crypto_trends.csv' and 'crypto_trends.xlsx'")


# In[59]:


# Assuming your main dataframe is df72 (cleaned from API)
import pandas as pd

# Example: keep relevant columns
df = df72.copy()

# Convert percent change columns to numeric (replace 'Data inaccessible by API' with NaN first)
percent_cols = ['percent_change_1h','percent_change_24h','percent_change_7d',
                'percent_change_30d','percent_change_60d','percent_change_90d']

for col in percent_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Group by coin name
df3 = df.groupby('name', sort=False)[percent_cols].mean()

# Stack into long format
df4 = df3.stack()
df5 = df4.to_frame(name='values').reset_index()
df7 = df5.rename(columns={'level_1': 'percent_change'})

# Rename percent_change values for readability
df7['percent_change'] = df7['percent_change'].replace(
    {'percent_change_1h':'1h','percent_change_24h':'24h','percent_change_7d':'7d',
     'percent_change_30d':'30d','percent_change_60d':'60d','percent_change_90d':'90d'})


# In[60]:


import seaborn as sns
import matplotlib.pyplot as plt

# Define path
save_path = r"C:\Users\Yogender\Documents\Python Scripts"

# Save cleaned dataset
df7.to_csv(f"{save_path}\\crypto_trends.csv", index=False)
df7.to_excel(f"{save_path}\\crypto_trends.xlsx", index=False)
print("✅ Cleaned dataset saved at:")
print(f"- {save_path}\\crypto_trends.csv")
print(f"- {save_path}\\crypto_trends.xlsx")

# -----------------------
# 1. Point Plot
# -----------------------
plt.figure(figsize=(12,6))
sns.pointplot(x='percent_change', y='values', hue='name', data=df7)
plt.title("Crypto Price % Change Trends")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{save_path}\\crypto_pointplot.png")
plt.show()

# -----------------------
# 2. Heatmap
# -----------------------
df_pivot = df7.pivot(index='name', columns='percent_change', values='values')
plt.figure(figsize=(10,6))
sns.heatmap(df_pivot, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap of Crypto % Changes")
plt.tight_layout()
plt.savefig(f"{save_path}\\crypto_heatmap.png")
plt.show()

# -----------------------
# 3. Line Plot
# -----------------------
plt.figure(figsize=(12,6))
sns.lineplot(x='percent_change', y='values', hue='name', marker="o", data=df7)
plt.title("Line Plot of Crypto % Changes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{save_path}\\crypto_lineplot.png")
plt.show()

print("📊 Visualization images saved at:")
print(f"- {save_path}\\crypto_pointplot.png")
print(f"- {save_path}\\crypto_heatmap.png")
print(f"- {save_path}\\crypto_lineplot.png")


# In[ ]:




