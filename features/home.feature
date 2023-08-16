Feature: Calculator
As a user, I want to calculate the integer number within the online calculator web-app

@regression
Scenario: The Calculation App Should Be Displayed Properly
    When the user navigates to the home page
    Then the calculation app should be displayed

@regression
Scenario Outline: The User Should Be Able To Calculate The Integer Number Properly
    Given the user navigates to the home page
    When the user enters "<first_number_value>" number
    And the user enters "<second_number_value>" number
    And the user performs "<calculation_type>" calculation 
    Then the output value should be "<output_value_expected>"

Examples:

      | first_number_value  | second_number_value  | calculation_type | output_expected |     
      | 1                   | 2                    | +                | 3               |
      | 111111111           | -2                   | +                | 111111109       |
      | 2                   | 1                    | -                | 1               |
      | -111111111          | 2                    | -                | -111111113      |
      | 3                   | 2                    | *                | 6               |
      | 111111111           | -2                   | *                | -222222222      |
      | 10                  | 2                    | /                | 5               |
      | -888888888          | 2                    | /                | -444444444      |

@regression
Scenario Outline: The User Should Be Able To Clear The Input Value Properly
    Given the user navigates to the home page
    When the user enters "<unexpected_number_value>" number
    And the user clicks on the reset button
    Then the output value should be "0"

Examples:

      | unexpected_number_value  |     
      | 2                        |
      | -2                       |

