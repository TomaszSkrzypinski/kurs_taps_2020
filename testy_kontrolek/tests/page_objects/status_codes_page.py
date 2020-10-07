from testy_kontrolek.tests.helpers.support_functions import *

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
status_code_200 = '200siteAnchor'
status_code_305 = '305siteAnchor'
status_code_404 = '404siteAnchor'
status_code_500 = '500siteAnchor'


def click_status_codes_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, status_codes_tab)
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_codes_content)
    return elem.is_displayed()


def click_status_code_200(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_code_200)
    elem.click()

def click_status_code_305(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_code_305)
    elem.click()


def click_status_code_404(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_code_404)
    elem.click()


def click_status_code_500(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, status_code_500)
    elem.click()