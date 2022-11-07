from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from prettytable import PrettyTable
import os
import string
import collections

# The Scraper object inherits Selenium's Python webdriver; it offers
# functions using the webdriver to scrape Indeed.com
class Scraper(webdriver.Chrome):
    def __init__(self, driver_path=r'A:\SeleniumDrivers', teardown=False):
        # append path for this process
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += f';{self.driver_path}'

        # options
        options = webdriver.ChromeOptions()
        
        # options.headless = True
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Scraper, self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def search_job(self, what, where):
        '''Opens the indeed URL with what and where filled.'''
        self.get(f'https://www.indeed.com/jobs?q={what}&l={where}')

    def get_job_descriptions(self, pages=3):
        '''Clicks on each individual job card and extracts the job description and returns
        the words in a list.
        '''
        job_descs = ''
        count = 0
        
        while count != pages:
            ul_element = self.find_element(
                By.ID, 'mosaic-jobcards')
            elements = ul_element.find_elements(By.CSS_SELECTOR, '.job_seen_beacon')
            for element in elements:
                element.click()
                ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
                job_desc = WebDriverWait(self, 5, ignored_exceptions=ignored_exceptions)\
                    .until(expected_conditions.presence_of_element_located((By.ID, 'jobDescriptionText')))
                paragraphs = job_desc.find_elements(By.CSS_SELECTOR, 'p')
                job_descs += job_desc.text

                # dummy wait to pause execution in order to not trigger anti-scraping mechanism
                # 0 second wait because the code takes a bit of time to execute
                try:
                    WebDriverWait(self, 0, ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.ID, 'sad9f0ajsjhxczivuhzxcvlkjzxcvz')))
                except:
                    continue
                
            count += 1
            next_page_div = self.find_element(
                By.CSS_SELECTOR, 'a[data-testid="pagination-page-next"]')
            next_page_div.click()
            
        # job_descs = job_descs.translate(str.maketrans('', '', string.punctuation))
        job_descs = job_descs.split()
        job_descs = [x for x in job_descs if ("," not in x) and (":" not in x) and ("." not in x)]
        
        return job_descs
            
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
