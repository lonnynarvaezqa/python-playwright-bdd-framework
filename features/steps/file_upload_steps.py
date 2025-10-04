from behave import given, when, then
from pages.file_upload_page import FileUploadPage
from playwright.sync_api import expect
import os
from pages.elements.file_upload_elements import FileUploadElements
from pages.login_page import LoginPage # Needed for the shared step



@given('the user is on the File Upload page')
def step_impl(context):
    context.file_upload_page = FileUploadPage(context.page)
    context.file_upload_page.navigate()
    context.page.wait_for_load_state("domcontentloaded")
    from pages.login_page import LoginPage
    context.login_page = LoginPage(context.page)


@when('the user selects a file named "{file_name}"')
def step_impl(context, file_name):
    # Construct the full path to the test file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    file_path = os.path.join(project_root, 'test_data', file_name)

    # Call the POM method to select and upload the file
    context.file_upload_page.select_file(file_path)


@when('the user clicks the upload button')
def step_impl(context):
    context.file_upload_page.click_upload_button()
    context.page.wait_for_load_state("domcontentloaded")


@then('the uploaded file name "{expected_file_name}" should be displayed')
def step_impl(context, expected_file_name):
    actual_name = context.file_upload_page.get_uploaded_file_name()

    assert expected_file_name.strip() == actual_name.strip(), \
        f"ERROR: Expected uploaded file name to be '{expected_file_name}' but found '{actual_name}'"
