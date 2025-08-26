# Automating-Crypto-Website-API-Pull-Using-Python
This Python project pulls cryptocurrency data from an API and analyzes it in Excel.

# 🚀 Cryptocurrency Data Automation with Python

This project automates the process of pulling live cryptocurrency data from the **CoinMarketCap API**, cleaning it, storing it in CSV/Excel, and visualizing market trends using Python.  

It is designed as a **Data Analyst project** to showcase skills in **Python, API integration, Pandas, Data Cleaning, and Data Visualization**.
It is designed to fetch live data for thousands of cryptocurrencies, process it, and make it ready for **data analytics and reporting**.

---

## 📌 Features
- Pulls latest crypto market data (top 15 coins) from **CoinMarketCap API**
- Stores data in **CSV/Excel** files for further analysis
- Cleans missing values and standardizes column names
- Generates insights like:
  - Market trends over time
  - % price changes (1h, 24h, 7d, 30d, 60d, 90d)
  - Trading volume analysis
- Creates professional visualizations:
  - 📊 Line plots
  - 🔥 Heatmaps
  - 📍 Point plots
- Runs automatically every minute (customizable)

---

## 🛠️ Tech Stack
- **Python**
- **Pandas** (data handling & cleaning)
- **Requests** (API calls)
- **Matplotlib & Seaborn** (visualizations)
- **Excel/CSV** for storage

---

# 🔑 How to Generate and Use a CoinMarketCap API Key

This project fetches cryptocurrency data using the **CoinMarketCap API**.  
To run it successfully, you’ll need to generate a free API key from the CoinMarketCap website and configure it in the script.

## 📝 Step 1: Create a CoinMarketCap Account

1. Go to [CoinMarketCap Developer Portal](https://coinmarketcap.com/api/).  
2. Click **"Get Your API Key Now"** or **"Sign Up"**.  
3. Create a free account using your email ID.  

---
## 📂 Project Structure

# 🚀 Automating Crypto Website API Pull Using Python

This project automates the process of pulling cryptocurrency market data from the **CoinMarketCap API** using Python.  
It is designed to fetch live data for thousands of cryptocurrencies, process it, and make it ready for **data analytics and reporting**.

---

## 🔎 Project Overview

The script connects to the **CoinMarketCap API** and retrieves real-time market data such as prices, market cap, supply, and trading volumes.  
It then structures the data so it can be used in **Excel, Power BI, or Python-based analysis**.

This project demonstrates **API automation, data handling, and real-world financial analytics**, making it valuable for data analyst roles.

---

## ✨ Features

- ✅ **API Automation** → Pulls live data directly from CoinMarketCap API.  
- ✅ **Large Dataset Support** → Retrieves up to **5000 cryptocurrencies** at once.  
- ✅ **Error Handling** → Manages timeouts, redirects, and connection errors.  
- ✅ **Data Extraction** → Collects useful metrics like:
  - Cryptocurrency `id`, `name`, `symbol`
  - `market_pairs`, `circulating_supply`, `total_supply`
  - `price`, `volume_24h`, `percent_change (1h, 24h, 7d)`  
- ✅ **Data Ready for Analysis** → Data can be exported into **CSV/Excel** for further use.  

---

## 🛠️ Tech Stack

- **Python** → Programming language  
- **Requests** → For API requests  
- **JSON** → Handling API response  
- *(Optional)* **Pandas / Excel** → Export and analysis  

---

## 📂 Code Flow

1. **Import Libraries** → `requests`, `json`  
2. **Define API URL & Parameters** → Base endpoint from CoinMarketCap  
3. **Set Headers** → Authentication using API Key  
4. **Make API Request** → Fetch live cryptocurrency data  
5. **Parse JSON Response** → Convert into Python structure  
6. **Save / Export Data** → Print, analyze, or export  

---

## 📊 Example Use Cases

- 📈 **Crypto Analytics** → Build dashboards in Power BI/Excel using live crypto data  
- 🤖 **Data Science** → Train ML models with real-time financial datasets  
- 🔔 **Alerts System** → Notify when a coin crosses certain price thresholds  
- 💼 **Portfolio Tracker** → Automate daily price updates for investments  

---
