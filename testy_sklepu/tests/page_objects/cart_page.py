from testy_sklepu.tests.helpers.support_functions import *

item_in_cart = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]'
remove_item_from_cart_button = '//*[@id="post-7"]/div/div/form/table/tbody/tr[1]/td[1]/a'
submit_cart = '//*[@id="post-7"]/div/div/div[2]/div/div/a'


def check_item_in_cart(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, item_in_cart)
    return elem.is_displayed()


def remove_item_from_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(remove_item_from_cart_button)
    elem.click()


def check_item_not_in_cart(driver_instance):
    try:
        wait_for_invisibility_of_element_by_xpath(driver_instance, item_in_cart)
        return True
    except NoSuchElementException:
        return False


def approve_cart(driver_instance):
    elem = driver_instance.find_element_by_xpath(submit_cart)
    elem.click()