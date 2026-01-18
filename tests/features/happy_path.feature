Feature: Happy Path Scenario

Scenario: Successful login attempt when user enters correct email and password combination
  Given the user is on the login page
  When the user enters a username that matches with existing records in the system
  And the user chooses 'Email' as authentication method
  And the user inputs their unique email address into the appropriate field
  And the same user provides correct password for verification
  And upon submission of credentials by clicking login button
  Then a session is established
  And an indicator such as cookies or tokens are set to authenticate the logged-in status
  And after successful authentication, the homepage appears with dashboard content displayed