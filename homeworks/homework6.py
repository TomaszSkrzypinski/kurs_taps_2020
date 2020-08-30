from selenium import webdriver


driver = webdriver.Chrome('C:\kurs_taps_2020\chromedriver.exe')
driver.maximize_window()
fabryka = driver.get('https://fabrykatestow.pl/')
xpath1 = '//*[@id="menu-item-506"]/a'
driver.find_element_by_xpath(xpath1).click()
xpath2 = '//*[@id="content"]/div/div/div/div/div/div/div/section[8]/div/div/div/div/div/div/div/h2'
driver.find_element_by_xpath(xpath2).location_once_scrolled_into_view
driver.get_screenshot_as_file('d://pawel.jpg')
driver.quit()
