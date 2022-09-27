from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#serviceObj = Service("C:\python\GitTestingProject\Browsers\chromedriver.exe")
#driver = webdriver.Chrome(serviceObj)
driver = webdriver.Chrome(executable_path="C:\python\GitTestingProject\Browsers\chromedriver.exe")


driver.get("https://www.c-and-a.com/nl/nl/shop")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
time.sleep(5)
#driver.delete_all_cookies(By.ID,"onetrust-accept-btn-handler").click()

# search button click
srcBut = "/html/body/div[1]/div[1]/header/nav/button"
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/nav/button").click()
time.sleep(5)

#search for a product
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='root']/div[1]/header/nav/div[2]/input").send_keys("rokken")
driver.find_element(By.CSS_SELECTOR,"#root > div.sc-fjqEFS.jgSVhW > header > nav > div.sc-jmnVvD.OpxHJ.sc-hgZZql.kWhFRv > button:nth-child(3) > svg").click()

#search results appear
time.sleep(5)
searchproduct = "Rok"
searchimage = "//*[@id='root']/div[2]/div[3]/div[2]/div[1]/div/a/div[1]/picture[2]/img"
time.sleep(5)
resultproduct = driver.find_element(By.XPATH,"//*[@id='root']/div[2]/div[3]/div[2]/div[1]/div/a/div[1]/picture[2]/img").get_attribute("title")
time.sleep(5)

pageurl = driver.current_url
print(pageurl)
driver.close()
if searchproduct == resultproduct:
    print("Search Test Successfull")
else:
    print("Search test failed!")


if searchproduct.lower() in pageurl:
    print("Search Page Load Successfull")
else:
    print("Search Page Load failed")
