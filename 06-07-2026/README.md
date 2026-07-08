# Data Extraction, Web Scraping, Data Analysis & Machine Learning Project

## Overview
This project showcases multiple Python concepts including API data extraction, web scraping, data analysis, data visualization, and machine learning. Data is collected from public APIs and websites, processed using Pandas, visualized using Matplotlib, and analyzed to generate meaningful insights.

## Technologies Used
- Python
- Pandas
- Requests
- BeautifulSoup
- Matplotlib
- Scikit-Learn
- OpenPyXL

## Project Modules

### 1. Data Extraction Through APIs
- Fetch data from GitHub API
- Fetch user data from JSONPlaceholder API
- Convert JSON responses into DataFrames
- Save extracted data to CSV and Excel files
- Handle API authentication and rate limits
- Implement error handling and retry mechanisms

### 2. Web Scraping
#### Fake Jobs Website
- Extract Job Title
- Company Name
- Location
- Apply Link
- Store results in structured datasets

#### Books To Scrape Website
- Extract Book Name
- Price
- Rating
- Availability

### 3. Data Analysis
- Dataset shape analysis
- Missing value detection
- Duplicate record checking
- Statistical summaries
- Company-wise job analysis
- Location-wise job analysis

### 4. Data Visualization
- Top Hiring Companies Chart
- Top Hiring Locations Chart
- Top GitHub Repositories by Stars

### 5. Machine Learning
- Linear Regression using Scikit-Learn
- Salary prediction based on years of experience
- Application logging using Python Logging module

## Files Generated
- github_repos.csv
- github_repos.xlsx
- users_data.csv
- users_data.xlsx
- jobs.csv
- jobs_clean.csv
- jobs_clean.xlsx
- top_companies.png
- top_locations.png

## Installation

```bash
pip install pandas requests beautifulsoup4 matplotlib scikit-learn openpyxl
```

## Run the Project

```bash
python project.py
```

## Features
- API Data Extraction
- JSON Data Processing
- Web Scraping with BeautifulSoup
- Data Cleaning and Analysis
- Data Visualization
- CSV and Excel Export
- Machine Learning Predictions
- Logging and Error Handling
- GitHub API Authentication

## Learning Outcomes
- Working with REST APIs
- JSON Data Handling
- Web Scraping Techniques
- Exploratory Data Analysis (EDA)
- Data Visualization using Matplotlib
- Machine Learning with Linear Regression
- File Handling (CSV & Excel)
- Logging and Monitoring Applications
- Error Handling and Retry Logic

## Author
**Sumukha Srivatsa**

## License
This project is developed for educational and learning purposes.
