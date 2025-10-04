from behave import given, when, then
from pages.home_page import HomePage
from playwright.sync_api import expect
# Removed 'import time'
import re


# Reusable step for setup
@given('the user is on the main landing page')
def step_impl(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate()
    context.page.wait_for_load_state("domcontentloaded")


@when('the user clicks the link titled "{link_text}"')
def step_impl(context, link_text):
    context.home_page.click_link_by_text(link_text)
    # Wait for the navigation to complete. This is explicit and more reliable.
    context.page.wait_for_load_state("domcontentloaded")


@then('the user should be redirected to the URL containing "{partial_url}"')
def step_impl(context, partial_url):
    """Verifies that the current URL contains the expected part using re."""

    # KEY CHANGE: Use re.compile to create a containment pattern
    # This searches for the partial_url anywhere in the URL string.
    pattern = re.compile(partial_url)

    # Use to_have_url with the pattern argument. This automatically waits for the match.
    expect(context.page).to_have_url(pattern)


@then('the page header should display "{expected_header}"')
def step_impl(context, expected_header):
    """Verifies the text of the new page's main header."""
    actual_header = context.home_page.get_page_header()

    # Use .strip() to ignore any extra whitespace, ensuring robust assertion.
    assert expected_header.strip() == actual_header.strip(), \
        f"ERROR: Expected page header '{expected_header}' but found '{actual_header}'"
