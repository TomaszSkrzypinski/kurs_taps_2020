from testy_kontrolek.tests.helpers.support_functions import *

date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker = 'start'


def click_date_picker_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, date_picker_tab)
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, date_picker_content)
    return elem.is_displayed()


def change_date(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, date_picker)
    elem.click()
    elem.send_keys('1022')
    value = '2020-10-22'
    if value == elem.get_attribute('value'):
        return True
    else:
        return False
