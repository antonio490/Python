from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities# provide driver details
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv


ALLLINKS = "showAllLink"
COOKIES = "didomi-notice-agree-button"
CONTAINER = "items-container discard-animation-core-vitals"

DELAY = 3 # seconds
URL = "https://www.idealista.com/"

def applySearch(driver, filter):
    try:
        myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, 'campoBus')))
        print("Page is ready!")

        driver.find_element_by_id("campoBus").send_keys(filter)
        print("Search on Madrid")

        driver.find_element_by_id("btn-free-search").click()
        print("click search")


        if driver.find_element_by_id(COOKIES):
            driver.find_element_by_id(COOKIES).click()


    except TimeoutException:
        print("Too much time!")

def countElements(driver):
    num = driver.find_element_by_id("h1-container").get_attribute('textContent')
    return num

def writeToCSV(driver):
    # with open('idealista.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter = '|')
    #     writer.writerow(["Name", "Price", "Location", "Description", "Garage"])

    lots = []
    for person in driver.find_elements_by_class_name(CONTAINER):
        title = person.find_element_by_xpath('.//div[@class="title"]/a').text
        company = person.find_element_by_xpath('.//div[@class="price-row"]/a').text

        lots.append({'title': title, 'company': company})

    print(lots)


def main():
    driver = webdriver.Firefox()
    driver.get(URL)
    dir(driver)

    applySearch(driver, "Madrid")
    # num = countElements(driver)
    # print(num)
    writeToCSV(driver)

    #driver.close()

if __name__ == "__main__":
    main()
