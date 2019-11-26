import parametre
import sys
import csv
import string
import time

import random

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def pause():
    time_break = random.randint(1,2)
    return time.sleep(time_break)

  
writer = csv.writer(open(parametre.file_name, 'wb'))

writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')
username = driver.find_element_by_name('session_key')

password = driver.find_element_by_id('password')

username.send_keys(parametre.linkedin_username)
password.send_keys(parametre.linkedin_password)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

sign_in_button.click()

sleep(0.2)

driver.get('https:www.google.com')
sleep(1)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parametre.search_query)
sleep(0.5)
search_query.send_keys(Keys.RETURN)
sleep(1)

nb = 1
while nb > 0:
  i = ["0","1","2","3","4","5","6","7","8","9","10","11"]
  for path in i:
    linkedin_urls = driver.find_elements_by_xpath("//*[@id='rso']/div/div/div[{}]/div/div/div[1]/a".format(path))
  
    for url in linkedin_urls:
      print(url.get_attribute("href"))
      url_link = url.get_attribute("href")
      writer.writerow(["","","","","",url_link.encode('utf-8')])

  try:
    next = driver.find_element_by_xpath("//*[@id='pnnext']")
    next.click()
  except:
    print ("failed")
    nb = 2



driver.quit()




