from testy_kontrolek.tests.helpers.support_functions import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
basic_auth_username_field = 'ba_username'
basic_auth_password_field = 'ba_password'
basic_auth_login_button = '//*[@id="content"]/button'



def click_basic_auth_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, basic_auth_tab)
    elem = driver_instance.find_element_by_id(basic_auth_tab)
    elem.click()


def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_content)
    return elem.is_displayed()


def basic_auth_log_in(driver_instance):
    elem1 = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_username_field)
    elem1.click()
    elem1.send_keys('admin')
    elem2 = wait_for_visibility_of_element_by_id(driver_instance, basic_auth_password_field)
    elem2.click()
    elem2.send_keys('admin')
    elem3 = driver_instance.find_element_by_xpath(basic_auth_login_button)
    elem3.click()
