from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\python\GitTestingProject\Browsers\chromedriver.exe")

# searched "rok" page
driver.get("https://www.c-and-a.com/nl/nl/shop/search?q=rok")
driver.maximize_window()
time.sleep(10)

#delete cookies
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(5)

# select product "rok"
productImg = "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/a/div[1]/picture[1]/img"
driver.find_element(By.XPATH,productImg).click()
time.sleep(6)

# product name
productName = "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/h1"
nameOfProduct = str(driver.find_element(By.XPATH,productName).text)
print( nameOfProduct )

# choose the size
dropDownSize = "//*[@id='root']/div[2]/div/div[2]/div/div/div[6]/div/button/div[2]"
driver.find_element(By.XPATH,dropDownSize).click()
time.sleep(2)

# select size 46 available
sizeDiv = '//*[@id="root"]/div[2]/div/div[2]/div/div/div[6]/div/div/div/button[7]/div/div'
driver.find_element(By.XPATH,sizeDiv).click()
time.sleep(2)

# add to shopping cart
cartButton = "//*[@id='root']/div[2]/div/div[2]/div/div/div[7]/button"
driver.find_element(By.XPATH,cartButton).click()
time.sleep(3)

# select shopping cart
cartIcon = '//*[@id="root"]/div[1]/header/nav/div[4]/button[3]/div'
driver.find_element(By.XPATH,cartIcon).click()
time.sleep(2)


selectedProductText = "/html/body/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/a/div/div"
productInCart = str(driver.find_element(By.XPATH,selectedProductText).text)
print(productInCart)
assert nameOfProduct == productInCart
"""
if(nameOfProduct == productInCart):
    print("Successfull shopping")
else:
    print("Found Wrong in Shopping!")
"""
driver.close()
print("test successfully end")
