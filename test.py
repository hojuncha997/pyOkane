# # Selenium import
# from selenium import webdriver
#
# # webdriver 설정하기
# driver = webdriver.Chrome('./chromedriver.exe')
# driver.get("https://class101.net")
#
# greenbox = driver.find_elements("/html/body/div[1]/div/div/section/header/div/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/div/form/input")
# greenbox.send_keys("유튜브")
#셀레니움이 3에서 4로 버전업 되면서 find명령어 사용법이 변경됐음. 위는 3버전 아래는 4버전
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


options = Options()
options.add_experimental_option("detach", True)
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "http://naver.com"
driver.get(url)
time.sleep(3)

driver.find_element()