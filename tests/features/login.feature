Feature: Login functionality using Email and Password credentials

Scenario: Successful user authentication when provided correct email and password
  Given the user is on the login page
  When the user enters a valid username via email input field And submits it with correct password through password field
  Then an acknowledgment message should be displayed stating 'Login successful'
And after submission, redirection to user dashboard occurs without any error messages shown

Scenario: Unsuccessful authentication when provided incorrect credentials
  Given the user is on the login page
  When the user enters a valid username via email input field And attempts to submit with an incorrect password through password field
  Then validation message should be displayed stating 'Invalid Password' and no redirection occurs
And after submission, staying on login page without going away or redirecting anywhere
