# pages/home_page.py
from pages.base_page import BasePage
from pages.elements.home_page_elements import HomePageElements
from pages.elements.generic_page_elements import GenericPageElements

class HomePage(BasePage):

    def navigate(self):
        """Navega a la URL principal."""
        self.page.goto(HomePageElements.BASE_URL)

    def click_link_by_text(self, link_text):
        """Hace clic en un enlace por su texto visible."""
        # Playwright localiza elementos por texto de forma nativa
        self.page.click(HomePageElements.LINK_BY_TEXT(link_text))

    def get_page_header(self):
        """Obtiene el texto del encabezado principal de la página."""
        return self.page.inner_text(GenericPageElements.PAGE_HEADER)