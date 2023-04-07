from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import json

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

def login():
  with open("./config/url.json") as url_json:
    with open("./config/login.secret.json") as user_information:
      data = json.load(user_information)
      url_data = json.load(url_json)
      url = url_data['url']['login']

      driver.get(url)

      driver.find_element(By.ID, 'username').send_keys(data['auth']['username'])
      driver.find_element(By.ID, 'password').send_keys(data['auth']['password'])
      driver.find_element(By.CSS_SELECTOR, 'button.radius').click()

      message_for_login = driver.find_element(By.ID, 'flash').text
      message_for_username = driver.find_element(By.ID, 'flash').text
      message_for_password = driver.find_element(By.ID, 'flash').text
      
#       
      if "You logged into a secure area!" in message_for_login:
        print('OK, You logged in')
        driver.save_screenshot('./screenshots/logged_in.png')
        
        logout_button = driver.find_element(By.XPATH, "//*[@id='content']/div/a/i")
        logout_button.click()

      elif "Your username is invalid!" in message_for_username:
        print('No, Your username is invalid')
        driver.save_screenshot('./screenshots/invalid_username.png')
      
      elif "Your password is invalid!" in message_for_password:
        print('No, Your password is invalid!')
        driver.save_screenshot('./screenshots/invalid_password.png')
        
      if 'login' in driver.current_url:
        print('Ok, you are back login page')
        driver.save_screenshot('./screenshots/reachable_login_page.png')
      else:
        print('No, you could not back login page')
        driver.save_screenshot('./screenshots/unreachable_login_page.png')
    
    driver.quit()
login()