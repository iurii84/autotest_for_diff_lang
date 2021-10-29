import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_have_btn_to_add_items_to_basket(browser):
    browser.get(link)

    elements_found = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    count_elements = len(elements_found)
    assert count_elements == 1, "Qty of found elements is not equal to 1"
