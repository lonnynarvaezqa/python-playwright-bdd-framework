from pages.base_page import BasePage
from pages.elements.login_page_elements import LoginPageElements
from config import AppConfig

class LoginPage(BasePage):

    def navigate(self):
        """Navega a la URL de login de práctica usando la configuración."""
        # Uso de la configuración
        self.page.goto(f"{AppConfig.BASE_URL}{AppConfig.LOGIN_PATH}")

    def enter_credentials(self, username, password):
        """Introduce el nombre de usuario y la contraseña."""
        self.page.fill(LoginPageElements.USERNAME_INPUT, username)
        self.page.fill(LoginPageElements.PASSWORD_INPUT, password)

    def click_login(self):
        """Hace clic en el botón de login."""
        self.page.click(LoginPageElements.LOGIN_BUTTON)

    def get_status_message(self):
        """Retorna el texto del mensaje de estado (éxito/fallo)."""
        # Usamos .text_content() y luego limpiamos el texto
        raw_text = self.page.inner_text(LoginPageElements.STATUS_MESSAGE)
        clean_text = raw_text.replace('\n', ' ').replace('×', '').strip()
        return clean_text
