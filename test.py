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



#URL
driver.get("https://sandbox.rsintanhusada.com/index.php?r=farmasiApotek&modul_id=10")

#LOGIN
driver.find_element(By.ID,'LoginForm_username').send_keys('sysadmin')
driver.find_element(By.ID,'LoginForm_password').send_keys('Rsih-123')
#se = Select(driver.findElement(By.xpath("//*[@id='oldSelectMenu']")));
#se = Select(driver.find_element(By.ID,'LoginForm_instalasi')).click()
driver.find_element(By.ID,'LoginForm_instalasi').click()
time.sleep(5)
#se.selectByIndex(3)
#driver.find_element(By.CSS_SELECTOR,"Option.[value='79']")
#
#pyautogui.countdown




#driver.implicitly_wait(10)
#pilih = Select(driver.find_element(By.ID,'LoginForm_instalasi'))
#pilih.select_by_visible_text('It/itkom/sirs/edp')
#pilih.select_by_value("79")
#select_by_value
#(79)
#driver.find_element(By.ID,'LoginForm_instalasi').click()
#Select instalasi = new Select(driver.find_element(By.ID('LoginForm_instalasi')))
#driver.find_element(By.CSS_SELECTOR,'option.value').click()
#send_keys('sysadmin')
#driver.find_element(By.ID,'LoginForm_ruangan').send_keys('Rsih-123')
#driver.find_element(By.ID,'LoginForm_modul').send_keys('sysadmin')
#driver.find_element(By.ID,'login-button').click()





