from testy_kontrolek.tests.helpers.support_functions import *

hovers_tab = 'hovers-header'
hovers_content = 'hovers-content'
gentleman_pic = '//*[@id="hovers-content"]/div/div[1]/img'
gentleman_link = '//*[@id="hovers-content"]/div/div[1]/div/a'


def click_hovers_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, hovers_tab)
    elem = driver_instance.find_element_by_id(hovers_tab)
    elem.click()


def hover_content_displayed(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, hovers_content)
    return elem.is_displayed()


def hover_over_element_and_click(driver_instance):
    hover_over_element_by_xpath(driver_instance, gentleman_pic)
    elem = driver_instance.find_element_by_xpath(gentleman_link)
    elem.click()