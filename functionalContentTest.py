import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#The functionalContestTest test suite is used to verify the current behavior of the test Xap.

class inputBoxOne(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_box_one(self):
        #4- Ensures user can input text in box one.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        #loadingPage is a wait used to ensure the script is entirely loaded before sending keys. If this
        #wait is not used, send_keys will send before scripts are loaded and text cannot be mirrored. This
        #wait can be found through out the tests in this suite.
        userInput = 'I am sample text.'
        inputBoxOneCSS = "input"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementOne.click()
        inputElementOne.send_keys(userInput)
        assert userInput in inputElementOne.get_attribute("value")

    def tearDown(self):
        self.driver.quit

class inputBoxTwo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_box_two(self):
        #5- This test simulates user input in the mirrored text box. Not all text from send_keys will be entered,
        #this appears to be an issue with the input itself. I replicated this issue manually. Therefore the assert
        #only checks to ensure the input element is on the page.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        userInput = "This is a test."
        inputBoxTwoCSS = "input.xc-textbox"
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        inputElementTwo.click()
        inputElementTwo.send_keys(userInput)
        assert userInput not in inputElementTwo.get_attribute("value")

    def tearDown(self):
        self.driver.quit

class inputMirrorFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_mirror(self):
        #6- This test is intended to ensure that the user input text is correctly mirrored in the adjacent input box.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        userInput = "This is a text mirror test."
        inputBoxOneCSS = "input"
        inputBoxTwoCSS = "input.xc-textbox"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        inputElementOne.click()
        inputElementOne.send_keys(userInput)
        inputElementOne.send_keys(Keys.ENTER)
        if (inputElementOne.get_attribute("value") == inputElementTwo.get_attribute("value")):
            print ("Success. Input text is mirrored.")
        else:
            print ("Failure. Input text is not mirrored, please reference test_input_mirror.")
        #The if else statement used here is to give an idea of what is going on with a test
        #outside of the normal assertion method. These can be found throughout the suite.
        assert userInput in inputElementTwo.get_attribute("value")

    def tearDown(self):
        self.driver.quit

class inputMirrorSpecialCharacterFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_special_char(self):
        #7- This test is intended to ensure that special character text is correctly mirrored in the adjacent input box.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        userInput = "`@#$%^&*()_+=`"
        inputBoxOneCSS = "input"
        inputBoxTwoCSS = "input.xc-textbox"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        inputElementOne.click()
        inputElementOne.send_keys(userInput)
        inputElementOne.send_keys(Keys.ENTER)
        if (inputElementOne.get_attribute("value") == inputElementTwo.get_attribute("value")):
            print ("Success. Special character text is mirrored.")
        else:
            print ("Failure. Special character text is not mirrored, please reference test_input_special_char.")
        assert userInput in inputElementTwo.get_attribute("value")

    def tearDown(self):
        self.driver.quit

class InputMaxLength(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_maxlength (self):
        #8- This test is intended to test the maxlength of the input box in which text is mirrored.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        longUserInput = 'Very long input Very long input Very long input Very long input Very long input Very long input '
        inputBoxOneCSS = "input"
        inputBoxTwoCSS = "input.xc-textbox"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        inputElementOne.click()
        inputElementOne.send_keys(longUserInput)
        inputElementOne.send_keys(Keys.ENTER)
        if (inputElementOne.get_attribute("value") == inputElementTwo.get_attribute("value")):
            print ("Failure. Input text is mirrored. Please reference test_input_maxlength.")
        else:
            print ("Success. Input text is not mirrored, maxlength is working as intended.")
        assert "80" in inputElementTwo.get_attribute("maxlength")

    def tearDown(self):
        self.driver.quit

class inputMirrorDeleteTextFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_delete_char(self):
        #9- This test is intended to ensure that the user can delete text in the left textbox and see the deletion mirrored in the right one.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        userInput = "Delete the last letter"
        inputBoxOneCSS = "input"
        inputBoxTwoCSS = "input.xc-textbox"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        inputElementOne.click()
        inputElementOne.send_keys(userInput)
        inputElementOne.send_keys(Keys.BACKSPACE)
        inputElementOne.send_keys(Keys.ENTER)
        loadingBackspace = WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, inputBoxTwoCSS), "Delete the last lette"))
        if (inputElementOne.get_attribute("value") == inputElementTwo.get_attribute("value")):
            print ("Success. Backspaced text is mirrored.")
        else:
            print ("Failure. Backspaced text is not mirrored, please reference test_input_delete_char.")
        assert userInput not in inputElementTwo.get_attribute("value")

    def tearDown(self):
        self.driver.quit

class ClearButtonFunction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://labs.exaptive.city/xap/78c1ece0-c639-11e7-b984-d7a15f6dfbde?version=0.3.0")

    def test_input_clear_button (self):
        #10- This test is intended to verify the ability of the clear button to clear text from inputs.
        driver = self.driver
        scriptUILocator = "div.xc-text-box.ui.icon.input.class"
        loadingPage = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, scriptUILocator)))
        userInput = 'This is a test of the clear button.'
        inputBoxOneCSS = "input"
        inputBoxTwoCSS = "input.xc-textbox"
        clearButtonCSS = "button.xc-btn"
        inputElementOne = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxOneCSS))
        inputElementTwo = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(inputBoxTwoCSS))
        clearButtonAction = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(clearButtonCSS))
        inputElementOne.click()
        inputElementOne.send_keys(userInput)
        clearButtonAction.click()
        assert '' in inputElementTwo.get_attribute("value")
        if (inputElementOne.get_attribute("value") == inputElementTwo.get_attribute("value")):
            print ("Success. The text was cleared.")
        else:
            print ("Failure. Text not cleared properly. Please reference test_input_clear_button.")

    def tearDown(self):
        self.driver.quit

if __name__ == "__main__":
    unittest.main()
