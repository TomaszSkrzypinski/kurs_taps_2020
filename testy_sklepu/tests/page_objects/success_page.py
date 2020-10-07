from testy_sklepu.tests.helpers.support_functions import *

success_order_page_content = 'primary'


def success_page_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, success_order_page_content)
    return elem.is_displayed
