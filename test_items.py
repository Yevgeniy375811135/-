from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_link(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button_is_present = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button_is_present, f"Button is not pesent on the page = {button_is_present}"
    time.sleep(15)