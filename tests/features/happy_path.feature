Feature: Happy Path Scenario

Scenario: Successful user authentication when provided correct email and password
  Given the user is on the login page
  When the user enters a valid username via email input field And submits it with correct password through password field
  Then an acknowledgment message should be displayed stating 'Login successful'
And after submission, redirection to user dashboard occurs without any error messages shown