from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities# provide driver details
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DELAY = 3 # seconds
page_url = "https://apps.indraweb.net/registrohorario/#/dashboard/registro"

def login(driver):
    try:
        myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, 'login')))
        print("Page is ready!")

        driver.find_element_by_id("login").send_keys("username")
        print("Username")

        driver.find_element_by_id("passwd").send_keys("password")
        print("Password")

        driver.find_element_by_id("nsg-x1-logon-button").click()
        print("Logged")

    except TimeoutException:
        print("Too much time!")

def main():
    driver = webdriver.Firefox()
    driver.get(page_url)
    dir(driver)

    login(driver)
    #time()

    driver.close()

if __name__ == "__main__":
    main()