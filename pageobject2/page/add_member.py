from selenium.webdriver.common.by import By

from pageobject2.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("abcde")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("appppp")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("12345678901")
        self.driver.find_element_by_css_selector(".js_btn_save").click()

    def get_first(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#member_list tr:nth-child(1) td:nth-child(2)').get_attribute(
            "title")
