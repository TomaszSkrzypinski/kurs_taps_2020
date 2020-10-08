import unittest
from selenium import webdriver
from testy_kontrolek.config.test_settings import TestSettings
from testy_kontrolek.tests.page_objects import main_page, checkboxes_page, hovers_page, users_page, inputs_page, dropdown_page, \
    add_remove_page, date_picker_page, logged_page, basic_auth_page, test_form_below_page, key_presses_page, \
    status_codes_page, code_response_page, iframe_page, drag_and_drop_page


class Tests(unittest.TestCase):
    def setUp(self):
        #konfiguracja zdalnego drivera do pracy w selenium grid
        self.selenium_grid_url = 'http://192.168.56.1:4445/wd/hub'
        self.capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        self.driver = webdriver.Remote(desired_capabilities=self.capabilities, command_executor=self.selenium_grid_url)

        #self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test2_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test3_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test4_inputs_visibility(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.input_content_visible(self.driver))

    def test5_inputs_correct_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_correct_keys_to_input(self.driver))

    def test6_inputs_incorrect_input(self):
        inputs_page.click_inputs_tab(self.driver)
        self.assertTrue(inputs_page.send_incorrect_keys_to_input(self.driver))

    def test7_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visibility(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test8_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)

    def test9_delete_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_content_visible(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test10_date_picker(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        date_picker_page.change_date(self.driver)

    def test11_basic_auth_log_in(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.basic_auth_log_in(self.driver)
        self.assertTrue(logged_page.logged_page_displayed(self.driver))

    def test12_basic_auth_log_out(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.basic_auth_log_in(self.driver)
        self.assertTrue(logged_page.logged_page_displayed(self.driver))
        logged_page.logged_page_log_out(self.driver)
        self.assertTrue(main_page.content_visible(self.driver))

    def test13_test_form_submit(self):
        test_form_below_page.click_test_form_tab(self.driver)
        self.assertTrue(test_form_below_page.test_form_content_visible(self.driver))
        test_form_below_page.test_form_submit(self.driver)
        self.assertTrue(test_form_below_page.alert_visibility(self.driver))

    def test14_key_presses(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))
        self.assertTrue(key_presses_page.key_presses_press(self.driver))

    def test15_status_code_200(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_code_200(self.driver)
        self.assertTrue(code_response_page.response_200(self.driver))

    def test16_status_code_305(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_code_305(self.driver)
        self.assertTrue(code_response_page.response_305(self.driver))

    def test17_status_code_404(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_code_404(self.driver)
        self.assertTrue(code_response_page.response_404(self.driver))

    def test18_status_code_500(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_code_500(self.driver)
        self.assertTrue(code_response_page.response_500(self.driver))

    def test19_iframe(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))
        self.assertTrue(iframe_page.click_buttons(self.driver))

    def test20_drag_and_drop(self):
        drag_and_drop_page.click_drag_and_drop_tab(self.driver)
        self.assertTrue(drag_and_drop_page.drag_and_drop_content_visible(self.driver))
        self.assertTrue(drag_and_drop_page.drag_and_drop_square(self.driver))


        if __name__ == '__main__':
            unittest.main()