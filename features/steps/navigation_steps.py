# features/steps/navigation_steps.py
from behave import given, when, then
from pages.home_page import HomePage
from playwright.sync_api import expect
import time
import re


# Paso reutilizable para el setup
@given('the user is on the main landing page')
def step_impl(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate()
    time.sleep(1)


@when('the user clicks the link titled "{link_text}"')
def step_impl(context, link_text):
    context.home_page.click_link_by_text(link_text)
    # Esperamos que la navegación se complete
    context.page.wait_for_load_state("domcontentloaded")


@then('the user should be redirected to the URL containing "{partial_url}"')
def step_impl(context, partial_url):
    """Verifica que la URL actual contenga la parte esperada usando re."""

    # 🚨 CAMBIO CLAVE: Usamos re.compile para crear un patrón de contención
    # Esto busca el partial_url en cualquier parte de la cadena de URL
    pattern = re.compile(partial_url)

    # 🚨 Usamos to_have_url con el argumento de patrón
    expect(context.page).to_have_url(pattern)


@then('the page header should display "{expected_header}"')
def step_impl(context, expected_header):
    """Verifica el texto del encabezado principal de la nueva página."""
    actual_header = context.home_page.get_page_header()

    # Usamos .strip() para ignorar cualquier espacio en blanco extra, como hicimos antes.
    assert expected_header.strip() == actual_header.strip(), \
        f"ERROR: Expected page header '{expected_header}' but found '{actual_header}'"
