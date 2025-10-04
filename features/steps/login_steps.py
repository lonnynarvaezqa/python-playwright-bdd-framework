from behave import given, when, then

from pages.elements.login_page_elements import LoginPageElements
from pages.login_page import LoginPage
from playwright.sync_api import expect


# Removed 'import time'

@given('the user is on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    # Implicit wait: Playwright's navigate() waits for 'load' by default,
    # but we can explicitly wait for 'domcontentloaded' or an element if needed.
    context.page.wait_for_load_state("domcontentloaded")  # Wait for the basic page structure


@when('the user enters "{username}" as username and "{password}" as password')
def step_impl(context, username, password):
    if password == "empty_value":
        password = ""
    context.login_page.enter_credentials(username, password)


@when('the user clicks the login button')
def step_impl(context):
    context.login_page.click_login()
    # Replace time.sleep(2). Wait for the secure area redirect/load.
    # The 'then' step will handle the ultimate wait (URL change and element visibility).


@then('the user should be redirected to the secure area')
def step_impl(context):
    # This assertion acts as a robust explicit wait for the redirect
    expect(context.page).to_have_url("https://the-internet.herokuapp.com/secure")

    # Verify that the 'Logout' element exists, which also acts as an element visibility wait
    logout_button = context.page.locator("#content > div > a")
    expect(logout_button).to_be_visible()


@then('a message containing "{expected_text}" should be displayed')
def step_impl(context, expected_text):
    actual_message = context.login_page.get_status_message()
    assert expected_text in actual_message, \
        f"ERROR: Expected message to contain '{expected_text}' but found '{actual_message}'"


@given('the user is logged in')
def step_impl(context):
    """
    Combines steps to ensure the user is in the 'logged in' state.
    """
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    context.page.wait_for_load_state("domcontentloaded")

    # Use valid credentials
    context.login_page.enter_credentials("tomsmith", "SuperSecretPassword!")
    context.login_page.click_login()

    # Explicit wait for the redirect
    expect(context.page).to_have_url(LoginPageElements.SECURE_AREA_URL)


@when('the user clicks the logout button')
def step_impl(context):
    context.login_page.click_logout()
    # The 'then' step will wait for the final state


@then('the user should be on the login page')
def step_impl(context):
    """Verifies that the URL is the login page URL (/login)."""
    # Explicit wait for the final URL after logout
    expect(context.page).to_have_url("https://the-internet.herokuapp.com/login")


@then('the password input field should have type "{expected_type}"')
def step_impl(context, expected_type):
    """Verifies the 'type' attribute (should be 'password')."""
    actual_type = context.login_page.get_password_input_type()

    # Assertion
    assert actual_type == expected_type, \
        f"ERROR: Expected password field type to be '{expected_type}' but found '{actual_type}'"


@when('the user attempts to navigate directly to "{path}"')
def step_impl(context, path):
    """Navigates directly to the secure area path."""
    context.login_page.navigate_directly(path)
