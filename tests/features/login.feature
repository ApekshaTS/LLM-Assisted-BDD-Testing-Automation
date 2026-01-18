Feature: Login functionality using Email & Password

Scenario: Successful login with correct credentials
  Given the user is on the login page
  When the user enters a legitimate email address into the username field and provides their corresponding password
  And they click the login button without any error messages popping up
  Then the dashboard should be visible to them, confirming successful authentication

Scenario: Failed login attempt with incorrect credentials - negative path one
  Given the user is on the login page
  When the user enters a legitimate email address into the username field and provides an invalid password for their account
  And they click the login button without any error messages popping up
  Then no dashboard should be visible, indicating authentication failure. Instead, there may appear errors or prompts to enter correct credentials