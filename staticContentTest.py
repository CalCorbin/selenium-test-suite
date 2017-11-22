import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class isExaptiveQAChallenge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_page_title(self):
    #Simple test that ensures this page is the QA Challenge
        driver = self.driver
        assert "QA Challenge" in driver.title

    def tearDown(self):
        self.driver.quit

class ensureCurrentJquery(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_jquery_url_correct(self):
        #This test is intended to ensure that the version of jquery on the page is up to date per the test case.
        driver = self.driver
        jqueryXpath = ('/html/head/div[1]/script[1]')
        jqueryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(jqueryXpath))
        assert "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0-beta1/jquery.min.js" in driver.page_source

    def tearDown(self):
        self.driver.quit

class ensureCurrentSemanticScript(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

        def test_semantic_script_correct(self):
            #This test is intended to ensure that the version of jquery on the page is up to date per the test case.
            driver = self.driver
            semanticMinXpath = ('/html/head/div[1]/script[2]')
            semanticMinElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(semanticMinXpath))
            assert "https://cdn.jsdelivr.net/semantic-ui/2.2.10/semantic.min.js" in driver.page_source

        def tearDown(self):
            self.driver.quit

if __name__ == "__main__":
    unittest.main()
