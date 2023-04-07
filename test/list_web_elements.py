import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.maximize_window()

def list_elements():
  driver.get("http://www.imdb.com")
  driver.find_element(By.XPATH, "//*[div]/label ").click()
  # with different xpath way
  # driver.find_element(By.XPATH, "//*[@id="imdbHeader-navDrawerOpen"]")
  # driver.find_element(By.XPATH, "/html/body/div[2]/nav/div[2]/label[1]")
  # with id
  # driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
  
  time.sleep(1)
  driver.find_element(By.XPATH, "//span[text()='Top 250 Movies']").click()

  movie_list = driver.find_elements(By.XPATH, "//table/tbody/tr/td[@class='titleColumn']")

  for i in movie_list:
    if i.text[-5:-1] == '2000':
      print(i.text)

  driver.quit()
list_elements()