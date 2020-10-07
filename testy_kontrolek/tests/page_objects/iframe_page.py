from testy_kontrolek.tests.helpers.support_functions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe = '//*[@id="iframe-content"]/div/div/iframe'
button1 = 'simpleButton1'
button2 = 'simpleButton2'
response = 'whichButtonIsClickedMessage'

def click_iframe_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, iframe_tab)
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, iframe_content)
    return elem.is_displayed()


def click_buttons(driver_instance):
    driver_instance.switch_to.frame(driver_instance.find_element_by_xpath(iframe))
    but1 = wait_for_visibility_of_element_by_id(driver_instance, button1)
    but2 = wait_for_visibility_of_element_by_id(driver_instance, button2)
    but1.click()
    resp = driver_instance.find_element_by_id(response)
    if resp.text == 'Button 1 was clicked!':
        a = 1
    else:
        a = 0
    but2.click()
    resp = driver_instance.find_element_by_id(response)
    if resp.text == 'Button 2 was clicked!':
        b = 1
    else:
        b = 0
    if a == 1 and b == 1:
        return True
    else:
        return False