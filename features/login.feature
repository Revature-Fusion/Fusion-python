Feature: Users and Admin can login to their account

  Scenario: Login to Fusion account
#    Given The User or admin are on the Login Page
#    When The user or admin clicks the Login button
#    Then They are taken to the Login page

    Given The User or Admin are on the Login Page
    When The User or Admin enter their username
    And The User or Admin enters their password
    And The User or Admin clicks on the login button
    Then They are able to login to the website