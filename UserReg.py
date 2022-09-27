from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\python\GitTestingProject\Browsers\chromedriver.exe")

driver.get("https://www.c-and-a.com/nl/nl/shop")
print("test started")
driver.maximize_window()
time.sleep(10)
#delete cookies
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(5)

#click user button
usericon = "//*[@id='root']/div[1]/header/nav/div[4]/button[1]"
driver.find_element(By.XPATH,usericon).click()
time.sleep(5)

# select Registeer Nu
regnu = "Registreer nu"
driver.find_element(By.LINK_TEXT,regnu).click()
time.sleep(5)

# New customer information table
# select Mrs. label
mrslabel = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[1]/div[1]/div[1]/label[2]"
driver.find_element(By.XPATH,mrslabel).click()

time.sleep(2)
# put first name
firstnamelabel = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[1]/div[1]/div[2]/label"
driver.find_element(By.XPATH,firstnamelabel).click()
driver.find_element(By.ID,"register.firstName").send_keys("Abc")

time.sleep(2)
# put surname
surnamelabel = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[1]/div[1]/div[3]/label"
driver.find_element(By.XPATH,surnamelabel).click()
driver.find_element(By.ID,"register.lastName").send_keys("Def")

time.sleep(2)
# put demo email address
emaillabel = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[1]/div[1]/div[3]/label"
driver.find_element(By.XPATH,emaillabel).click()
driver.find_element(By.ID,"register.email").send_keys("ghi@yahoo.com")
time.sleep(2)

# Demo password 8 char: 1 num 1 letter 1 capital 1 special character
passlabel = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[1]/div[3]/div/label"
driver.find_element(By.XPATH, passlabel).click()
passinputtext = "register.loginPassword"
driver.find_element(By.ID,passinputtext).send_keys("Jklmno9?")
time.sleep(2)

# select Data Protection agreement
regConfirm = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/fieldset[2]/div/div/label"
driver.find_element(By.XPATH,regConfirm).click()
time.sleep(2)

#Submit "Register Now"
regNowButton = "//*[@id='main']/section/div/div[3]/div/div[2]/div[1]/div/div/form/ng-form/div/button"
driver.find_element(By.XPATH,regNowButton).submit()
time.sleep(2)


print("test successfully end")
driver.close()



