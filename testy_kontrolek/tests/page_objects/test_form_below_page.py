from testy_kontrolek.tests.helpers.support_functions import *

test_form_tab = 'form-header'
test_form_content = 'form-content'
test_form_first_name_field = 'fname'
test_form_last_name_field = 'lname'
test_form_submit_button = 'formSubmitButton'



def click_test_form_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, test_form_tab)
    elem = driver_instance.find_element_by_id(test_form_tab)
    elem.click()


def test_form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, test_form_content)
    return elem.is_displayed()


def test_form_submit(driver_instance):
    elem1 = wait_for_visibility_of_element_by_id(driver_instance, test_form_first_name_field)
    elem1.click()
    elem1.send_keys('Jan')
    elem2 = wait_for_visibility_of_element_by_id(driver_instance, test_form_last_name_field)
    elem2.click()
    elem2.send_keys('Kowalski')
    elem3 = driver_instance.find_element_by_id(test_form_submit_button)
    elem3.click()


def alert_visibility(driver_instance):
    success = 'success'
    alert = driver_instance.switch_to.alert.text
    if alert == success:
        return True
    else:
        return False

