from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from jobs_io.results import Results
from .home_page import HomePage

class Search:

    def __init__(self, keyword) -> None:
        self.keyword = keyword
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.results = Results(self.driver)

    
    def search(self):
        self.home_page.search(self.keyword)
        job_ids = self.results.scrape_results()

        return job_ids
