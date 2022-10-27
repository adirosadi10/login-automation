from lib2to3.pgen2 import driver
from optparse import Option
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
#3import org.openqa.selenium.
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import pyautogui
import time
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.maximize_window()



#URL
#driver.get("https://sandbox.rsintanhusada.com/index.php?r=farmasiApotek&modul_id=10")
driver.get("https://dev.ihospital.id/index.php?r=site/login")

#LOGIN
##username dan password
driver.find_element(By.ID,'LoginForm_username').send_keys('rosadi')
driver.find_element(By.ID,'LoginForm_password').send_keys('Rosadi-10')
time.sleep(3)
driver.find_element(By.ID,'login-button').click()

#MASUK KE MENU LOGIN PEMAKAI
#driver.find_element(By.LINK_TEXT,value='/index.php?r=sistemAdministrator/LoginpemakaiK/Admin&modulId=1')
#driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/ul[1]/li[6]/ul/li[2]/a').click()
#driver.find_element(By.CSS_SELECTOR, value='.navbar-nav > li:nth-child(6) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)').click()
driver.find_element(By.CLASS_NAME,'icon-batalkeluarumum').click()

