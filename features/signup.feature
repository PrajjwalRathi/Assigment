Feature: User Signup and Login

  Scenario: Successfully create a new account
    Given I am on the signup page
    When I enter valid information in all required fields
    And I submit the signup form
    Then I should be redirected to the account dashboard
    And I should see a confirmation message for account creation

  Scenario: Log in with valid credentials
    Given I have an existing account
    And I am on the login page
    When I enter valid login credentials
    And I submit the login form
    Then I should be redirected to the account dashboard

  Scenario: Log in with invalid credentials
    Given I am on the login page
    When I enter an invalid username or password
    And I submit the login form
    Then I should see an error message indicating invalid credentials
