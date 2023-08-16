from typing import Any
from selenium.webdriver.common.by import By
from pages.base_page import Base


class HomePage(Base):
    """This class is used for handling the calculation web-app"""
    
    #Constructor
    def __init__(self, browser) -> None:
        super().__init__(browser)

    # Selectors
    def get_plus_button(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.PLUS_BUTTON, \
            'Unable to find the plus button !!!')

    def get_minus_button(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.MINUS_BUTTON, \
            'Unable to find the minus button !!!')

    def get_multiplication_button(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.MULTIPLICATION_BUTTON, \
            'Unable to find the multiplication button !!!')

    def get_division_button(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.DIVISION_BUTTON, \
            'Unable to find the division button !!!')

    def get_reset_button(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.RESET_BUTTON, \
            'Unable to find the reset button !!!')

    def get_output_textbox(self) -> Any:
        return self.browser.find_visible_element(HomePageLocators.OUTPUT_TEXTBOX, \
            'Unable to find the output textbox !!!')

    # Methods
    def navigate(self) -> None:
        self.browser.get(HomePageLocators.PAGE_URL)
        self.browser.maximize_window()

    def click_on_plus_button(self) -> None:
        self.get_plus_button().click()

    def click_on_minus_button(self) -> None:
        self.get_minus_button().click()

    def click_on_multiplication_button(self) -> None:
        self.get_multiplication_button().click()

    def click_on_division_button(self) -> None:
        self.get_division_button().click()

    def click_on_reset_button(self) -> None:
        self.get_reset_button().click()

    def set_the_output_value(self, output_value) -> None:
        #TODO: Set the value of the output textbox
        raise NotImplementedError

    # Assertions
    def title_is_loaded(self) -> bool:
        return self.browser.title.__eq__(HomePageLocators.TITLE)

    def verify_the_output_value(self, the_output_value_expected) -> bool:
        the_output_textbox = self.get_output_textbox()
        return (the_output_textbox != None and the_output_textbox.text == the_output_value_expected)

class HomePageLocators(object):
    """This class is used for handling locators on the calculation web-app"""
    
    PAGE_URL = "https://www.online-calculator.com/"
    TITLE = 'Full Screen Calculator - Online Calculator'
    PLUS_BUTTON = (By.ID, 'btnPlus')
    MINUS_BUTTON = (By.ID, 'btnMinus')
    MULTIPLICATION_BUTTON = (By.ID, 'btnMultiplication')
    DIVISION_BUTTON = (By.ID, 'btnDivision')
    RESET_BUTTON = (By.ID, 'btnReset')
    OUTPUT_TEXTBOX = (By.ID, 'txtOutput')