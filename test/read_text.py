from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

def read_text():
  # these are turkish source for wikipedia
  url = "https://tr.wikipedia.org/wiki/Anasayfa"
  driver.maximize_window

  driver.get(url)
  readable_featured_text = driver.find_element(By.ID, "mp-tfa").text
  readable_text = readable_featured_text.split(",")[0]

  if "Mount & Blade II: Bannerlord" in readable_text:
    print(readable_text)
    driver.save_screenshot("screenshots/readable_featured_text.png")
  else:
    print(readable_text)
    driver.save_screenshot("screenshots/does_not_catch_readable_featured_text.png")

# these are english source for wikipedia
  today_featured_picture = driver.find_element(By.ID, "mp-tfp").text
  text = today_featured_picture.split(".")[0]
  
  if "Landscape" in text:
    print(text)
    driver.save_screenshot('screenshots/landscape_first_element.png')
  
  # the link is not turkish. therefore else condition will run.
  else:
    print(text)
    driver.save_screenshot('screenshots/does_not_catch_landscape.png')
  driver.quit()

read_text()