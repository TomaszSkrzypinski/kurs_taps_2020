from testy_kontrolek.tests.helpers.support_functions import *

response = '/html/body/pre'


def response_200(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, response)
    if elem.text == '200 OK':
        return True
    else:
        return False


def response_305(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, response)
    if elem.text == '305 Use Proxy':
        return True
    else:
        return False


def response_404(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, response)
    if elem.text == '404 Not Found':
        return True
    else:
        return False


def response_500(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, response)
    if elem.text == '500 Internal Server Error':
        return True
    else:
        return False
