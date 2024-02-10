from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver) -> None:
        self.keyword_field = (By.ID, "keywords-input")
        self.search_button = (By.ID, "searchButton") 
        self.driver = driver

    def search(self, keyword):

        self.driver.get("https://www.jobstreet.com.ph/")

        keyword_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.keyword_field))
        seek_button = self.driver.find_element(*self.search_button)    
        keyword_input.send_keys(keyword)
        seek_button.click()

        