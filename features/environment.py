# features/environment.py (Versión Limpia y Simple para login)
from playwright.sync_api import sync_playwright

# Usamos before_all/after_all para la instancia principal de Playwright
def before_all(context):
    context.p = sync_playwright().start()

def after_all(context):
    if hasattr(context, 'p') and context.p:
        context.p.stop()

# Abre un nuevo 'browser' antes de cada escenario
def before_scenario(context, scenario):
    # La clave es lanzar el navegador
    context.browser = context.p.chromium.launch(headless=False)
    # y crear la 'page' dentro del contexto
    context.page = context.browser.new_page()

# Cierra solo el 'browser' después de cada escenario
def after_scenario(context, scenario):
    # Cierra context.browser, NO context.browser_context
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()