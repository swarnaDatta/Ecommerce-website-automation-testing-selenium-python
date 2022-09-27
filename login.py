from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

#Give demo email address
emailLabel = "//*[@id='root']/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/label"
driver.find_element(By.XPATH,emailLabel).click()
emailInput = "myaccount_login_email"
driver.find_element(By.ID,emailInput).send_keys("def@yahoo.com")

time.sleep(2)

# Give demo password
passLabel = "//*[@id='root']/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/label"
driver.find_element(By.XPATH,passLabel).click()
passInput = "myaccount_login_password"
driver.find_element(By.ID,passInput).send_keys("Jklmno9!")
time.sleep(2)

# Submit Log In
LoginButton = "//*[@id='root']/div[2]/div[2]/div/div/div[2]/form/div[4]/button"
driver.find_element(By.XPATH,LoginButton).submit()

time.sleep(2)

# click cross button
crossButton = "//*[@id='root']/div[2]/div[2]/div/div/div[1]/button"
driver.find_element(By.XPATH,crossButton).click()

time.sleep(2)

print("test successfully ended")
driver.close()
