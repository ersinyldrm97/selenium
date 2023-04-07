from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

def type_text():
  url = "http://www.google.com/"
  
  driver.get(url)
  
  search_box = driver.find_element(By.NAME, "q")
  search_box.send_keys("selenium")
  search_box.send_keys(Keys.ENTER) 
  
  driver.quit()

def click():
  url = "http://www.google.com"

  driver.get(url)

  search_box = driver.find_element(By.NAME, "q")
  search_box.send_keys("selenium")

  # click button for search from google
  driver.find_element(By.CSS_SELECTOR, "div.FPdoLc input.gNO89b").click()

  # click selenium page
  driver.find_element(By.CSS_SELECTOR, "div.tF2Cxc h3.LC20lb").click()

  if "Selenium" in driver.title:
    driver.save_screenshot("screenshots/selenium_include_in_title.png")
  else:
    driver.save_screenshot("screenshots/selenium_does_not_include_in_title.png")
  driver.quit()

# type_text()
click()