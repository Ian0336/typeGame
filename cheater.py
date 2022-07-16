from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pykeyboard import *
import re
import time
driver = webdriver.Edge(executable_path="D:\\edgedriver\\msedgedriver")
driver.maximize_window()
driver.get("https://ian0336.github.io/typeGame/?fbclid=IwAR2W_EpdhQ9ljRGZlIIJlwlADpZwLBRoBD8Ymx_ooHSnFzPvq2ur99umOTc")
pat = re.compile("[0-9]+")

element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "app"))
)
k = PyKeyboard()
start = driver.find_element("id", "start")
randAlph = driver.find_element("id", "randalph")
redCar = driver.find_element("id", "car")


def setUp(m, l):
    mode = Select(driver.find_element("id", 'mode'))
    mode.select_by_index(m)
    level = Select(driver.find_element("id", "level"))
    level.select_by_index(l)
    start.click()


def playGame():
    global redCar
    print(str(pat.match(str(redCar.value_of_css_property("left"))).group()))
    while(int(str(pat.match(str(redCar.value_of_css_property("left"))).group())) < 1420):
        randAlph = driver.find_element("id", "randalph")
        print(str(randAlph.text))
        redCar = driver.find_element("id", "car")
        for char in str(randAlph.text):
            print(char)
            k.press_key(char)
            time.sleep(0.01)


for i in range(2):
    for j in range(4):
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "randalph"))
        )
        setUp(i, j)
        playGame()
        time.sleep(2)
        driver.switch_to.alert.accept()

time.sleep(5)
driver.quit()
