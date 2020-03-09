# Created by Ademola Bhadmus at 06/03/2020
Feature: Registration Validation
  This Describes the steps to validate Registration of a user

  Scenario: Steps to validate a user registration that already exists.
    Given I am on the saloodo web page.
    When I clicked on the Register button.
    And I click on the Register Your Company Option.
    And I filled my details in the form that is displayed.
    And I click create account button.
    Then It should NOT be successful.


  Scenario: Steps to Login as a user
    Given I am on the saloodo web page.
    When I click on the login button.
    And I insert my email and password.
    And I click the login button.
    Then I should be directed to the dashboard.


  Scenario: Steps to add a details to a user's profile.

    When I click my profile name.
    And I click the general option.
    And I click the edit option under company.
    And I fill in the valid details.
    And I click on update profile.
    Then It should be successful.

