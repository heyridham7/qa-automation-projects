Feature: Login functionality
  As a user
  I want to login to the website
  So that I can access my account

  Scenario: Valid login
    Given I am on the login page
    When I enter username "scroll" and password "scroll"
    And I click the login button
    Then I should be logged in successfully

  Scenario: Empty login
    Given I am on the login page
    When I click the login button
    Then I should still be on the login page