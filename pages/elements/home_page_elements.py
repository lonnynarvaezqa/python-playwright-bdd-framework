# pages/elements/home_page_elements.py

class HomePageElements:
    """Selectores para la página principal (Landing Page)."""

    # Localizador genérico para un enlace basado en su texto (Playwright lo hace fácil)
    LINK_BY_TEXT = lambda text: f"text={text}"

    # URL de la página principal (la base para todas las pruebas)
    BASE_URL = "https://the-internet.herokuapp.com/"

    # Ejemplo de un enlace específico (opcional)
    # HORIZONTAL_SLIDER_LINK = "a[href='/horizontal_slider']"