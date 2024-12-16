import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Google
driver.get("https://www.google.com")
# Navigate to Google
driver.get("https://about.google/")
# Navigate to Google
driver.get("https://about.google/products/")
# Navigate to Google
driver.get ("https://store.google.com/IN?utm_source=hp_header&utm_medium=google_ooo&utm_campaign=GS100042&hl=en-IN")
# Print the title of the page

print("Page title is:", driver.title)
   assert driver.title=="Google"
ele = driver.find_element(By.NAME, 'q')
ele.send_keys("nishma")
time.sleep(30)
"""

@pytest.fixture
def driver():
    print("enter")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("before yield")
    yield driver  
    print("after yield")
    driver.quit() 


def test_subject(driver):
    print("In test")
    driver.get("https://google.com")
    print("Page title is:", driver.title)
    assert driver.title == "Google"
    
    
