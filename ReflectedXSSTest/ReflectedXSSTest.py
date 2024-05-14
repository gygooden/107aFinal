import pytest
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

webpage = "http://localhost/xvwa/vulnerabilities/reflected_xss"

root_dir = Path(__file__).parent # Obtain directory of the current script
our_file = root_dir / 'example-data' # Path concatenation using the Path object

with open(our_file, 'r') as xsspayloads:
    payloads = [payload.strip() for payload in xsspayloads.readlines()]

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()

@pytest.mark.parametrize("xsspayload", payloads)
def test_xvwa_reflected_xss(driver, xsspayload):
    try:
        print("Loading page " + webpage)
        driver.get(webpage)
        sbox = driver.find_element(By.NAME, "item")
        print("Sending payload to target field " + xsspayload)
        sbox.send_keys(xsspayload)
        verify = driver.find_element(By.CSS_SELECTOR, "div.form > div > button")
        verify.click()

        print("Checking if vulnerable..")
        obj = driver.switch_to.alert
        output = obj.text
        time.sleep(2)
        obj.accept()
        assert "Expected text if vulnerable" in output
    except (NoSuchElementException, NoAlertPresentException):
        print("Test failed: Element not found or no alert present.")
