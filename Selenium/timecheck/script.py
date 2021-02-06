from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities# provide driver details
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DELAY = 5 # seconds
page_url = "https://apps.indraweb.net/registrohorario/#/dashboard/registro"
keyFILE = "/home/antonio/INDRA.key"

def credentials():
    creds = {}
    with open(keyFILE) as file:
        for line in file:
            key, value = line.strip().split('=')
            creds[key] = value
    return creds

def login(driver, creds):
    try:
        WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, 'login')))

        driver.find_element_by_id("login").send_keys(creds["username"])
        driver.find_element_by_id("passwd").send_keys(creds["password"])

        driver.find_element_by_id("nsg-x1-logon-button").click()
        print("Logged")

    except TimeoutException:
        print("Too much time!")

def registerTime(driver):
        try:
            WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, 'content2')))

            if driver.find_element_by_class_name("alone"):
                btnEnd = driver.find_element_by_class_name("alone")
                btnEnd.find_element_by_class_name("c-button").click()

                WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, 'button-box')))

                btn = driver.find_element_by_class_name("button-box")
                btn.find_element_by_class_name("c-button").click()

                print("Jornada registrada")

            else:
                btnStart = driver.find_element_by_class_name("content2")
                btnStart.find_element_by_class_name("c-button").click()
                print("Jornada iniciada")



        except TimeoutException:
            print("Too much time!")

def main():
    driver = webdriver.Firefox()
    driver.get(page_url)
    dir(driver)

    creds = credentials()
    login(driver, creds)
    registerTime(driver)

    driver.close()

if __name__ == "__main__":
    main()
