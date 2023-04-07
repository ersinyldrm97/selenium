from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

def visit_apple_homepage():
  url = "http://www.apple.com"
  driver.maximize_window()

  driver.get(url)
  
  link = driver.current_url
  title = driver.title

  print("your page title is: ", title)

  if "apple.com" in link:
    print("You are on ", link)
    driver.save_screenshot("./screenshots/apple.png")
  driver.quit()

def visit_etsy_homepage():
  url = "http://www.etsy.com"
  driver.maximize_window()

  driver.get(url)

  link = driver.current_url
  title = driver.title

  print("Your page title is: ", title)

  if "etsy" in link:
    print("You are on ", link)
    driver.save_screenshot("./screenshots/true_link_for_etsy.png")
  else:
    print("Wrong parameter. Parameter should be ", link)
    driver.save_screenshot("./screenshots/wrong_link_for_etsy.png")

  driver.quit()

visit_apple_homepage()
visit_etsy_homepage()