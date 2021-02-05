from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities# provide driver details

#selenium_driver_url = "http://127.0.0.1:4444/wd/hub"
#desired_capabilities = DesiredCapabilities.CHROME# creating instance of the WebDriver
#driver = webdriver.Remote(command_executor=selenium_driver_url, desired_capabilities=desired_capabilities)# navigate to provided page url

driver = webdriver.Firefox()

page_url = "https://www.python.org"
driver.get(page_url)# list of methods available on `driver` (optional)
dir(driver)# invoke full-screen operation
driver.fullscreen_window()# scroll through the page and take screenshots
driver.save_screenshot("screenshot_01.png")
driver.execute_script("window.scrollBy(0, 500)");
driver.save_screenshot("screenshot_02.png")
driver.execute_script("window.scrollBy(0, 500)");
driver.save_screenshot("screenshot_03.png")
driver.execute_script("window.scrollBy(0, 500)");
driver.save_screenshot("screenshot_04.png")
driver.execute_script("window.scrollBy(0, 500)");# exit the browser
driver.close()
