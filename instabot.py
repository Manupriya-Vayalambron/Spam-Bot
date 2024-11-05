from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s=Service("C:/Users/kmrah/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.instagram.com")
time.sleep(1)
username=driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""")
username.send_keys("9539024555")
password=driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""")
password.send_keys("24may2005")
password.send_keys(Keys.ENTER)
time.sleep(5)
messenger=driver.find_element_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a""")
messenger.click()
time.sleep(5)
turnon=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]""")
turnon.click()
time.sleep(5)
sendmessage=driver.find_element_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div""")
sendmessage.click()
time.sleep(6)
friend=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/label/input""")
friend.send_keys("nawez.delight")
time.sleep(5)
tick=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div[1]""")
tick.click()
time.sleep(5)
chat=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div""")
chat.click()
time.sleep(5)
for i in range(7):
    text=driver.find_element_by_xpath("""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]""")
    text.send_keys("happie happie happie")
    text.send_keys(Keys.ENTER)
    time.sleep(1)
    
    
