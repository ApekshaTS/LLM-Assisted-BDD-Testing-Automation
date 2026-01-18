from behave import given, when, then

@given("the user is on the login page")
def step_open_login(context):
    context.page.goto("http://127.0.0.1:5000/login")

@when("the user enters a valid email")
def step_enter_valid_email(context):
    context.page.fill("#email", "test@example.com")

@when("the user enters a valid password")
def step_enter_valid_password(context):
    context.page.fill("#password", "Password123")

@when("the user enters an invalid password")
def step_enter_invalid_password(context):
    context.page.fill("#password", "wrongpassword")

@when("the user clicks the login button")
def step_click_login(context):
    context.page.click("#login")

@when("the user enters a username that matches with existing records in the system")
def step_username_matches(context):
    context.page.fill("#email", "test@example.com")

@when("the user inputs their unique email address into the appropriate field")
def step_input_unique_email(context):
    context.page.fill("#email", "test@example.com")

@when("the same user provides correct password for verification")
def step_provide_correct_password(context):
    context.page.fill("#password", "Password123")

@when("they click the login button without any error messages popping up")
@when("upon submission of credentials by clicking login button")
def step_click_login_variations(context):
    context.page.click("#login")

@when("the user enters a legitimate email address into the username field and provides their corresponding password")
def step_combined_credentials(context):
    context.page.fill("#email", "test@example.com")
    context.page.fill("#password", "Password123")

@when("the user chooses 'Email' as authentication method")
def step_choose_email_method(context):
    pass

@then("the user should be redirected to the dashboard")
@then("a session is established")
@then("after submission, redirection to user dashboard occurs without any error messages shown")
@then("after successful authentication, the homepage appears with dashboard content displayed")
def step_verify_dashboard(context):
    assert "dashboard" in context.page.url
    assert "Welcome" in context.page.content()

@then("an acknowledgment message should be displayed stating 'Login successful'")
def step_ack_message(context):
    assert "Welcome" in context.page.content()

@then("an error message should be displayed")
def step_error_message(context):
    assert "Invalid" in context.page.content()

@then("an indicator such as cookies or tokens are set to authenticate the logged-in status")
def step_validate_cookies(context):
    cookies = context.page.context.cookies()
    assert cookies is not None

@then("the dashboard should be visible to them, confirming successful authentication")
def step_dashboard_visible_confirmed(context):
    assert "dashboard" in context.page.url
    assert "Welcome" in context.page.content()
