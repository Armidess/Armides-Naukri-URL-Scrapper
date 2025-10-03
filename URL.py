import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_URL = "https://www.naukri.com/security-engineer-network-engineer-network-security-cyber-security-cloud-security-application-security-devsecops-penetration-testing-jobs?k=security%20engineer%2C%20network%20engineer%2C%20network%20security%2C%20cyber%20security%2C%20cloud%20security%2C%20application%20security%2C%20devsecops%2C%20penetration%20testing&nignbevent_src=jobsearchDeskGNB&experience=3&ctcFilter=6to10&ctcFilter=10to15&ctcFilter=15to25&ctcFilter=25to50&ctcFilter=50to75&ctcFilter=75to100&ctcFilter=3to6"

OUTPUT_CSV = "scraped_jobs.csv"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def scrape_jobs_from_page():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.cust-job-tuple")))

    job_divs = driver.find_elements(By.CSS_SELECTOR, "div.cust-job-tuple.layout-wrapper.lay-2.sjw__tuple")

    job_urls = []
    for job_div in job_divs:
        try:
            anchor = job_div.find_element(By.CSS_SELECTOR, "h2 a.title")
            full_url = anchor.get_attribute("href")
            # Get relative url (for example usage)
            relative_url = full_url.replace("https://www.naukri.com", "")
            job_urls.append(relative_url)
        except Exception as e:
            print(f"Error extracting job URL: {e}")
            continue
    return job_urls

def go_to_next_page():
    try:
        next_btn = driver.find_element(By.XPATH, "//a[span[text()='Next'] and contains(@class, 'styles_btn-secondary__2AsIP')]")

        # Scroll the element into view to avoid overlays
        driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        time.sleep(1)

        # Use JavaScript click instead of Selenium click to avoid interception
        driver.execute_script("arguments[0].click();", next_btn)
        time.sleep(3)  # Wait for page to load
        return True
    except Exception as e:
        print(f"No Next button found or error: {e}")
        return False



def main():
    driver.get(SEARCH_URL)

    all_job_urls = []
    page_count = 0
    MAX_PAGES = 50  # Customize as needed

    while page_count < MAX_PAGES:
        job_urls = scrape_jobs_from_page()
        print(f"Page {page_count + 1} scraped {len(job_urls)} jobs.")
        all_job_urls.extend(job_urls)

        if not go_to_next_page():
            print("No next page or last page reached.")
            break
        page_count += 1

    # Deduplicate URLs
    unique_urls = list(set(all_job_urls))
    print(f"Total unique job URLs scraped: {len(unique_urls)}")

    # Save to CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for url in unique_urls:
            writer.writerow([url])

    driver.quit()

if __name__ == "__main__":
    main()
