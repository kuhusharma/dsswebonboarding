from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# try bs4 with requests for webscraping; only use selenium for clicking/interacting with the page
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options, service=service)
# options.add_argument("--headless=new")

driver.get("https://www.google.com/")

search_bar = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

search_bar.send_keys("dss berkeley", Keys.RETURN)
