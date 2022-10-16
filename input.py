from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from openpyxl import load_workbook
import time

wb = load_workbook(filename="C:\Users\wawan\OneDrive\Documents\loginpemakai_k.xlsx")
sheetRange = wb['Sheet1']
driver = webdriver.Chrome()
#driver.get("https://sandbox.rsintanhusada.com/index.php?r=sistemAdministrator/loginpemakaiK/create&modul_id=1")
driver.get("https://sandbox.rsintanhusada.com/index.php?r=sistemAdministrator/LoginpemakaiK/Admin&modulId=1")
driver.maximaze_windows()
driver.implicitly_wait(5)

#looping
i = 2

while i <= len(sheetRange['A']):
    pegawai = sheetRange['A'+str(i)].value
    username = sheetRange['B'+str(i)].value
    password = sheetRange['C'+str(i)].value
    repassword = sheetRange['D'+str(i)].value

driver.find_element_by_class('btn btn-danger').click()


try:
    #WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div')))

    driver.find_element_by_id('SAPegawaiM_nama_pegawai').send_keys(pegawai)
    driver.find_element_by_id('LoginpemakaiK_nama_pemakai').send_keys(username)
    driver.find_element_by_id('LoginpemakaiK_new_password').send_keys(password)
    driver.find_element_by_id('LoginpemakaiK_new_password_repeat').send_keys(repassword)
    driver.find_element_by_id('submitButton').click()

except TimeoutException:
    print("OK")
    pass

time.sleep(1)
i = i + 1

print("clear")