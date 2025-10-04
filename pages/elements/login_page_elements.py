class LoginPageElements:
    """Class containing all selectors for the Login page."""

    # Username input field
    USERNAME_INPUT = "#username"

    # Password input field
    PASSWORD_INPUT = "#password"

    # Login button
    LOGIN_BUTTON = ".fa.fa-2x.fa-sign-in"

    # Status message (Success or Failure)
    STATUS_MESSAGE = "#flash"

    # Logout button (found on the secure area page)
    LOGOUT_BUTTON = "#content > div > a"

    # Expected URL after successful login
    SECURE_AREA_URL = "https://the-internet.herokuapp.com/secure"
