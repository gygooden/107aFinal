# Grayson Gooden / Akhil Lingutla
# Cosi107a Final Project
import pytest
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

url = "http://localhost/xvwa/vulnerabilities/reflected_xss"

script_dir = Path(__file__).parent
data_file = script_dir / 'example-data'

with open(data_file, 'r') as file:
    payloads = [line.strip() for line in file.readlines()]

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    yield browser
    browser.close()

@pytest.mark.parametrize("payload", payloads)
def test_xvwa_reflected_xss(driver, payload):
    try:
        print(f"Loading page {url}")
        driver.get(url)
        search_box = driver.find_element(By.NAME, "item")
        print(f"Sending payload to target field {payload}")
        search_box.send_keys(payload)
        submit_button = driver.find_element(By.CSS_SELECTOR, "div.form > div > button")
        submit_button.click()

        print("Checking if vulnerable..")
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        alert.accept()
        assert "Expected text if vulnerable" in alert_text
    except (NoSuchElementException, NoAlertPresentException):
        print("Test failed: Element not found or no alert present.")
