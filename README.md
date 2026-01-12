# 📚 E-commerce Web Scraper

A Python automation script designed to extract product data (title, price, rating, and availability) from e-commerce websites and export it to Excel for market analysis.

> **Note:** This project targets *Books to Scrape*, a sandbox website specifically built for testing web scraping scripts.

## 🚀 Features
- **Data Extraction:** Scrapes product names, pricing, star ratings, and stock status.
- **Data Cleaning:** Processes raw currency strings into floating-point numbers for analysis.
- **Export:** Automatically saves the structured data into an `.xlsx` (Excel) file.
- **Error Handling:** Includes basic HTTP error management using the `requests` library.

## 🛠️ Technologies Used
- **Python 3**
- **BeautifulSoup4** (HTML Parsing)
- **Requests** (HTTP Requests)
- **Pandas** (Data Manipulation & Export)

## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/seu-usuario/ecommerce-scraper.git](https://github.com/seu-usuario/ecommerce-scraper.git)
