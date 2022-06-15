import time
import pickle
import asyncio
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


async def grab_data(url, stock):

    print("Grabbing data")

    # setting up selenium
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')

    chrome_driver_binary = "/home/nils/.local/bin/chromedriver"

    browser = webdriver.Chrome(
        options=options, executable_path='/snap/bin/chromium.chromedriver')

    delay = 60

    browser.get(url)

    def get_element(x_path):
        try:
            return WebDriverWait(browser, delay).until(EC.presence_of_element_located(
                (By.XPATH, str(x_path))))
        except TimeoutException:
            print("Loading took too much time!")
            browser.quit()

    ################# LOGIN #############
    email = "nils.malmberg@edu.jarfalla.se"
    vklass_uname = "JFK\\nimal003"
    vklass_pwd = "Sommar16"

    # input email:
    input = get_element(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    input.send_keys(email)

    # press "done":
    button = get_element(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
    button.click()

    # press "vklass inloggning":
    button = get_element(
        "/html/body/div/div/section/div[2]/div/div[1]/a[3]")
    button.click()

    # input "vklass uname"
    input = get_element(
        "/html/body/div/div/section/div[2]/div/form/div[1]/div/input")
    input.send_keys(vklass_uname)

    # input "vklass pwd"
    input = get_element(
        "/html/body/div/div/section/div[2]/div/form/div[2]/div/input")
    input.send_keys(vklass_pwd)

    # press "Logga in"
    button = get_element(
        "/html/body/div/div/section/div[2]/div/form/div[4]/button")
    button.click()

    ############ EXEL work ############

    # inject function
    input = get_element(
        "/html/body/div[2]/div[8]/div[6]/div[3]/div[3]/div/div/div")

    for i in range(100):
        input.send_keys(Keys.BACK_SPACE)

    input.send_keys(
        f'=GOOGLEFINANCE("{stock}"; "all"; "01/01/1980"; "10/06/2022"; "DAILY")')
    input.send_keys(Keys.RETURN)

    # press "Arkiv":
    button = get_element("/html/body/div[2]/div[4]/div[1]/div[1]/div[1]")
    button.click()

    # navigate and press "Ladda ner":
    for i in range(7):
        ActionChains(browser).send_keys(Keys.DOWN).perform()

    ActionChains(browser).send_keys(Keys.ENTER).perform()

    for i in range(4):
        ActionChains(browser).send_keys(Keys.DOWN).perform()

    ActionChains(browser).send_keys(Keys.ENTER).perform()

    print("Data collection complete")

    time.sleep(5)

    browser.quit()

if __name__ == "__main__":
    asyncio.run(grab_data(
        "https://docs.google.com/spreadsheets/d/1I2tt5_pZlXiQZKwZKYMgAyM5TzaFoYXuKVWf2R-gkdY/edit#gid=0", "TSLA"))
