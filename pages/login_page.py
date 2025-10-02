# pages/login_page.py
from pages.base_page import BasePage
from playwright.sync_api import expect
from pages.elements.login_page_elements import LoginPageElements

class LoginPage(BasePage):

    def navigate(self):
        """Navega a la URL de login de práctica."""
        self.page.goto("https://the-internet.herokuapp.com/login")

    def enter_credentials(self, username, password):
        """Introduce el nombre de usuario y la contraseña."""
        # USAMOS EL NUEVO NOMBRE DE CLASE LoginPageElements.USERNAME_INPUT
        self.page.fill(LoginPageElements.USERNAME_INPUT, username)
        self.page.fill(LoginPageElements.PASSWORD_INPUT, password)

    def click_login(self):
        """Hace clic en el botón de login."""
        self.page.click(LoginPageElements.LOGIN_BUTTON)

    def get_status_message(self):
        """Retorna el texto limpio del mensaje de estado (éxito/fallo)."""

        # 1. Obtiene el contenido de texto
        raw_text = self.page.inner_text(LoginPageElements.STATUS_MESSAGE)

        # 2. Limpia los caracteres problemáticos
        #    - Reemplaza el salto de línea por espacio
        #    - Elimina el carácter de cierre '×'
        #    - Elimina espacios en blanco al inicio/fin (strip())
        clean_text = raw_text.replace('\n', ' ').replace('×', '').strip()

        return clean_text

    def click_logout(self):
        """Hace clic en el botón de Logout."""
        self.page.click(LoginPageElements.LOGOUT_BUTTON)

    def navigate_directly(self, path):
        """Navega a un path relativo, usado para acceder al área segura."""
        base_url = "https://the-internet.herokuapp.com"
        self.page.goto(f"{base_url}{path}")

    def get_password_input_type(self):
        """Retorna el atributo 'type' del campo de contraseña."""
        # Usa el método locator para interactuar con el elemento
        return self.page.locator(LoginPageElements.PASSWORD_INPUT).get_attribute("type")
