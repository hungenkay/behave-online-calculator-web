from typing import Any
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self, browser) -> None:
        self.browser = browser

    def find_visible_element(self, by, error_message='') -> Any:
        element = self.wait.until(EC.visibility_of_any_element_located(by), error_message)
        return element

    def find_visible_elements(self, by, parent_element=None) -> Any:
        elements = self.driver.find_elements(*by) if parent_element is None else parent_element.find_elements(*by)
        visible_elements = [element for element in elements if element.is_displayed()]
        return visible_elements