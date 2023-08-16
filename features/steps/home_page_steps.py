import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.path[0])))))
from pages.home_page import HomePage

use_step_matcher("parse")


@step('the user navigates to the home page')
def the_user_navigates_to_the_home_page(context) -> None:
    home_page = HomePage(context.browser)
    home_page.navigate()

@step('the calculation app should be displayed')
def the_calculation_app_should_be_displayed(context) -> None:
    home_page = HomePage(context.browser)
    home_page.title_is_loaded()

@step('the user clicks on the reset button')
def the_user_clicks_on_the_reset_button(context) -> None:
    home_page = HomePage(context.browser)
    home_page.click_on_reset_button()

@step('the user enters "{number_value}" number')
def the_user_enters_number(context, number_value) -> None:
    home_page = HomePage(context.browser)
    home_page.set_the_output_value(number_value)

@step('the user performs + calculation')
def the_user_performs_addition_calculation(context) -> None:
    home_page = HomePage(context.browser)
    home_page.click_on_plus_button()

@step('the user performs - calculation')
def the_user_performs_subtraction_calculation(context) -> None:
    home_page = HomePage(context.browser)
    home_page.click_on_minus_button()

@step('the user performs * calculation')
def the_user_performs_multiplication_calculation(context) -> None:
    home_page = HomePage(context.browser)
    home_page.click_on_multiplication_button()

@step('the user performs / calculation')
def the_user_performs_division_calculation(context) -> None:
    home_page = HomePage(context.browser)
    home_page.click_on_division_button()

@step('the output value should be "{output_value_expected}"')
def the_output_value_should_be(context, output_value_expected) -> None:
    home_page = HomePage(context.browser)
    home_page.verify_the_output_value(output_value_expected)
