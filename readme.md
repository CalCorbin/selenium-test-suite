# Challenge Test Suite

This is a suite of Selenium regression tests written in Python. These test verify the current behavior of the test Xap.
These test cases use the Python unittest module and are intended to guard against breaking changes to the application. The test
has been broken down into three seperate files. There is the staticContestTest which is used to test and verify static
content on the page. Next there is the functionalContentTest which is used to verify all functional content on the page.
Finally there is the completeTestSuite test, this test contains the entire suite of tests.

This test suite is intended to specifically ensure the following behavior:
1. A user can type into the left textbox and see their text mirrored into the right textbox.
2. A user can delete text in the left textbox and see the deletion mirrored in the right textbox.
3. A user can click the "Clear" button to remove the text from both boxes.

## Instructions

Once you have navigated to the correct directory in terminal, the tests can be run in the terminal via:
`python completeTestSuite.py`

### Prerequisites

* Have the most up to date version of Python installed on your local machine.
* Have Selenium installed.
* Ensure the driver for Chrome is installed in your local Python installation.

### Installing

* Install Selenium locally
`pip install selenium`
* Ensure you have the chromedriver.exe installed on your local installation of Python, i.e. (C:\Python36\chromedriver.exe). The driver
can be found at https://sites.google.com/a/chromium.org/chromedriver/downloads.
* Detailed instructions for all of this can be found at http://selenium-python.readthedocs.io/installation.html.

## Built With

* [Atom] Text Editor and IDE - (https://atom.io/)
* [Selenium] Web Browser Automation - (http://www.seleniumhq.org/)
* [Selenium Python Driver] Simple API for writing tests using Selenium WebDriver - (http://selenium-python.readthedocs.io/)
* [Python Unit Test Module] Unit Testing Framework - (https://docs.python.org/2/library/unittest.html)
