import os
from testy_kontrolek.tests.helpers.support_functions import *

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
result = '//*[@id="column-a"]/header'
dnd_file = 'C:\kurs_taps_2020\\testy_kontrolek\config\dnd.js'


def click_drag_and_drop_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_tab)
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_square(driver_instance):
    with open(os.path.abspath(dnd_file), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()
    driver_instance.execute_script(script + " jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    elem = driver_instance.find_element_by_xpath(result)
    if elem.text == 'B':
        a = 1
    else:
        a = 0
    driver_instance.execute_script(script + " jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    elem = driver_instance.find_element_by_xpath(result)
    if elem.text == 'A':
        b = 1
    else:
        b = 0
    driver_instance.execute_script(script + " jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    elem = driver_instance.find_element_by_xpath(result)
    if elem.text == 'B':
        c = 1
    else:
        c = 0
    if a == 1 and b == 1 and c == 1:
        return True
    else:
        return False
