from tests.helpers.support_functions import *

logged_page = 'page'
logged_page_return_button = 'retrun button'


def logged_page_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, logged_page)
    return elem.is_displayed()

def logged_page_log_out(driver_instance):
    elem = driver_instance.find_element_by_id(logged_page_return_button)
    elem.click()