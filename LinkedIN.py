#Import and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Here the process of automation is achieved by using the framework Selenium.
#Selenium is a portable framework for testing and automating web applications web applications

#Path to chromedriver.exe
chrome_path = r"C:\Users\giril\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"

#Initiating and setting up the driver
driver = webdriver.Chrome(chrome_path)

URL = "https://www.linkedin.com/"
driver.get(URL)

#The script is made to wait, to ensure that the page is loaded
time.sleep(2)

driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input").click()
name = input("Enter your username ")
time.sleep(3)
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input").send_keys(name)
time.sleep(2)
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input").click()
time.sleep(2)
passwd = input("Enter your password ")
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input").send_keys(passwd)
time.sleep(2)
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]").click()
time.sleep(1)
ppl = input("Enter the name of the contact ")
driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input").send_keys(ppl)
time.sleep(1)
driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[2]/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[1]/div/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
message = input("Enter the note u want to connect with ")
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/textarea").send_keys(message)
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[1]/a/span[1]").click()
