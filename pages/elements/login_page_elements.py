# pages/elements/login_page_elements.py

class LoginPageElements:
    """Clase que contiene todos los selectores de la página de Login."""

    # Campo de Nombre de Usuario
    USERNAME_INPUT = "#username"

    # Campo de Contraseña
    PASSWORD_INPUT = "#password"

    # Botón de Login
    LOGIN_BUTTON = ".fa.fa-2x.fa-sign-in"

    # Mensaje de Estado (Éxito o Fallo)
    STATUS_MESSAGE = "#flash"

    # Botón de Logout (para verificar la redirección a secure area)
    LOGOUT_BUTTON = "#content > div > a"

    # URL esperada después del login exitoso
    SECURE_AREA_URL = "https://the-internet.herokuapp.com/secure"

    # Botón de Logout (ya lo teníamos, solo lo mantenemos)
    LOGOUT_BUTTON = "#content > div > a"

    # Campo de Contraseña (ya lo teníamos)
    PASSWORD_INPUT = "#password"

    # URL esperada después del login exitoso (ya lo teníamos)
    SECURE_AREA_URL = "https://the-internet.herokuapp.com/secure"

