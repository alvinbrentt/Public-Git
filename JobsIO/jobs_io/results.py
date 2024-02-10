from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Results:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.job_id_element = (By.XPATH, "//*[starts-with(@id, 'job-title-')]")
        self.pages = 5

    
    def scrape_results(self):

        job_ids = []
        self.driver.get("https://www.jobstreet.com.ph/wfh-jobs?page=1")

        for x in range(1, self.pages):

            self.driver.get("https://www.jobstreet.com.ph/wfh-jobs?page=" + str(x))

            try:
                job_id_elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(self.job_id_element),
                    message="message ids found."
                )

                for element in job_id_elements:
                    job_ids.append(element.text)
            
            except TimeoutError:
                print(f"Timed out while fetching job IDs for page {x}")

            time.sleep(2)

        return job_ids