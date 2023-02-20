from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button(browser):
    browser.get(link)
    time.sleep(30)
    button_is_present = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button_is_present, f"Button is not pesent on the page "
    