Feature: Users and Guests can sign up for an account

  Scenario: Register new account
    Given The User is on the Register Page
    When They navigate to the register form
    And They enter their Role, Email, First Name, Last Name, Username, Password
    And They click the Register button
    Then The form is submitted and they are able to login


  Scenario: Guest signs up
    Given The Guest is on the Register Page
    When They navigate to the guest form
    And They enter their Email, First Name, Last Name
    And They click on the Submit button
    Then The information is saved for them


