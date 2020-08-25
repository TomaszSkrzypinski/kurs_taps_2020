from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, xpath):
    element = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()


def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=10):
    try:
        element = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located(By.XPATH, xpath))
    except TimeoutException:
        element = False
    return element


def wait_for_invisibility_of_element(driver_instance, xpath, time_to_wait=10):
    inv_element = WebDriverWait(driver_instance, time_to_wait).until(EC.invisibility_of_element_located(By.XPATH, xpath))
    return inv_element
