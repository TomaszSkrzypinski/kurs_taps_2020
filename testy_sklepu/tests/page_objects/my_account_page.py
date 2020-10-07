from testy_sklepu.tests.helpers.support_functions import *

my_account_header = '//*[@id="post-9"]/header/h1'


def my_account_header_visibility(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, my_account_header)
    return elem.is_displayed()