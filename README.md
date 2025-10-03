# Naukri Job URL Scraper

A Python Selenium-based scraper to extract all job listing URLs from a given Naukri.com job search URL, including pagination handling.

## Features

- Scrapes all job URLs on the given search page and subsequent pages.
- Handles dynamic pagination with scrolling and JavaScript clicks to avoid overlay click interception.
- Extracts relative URLs compatible with JobSailor application script.
- Saves unique job URLs to a CSV file.
- Uses environment variables for configuration using `.env` file.

## Requirements

- Python 3.10+
- Google Chrome browser
- ChromeDriver compatible with your Chrome version (if not using undetected-chromedriver)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/naukri-job-scraper.git
    cd naukri-job-scraper
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Create a `.env` file in project root and configure any needed variables (e.g. search URL, output CSV):

    ```
    # Example .env
    SEARCH_URL=https://www.naukri.com/security-engineer-network-engineer-network-security-cyber-security-cloud-security-application-security-devsecops-penetration-testing-jobs?k=security%20engineer%2C...
    OUTPUT_CSV=scraped_job_urls.csv
    MAX_PAGES=10
    ```

## Usage

Run the scraper:

