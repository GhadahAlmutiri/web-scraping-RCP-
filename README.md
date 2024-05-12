# Watch Brand Website Scraper

## About the Project

The goal of this project is to scrape a watch brand's website to gather a set of data points about every watch. The project is divided into three major tasks:

1. **Stage 1: Data Collection (Web Scraping)**
   - Collect data via web scraping.
   - Perform data analysis and create a summary report in a Python notebook.

2. **Stage 2: Data Cleaning**
   - Perform data cleaning on the collected data.

3. **Stage 3: Pipeline Automation**
   - Automate the pipeline using Airflow and Docker.

## Project Overview

For this project, we used BeautifulSoup to scrape data from Raymond Weil watches brand. The main task was to extract watch specifications and store them in a CSV file. We categorized the watches into two sections: men's watches and women's watches.

### Tools and Packages Used

- **Web Scraping:** We used `requests`, `BeautifulSoup`, and `selenium` with a webdriver to scrape the website.
  - Opened the website links for each men and women watches.
  - Closed the website cookie consent banner (if present).
  - Scrolled the page to load additional watch listings.
  - Extracted basic product details (title, link) from the currently loaded page content.
  - Fetched and visited individual product pages to extract detailed specs.

- **CSV File Export:**
  - Used `csv.writer` to export the collected watches data into a CSV file.

- **Data Analysis:**
  - Used `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scipy.stats` for data analysis.
  - Read the CSV file into a Pandas DataFrame using `pd.read_csv`.
  - Operated statistics on the DataFrame and retrieved info about it using `df.describe` and `df.info`.
  - Visualized data features and specifications using various charts (e.g., bar chart, pie chart).

## Project Implementation

The project is implemented in stages, with each stage focusing on a specific task. During each stage, we submitted our project implementation for review.

