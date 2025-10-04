from pages.base_page import BasePage
from pages.elements.login_page_elements import LoginPageElements
from config import AppConfig

class LoginPage(BasePage):

    def navigate(self):
        """Navigates to the practice login URL using the application configuration."""
        # Use configuration settings
        self.page.goto(f"{AppConfig.BASE_URL}{AppConfig.LOGIN_PATH}")

    def enter_credentials(self, username, password):
        """Enters the username and password."""
        self.page.fill(LoginPageElements.USERNAME_INPUT, username)
        self.page.fill(LoginPageElements.PASSWORD_INPUT, password)

    def click_login(self):
        """Clicks the login button."""
        self.page.click(LoginPageElements.LOGIN_BUTTON)

    def click_logout(self):
        """Clicks the logout button on the secure area page."""
        self.page.click(LoginPageElements.LOGOUT_BUTTON)

    def get_password_input_type(self):
        """Returns the value of the 'type' attribute for the password input field."""
        # Note: Playwright's get_attribute auto-waits for the element to be visible/enabled
        return self.page.get_attribute(LoginPageElements.PASSWORD_INPUT, "type")

    def navigate_directly(self, path):
        """Navigates directly to a given path relative to the BASE_URL."""
        self.page.goto(f"{AppConfig.BASE_URL}{path}")

    def get_status_message(self):
        """Returns the text of the status message (success/failure)."""
        raw_text = self.page.inner_text(LoginPageElements.STATUS_MESSAGE, timeout=5000)  # 5 segundos de espera
        clean_text = raw_text.replace('\n', ' ').replace('×', '').strip()
        return clean_text
