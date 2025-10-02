# features/steps/login_steps.py
from behave import given, when, then

from pages.elements.login_page_elements import LoginPageElements
from pages.login_page import LoginPage
from playwright.sync_api import expect
import time

@given('the user is on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    time.sleep(1)


@when('the user enters "{username}" as username and "{password}" as password')
def step_impl(context, username, password):
    if password == "empty_value":
        password = ""
    context.login_page.enter_credentials(username, password)


@when('the user clicks the login button')
def step_impl(context):
    context.login_page.click_login()
    time.sleep(2)  # Espera a que cargue el mensaje

@then('the user should be redirected to the secure area')
def step_impl(context):
    # Verificamos que la URL haya cambiado a la del área segura
    # El área segura tiene el path /secure
    expect(context.page).to_have_url("https://the-internet.herokuapp.com/secure")

    # También podemos verificar que el elemento de "Logout" exista
    # Esto es una validación más robusta de que estamos en la página correcta
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
    Combina los pasos para asegurar que el usuario esté en el estado de 'logueado'.
    Esto es mejor que repetir los pasos Given/When/And en Gherkin.
    """
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    # Usa credenciales válidas
    context.login_page.enter_credentials("tomsmith", "SuperSecretPassword!")
    context.login_page.click_login()

    # Asume que el login fue exitoso, verificando la URL
    expect(context.page).to_have_url(LoginPageElements.SECURE_AREA_URL)

@when('the user clicks the logout button')
def step_impl(context):
    context.login_page.click_logout()
    # Espera implícita de Behave/Playwright, pero puedes agregar un sleep si es necesario
    # time.sleep(1)

@then('the user should be on the login page')
def step_impl(context):
    """Verifica que la URL sea la de la página de login (la base)."""
    # La página de login es la URL base con el path /login
    expect(context.page).to_have_url("https://the-internet.herokuapp.com/login")

@then('the password input field should have type "{expected_type}"')
def step_impl(context, expected_type):
    """Verifica el atributo 'type' (debe ser 'password')."""
    actual_type = context.login_page.get_password_input_type()

    # Asersión
    assert actual_type == expected_type, \
        f"ERROR: Expected password field type to be '{expected_type}' but found '{actual_type}'"

@when('the user attempts to navigate directly to "{path}"')
def step_impl(context, path):
    """Navega directamente al path del área segura."""
    context.login_page.navigate_directly(path)
