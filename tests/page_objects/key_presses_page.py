from tests.helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

key_presses_tab = 'keypresses-header'
key_presses_content = 'keypresses-content'
key_presses_field = 'target'
key_presses_result = 'keyPressResult'

def click_key_presses_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, key_presses_tab)
    elem = driver_instance.find_element_by_id(key_presses_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_content)
    return elem.is_displayed()


def key_presses_press(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, key_presses_field)
    elem.click()
    elem.send_keys(Keys.ENTER)
    result = driver_instance.find_element_by_id(key_presses_result).get_attribute("outerHTML")
    if result == '<p id="keyPressResult" style="color:green">You entered: ENTER</p>':
        a = 1
    else:
        a = 0
    elem.send_keys(Keys.BACKSPACE)
    result = driver_instance.find_element_by_id(key_presses_result).get_attribute("outerHTML")
    if result == '<p id="keyPressResult" style="color:green">You entered: BACK_SPACE</p>':
        b = 1
    else:
        b = 0
    elem.send_keys(Keys.ESCAPE)
    result = driver_instance.find_element_by_id(key_presses_result).get_attribute("outerHTML")
    if result == '<p id="keyPressResult" style="color:green">You entered: ESCAPE</p>':
        c = 1
    else:
        c = 0
    if a == 1 and b == 1 and c ==1:
        return True
    else:
        return False


