from testy_sklepu.tests.helpers.support_functions import *
from selenium.webdriver.support.select import Select
from testy_sklepu.tests.helpers.DataGenerator import *

name = 'billing_first_name'
surname = 'billing_last_name'
dropdown_country = 'billing_country'
street = 'billing_address_1'
postcode = 'billing_postcode'
city = 'billing_city'
phone = 'billing_phone'
email = 'billing_email'
place_order_button = 'place_order'

valid_postcode = '00-123'
invalid_postcode = 'abc'


def form_add_proper_name(driver_instance):
    elem = driver_instance.find_element_by_id(name)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_name(driver_instance):
    elem = driver_instance.find_element_by_id(name)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_surname(driver_instance):
    elem = driver_instance.find_element_by_id(surname)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_surname(driver_instance):
    elem = driver_instance.find_element_by_id(surname)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def get_first_dropdown_value(driver_instance):
    elem_list = Select(driver_instance.find_element_by_id(dropdown_country))
    wait_for_visibility_of_element_by_id(driver_instance, dropdown_country, 1)
    elem_list.select_by_index(1)


def form_add_proper_street(driver_instance):
    elem = driver_instance.find_element_by_id(street)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_street(driver_instance):
    elem = driver_instance.find_element_by_id(street)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_city(driver_instance):
    elem = driver_instance.find_element_by_id(city)
    elem.send_keys(DataGenerator.generateProperName())


def form_add_wrong_city(driver_instance):
    elem = driver_instance.find_element_by_id(city)
    elem.send_keys(DataGenerator.generateWrongName(DataGenerator()))


def form_add_proper_postcode(driver_instance):
    elem = driver_instance.find_element_by_id(postcode)
    elem.send_keys(valid_postcode)

def form_add_wrong_postcode(driver_instance):
    elem = driver_instance.find_element_by_id(postcode)
    elem.send_keys(invalid_postcode)


def form_add_proper_phone(driver_instance):
    elem = driver_instance.find_element_by_id(phone)
    elem.send_keys(DataGenerator.generateProperMobileNumber(DataGenerator()))


def form_add_wrong_phone(driver_instance):
    elem = driver_instance.find_element_by_id(phone)
    elem.send_keys(DataGenerator.generateWrongMobileNumber(DataGenerator()))


def form_add_proper_email(driver_instance):
    elem = driver_instance.find_element_by_id(email)
    elem.send_keys(DataGenerator.generateProperEmail())


def form_add_wrong_email(driver_instance):
    elem = driver_instance.find_element_by_id(email)
    elem.send_keys(DataGenerator.generateWrongEmail())


def proper_fill_all_form_areas(driver_instance):
    form_add_proper_name(driver_instance)
    form_add_proper_surname(driver_instance)
    get_first_dropdown_value(driver_instance)
    form_add_proper_street(driver_instance)
    form_add_proper_city(driver_instance)
    form_add_proper_postcode(driver_instance)
    form_add_proper_phone(driver_instance)
    form_add_proper_email(driver_instance)


def submit_order(driver_instance):
    elem = driver_instance.find_element_by_id(place_order_button)
    elem.click()