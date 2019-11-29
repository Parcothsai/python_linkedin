# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from bs4 import BeautifulSoup

import parametre
import sys
import csv
import string
import time
import os.path
from os import path


import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("--driver", "-d", help="choose your driver with value chrome or firefox")
parser.add_argument("--install", "-i", help="Install driver chrome || firefox")
#parser.add_argument("--search", "-s", help="Use -s || --search to make search without using parametre.py ")

args = parser.parse_args()
if args.install == "chrome":
    subprocess.call(["bash","install/chrome.sh"])
if args.install == "firefox":
    subprocess.call(["bash","install/firefox.sh"])
    
if args.driver == "chrome":
    print ("driver is chrome")
    print ("Check if webdriver chrome exist")
    if path.exists("./chromedriver"):
        print "webdriver chrome exist, continue !\n"
        driver = webdriver.Chrome('./chromedriver')
    else:
        print "Webdriver not present, please use -h for help ! "
        sys.exit()
       

elif args.driver == "firefox":
    print("driver is firefox")
    if path.exists("/usr/local/bin/geckodriver") or path.exists("/usr/bin/geckodriver"):
        print "Ok, geckodriver is present, continue..."
        driver = webdriver.Firefox()
    else:
        print "Geckodriver is not present, please use growth -i firefox"
        sys.exit()
else:
    print ("Expected one argument, chrome or firefox ! Use grotwh.py -d chrome or -d firefox")
    sys.exit()


    


def pause():
    time_break = random.randint(1,2)
    # print "Pause de " + str(time_break) + " seconde(s)."
    return time.sleep(time_break)

  
writer = csv.writer(open(parametre.file_name, 'wb'))

writer.writerow(['Name', 'Job Title', 'Location', 'URL'])


driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')
username = driver.find_element_by_name('session_key')

password = driver.find_element_by_id('password')

username.send_keys(parametre.linkedin_username)
password.send_keys(parametre.linkedin_password)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

sign_in_button.click()
sleep(0.2)
driver.get('https://www.google.com')
sleep(1)
search_query = driver.find_element_by_name('q')
search_query.send_keys(parametre.search_query)
sleep(0.5)
search_query.send_keys(Keys.RETURN)
sleep(1)

nb = 3
while nb > 2:
  i = ["0","1","2","3","4","5","6","7","8","9","10","11"]
  driver.current_url
  htmlBody = driver.find_element_by_css_selector("body").get_attribute('innerHTML')

  soup = BeautifulSoup(htmlBody, 'html5lib')

  while soup.find("div", id="recaptcha") is not None:
      print('You are temporary blacklisted from Google search. Complete the captcha then press ENTER.')
      token = raw_input(">")
      htmlBody = driver.find_element_by_css_selector("body").get_attribute('innerHTML')
      soup = BeautifulSoup(htmlBody, 'html5lib')
  for path in i:
    linkedin_urls = driver.find_elements_by_xpath("//*[@id='rso']/div/div/div[{}]/div/div/div[1]/a".format(path))

    for url in linkedin_urls:
      print(url.get_attribute("href"))
      url_link = url.get_attribute("href")
      driver.get(url_link)
      linkedin_name = driver.find_element_by_xpath('//li[contains(@class,"inline t-24 t-black t-normal break-words")]')
      linkedin_work = driver.find_element_by_xpath('//h2[contains(@class,"mt1 t-18 t-black t-normal")]')
      linkedin_region = driver.find_element_by_xpath('//li[contains(@class,"t-16 t-black t-normal inline-block")]')
      print(linkedin_name.text)
      print(linkedin_work.text)
      print(linkedin_region.text)
      writer.writerow([linkedin_name.text,linkedin_work.text,linkedin_region.text,url_link.encode('utf-8')])
      driver.back()
      sleep(2)

  try:

    next = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='pnnext']"))
    )
    next.click()

  except:
    print ("Your are on the last page, exit")
    nb = 1

driver.quit()


