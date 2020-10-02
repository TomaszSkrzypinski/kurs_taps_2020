import os
from tests.helpers.support_functions import *

drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
result = '//*[@id="column-a"]/header'


def click_drag_and_drop_tab(driver_instance):
    wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_tab)
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def drag_and_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_id(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def drag_and_drop_square(driver_instance):
    with open(os.path.abspath('C:\kurs_taps_2020\config\dnd.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()
        driver_instance.execute_script(script + "$('column-a').simulateDragDrop({ dropTarget: 'column-b'});")
    elem = driver_instance.find_element_by_xpath(result)
    print(elem.text)