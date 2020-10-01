from tests.helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
squareA = '//*[@id="column-a"]'
squareB = '//*[@id="column-b"]'
result = '//*[@id="column-a"]/header'


def click_drag_and_drop_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_tab)
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_square(driver_instance):
    source_element = driver_instance.find_element_by_xpath(squareA)
    dest_element = driver_instance.find_element_by_xpath(squareB)
    ActionChains(driver_instance).click_and_hold(source_element).pause(4).move_to_element(dest_element).release(source_element).perform()
    sleep(3)

    elem = driver_instance.find_element_by_xpath(result)
    print(elem.text)