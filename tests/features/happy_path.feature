Feature: Happy Path Scenario

Scenario: Successful login with correct credentials
  Given the user is on the login page
  When the user enters a legitimate email address into the username field and provides their corresponding password
  And they click the login button without any error messages popping up
  Then the dashboard should be visible to them, confirming successful authentication