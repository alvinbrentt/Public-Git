from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Results:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.job_id_element = (By.XPATH, "//*[starts-with(@id, 'job-title-')]")
        self.salary_range = (By.CSS_SELECTOR, '[data-automation="jobSalary"]')
        self.job_link = (By.CSS_SELECTOR, '[data-automation="job-list-view-job-link"]')
        self.pages = 50

    
    def scrape_results(self) -> list:

        paired_list = []
        self.driver.get("https://www.jobstreet.com.ph/wfh-jobs?page=1")

        for x in range(1, self.pages):

            self.driver.get("https://www.jobstreet.com.ph/wfh-jobs?page=" + str(x))

            try:
                job_id_elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(self.job_id_element),
                    message="message ids found."
                )
                salary_range_elements = self.driver.find_elements(*self.salary_range)
                job_link_elements = self.driver.find_elements(*self.job_link)
                
                job_ids = [element.text for element in job_id_elements]
                salary_range = [element.text for element in salary_range_elements]
                job_links = [element.get_attribute('href')[0:41] for element in job_link_elements]

                paired_list_batch = list(zip(job_ids, salary_range, job_links))

            except TimeoutError:
                print(f"Timed out while fetching job IDs for page {x}")

            time.sleep(2)
            paired_list.extend(paired_list_batch)

        return paired_list
    
    