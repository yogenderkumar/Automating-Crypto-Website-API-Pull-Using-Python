# 💰 Automating-Crypto-Website-API-Pull-Using-Python

Cryptocurrency Data Automation with Python project pulls cryptocurrency data from an API and analyzes & visualize it in Excel.

## 🔎 Project Overview

- Cryptocurrency data changes every second, and analyzing it manually is inefficient.
- This project automates the process of pulling live cryptocurrency data from the **CoinMarketCap API**, and visualizing market trends.  
- It fetches live data for thousands of cryptocurrencies, process it, and make it ready for **data analytics and reporting** using Python.

This project solves that problem by:  
- **Automating API calls** to fetch thousands of cryptocurrencies in real-time.  
- **Transforming raw JSON data** into structured tables for analysis.  
- **Exporting results** to CSV/Excel for easy reporting.  
- **Visualizing key insights** such as price changes, trading volumes, and market trends.  

---

## 📌 Features

This project demonstrates **API automation, data handling, and real-world financial analytics**

- ✅ **API Automation** → Pulls live data directly from CoinMarketCap API.  
- ✅ **Large Dataset Support** → Retrieves up to **5000 cryptocurrencies** at once.  
- ✅ **Error Handling** → Manages timeouts, redirects, and connection errors.  
- ✅ **Data Extraction** → Collects useful metrics like:
  - Cryptocurrency `id`, `name`, `symbol`
  - `market_pairs`, `circulating_supply`, `total_supply`
  - `price`, `volume_24h`, `percent_change (1h, 24h, 7d)`  
- ✅ **Data Ready for Analysis** → Data can be exported into **CSV/Excel** for further use.
  
- Pulls latest crypto market data (top 15 coins) from **CoinMarketCap API**
- Stores data in **CSV/Excel** files for further analysis
- Cleans missing values and standardizes column names
- Generates insights like:
  - Market trends over time
  - % price changes (1h, 24h, 7d, 30d, 60d, 90d)
  - Trading volume analysis
- Creates professional visualizations:
  - 📊 Line charts → Price trends  
  - 🔥 Heatmaps → % change comparison  
  - 📍 Point plots → Volume vs Price
- Runs automatically every minute (customizable)

---

## 🛠️ Tech Stack

- **Python** → Core programming  
- **Requests** → API integration  
- **JSON** → Handling API responses  
- **Pandas** → Data manipulation & cleaning  
- **Matplotlib & Seaborn** → Visualizations  
- **Excel/CSV** → Data export for reporting/Power BI

---

## 🔑 API Key Generation

- This project fetches cryptocurrency data using the **CoinMarketCap API**.  
- To run it successfully, you’ll need to generate a free API key from the CoinMarketCap website and configure it in the script.

**How to Generate and Use a CoinMarketCap API Key-**

1. Go to [CoinMarketCap Developer Portal](https://coinmarketcap.com/api/).  
2. Click **"Get Your API Key Now"** or **"Sign Up"**.  
3. Create a free account using your email ID.  

---

## 📂 Code Flow

1. **Import Libraries** → `requests`, `json`  
2. **Define API URL & Parameters** → Base endpoint from CoinMarketCap
3. **Connect to API** → Authenticate with CoinMarketCap API key. 
4. **Set Headers** → Authentication using API Key  
5. **Make API Request** → Fetch live cryptocurrency data  
6. **Fetch Data** → Retrieve crypto data in JSON format.  
7. **Transform Data** → Clean and structure into tabular form.  
8. **Export Data** → Save to CSV/Excel for further use.  
9. **Visualize** → Create trend charts, heatmaps, and performance insights. 
10. **Save / Export Data** → Print, analyze, or export  

---

## 📊 Example Use Cases

- 📈 **Crypto Market Analytics** → Build dashboards in Power BI/Excel using live crypto data  
- 🤖 **Data Science** → Train ML models with real-time financial datasets  
- 🔔 **Alerts System** → Notify when a coin crosses certain price thresholds  
- 💼 **Portfolio Tracker** → Automate daily price updates for investments  

---
