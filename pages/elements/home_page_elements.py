class HomePageElements:
    """Selectors for the main landing page."""

    # Generic locator for a link based on its text (Playwright makes this easy)
    LINK_BY_TEXT = lambda text: f"text={text}"

    # Base URL for the entire application (the base for all tests)
    BASE_URL = "https://the-internet.herokuapp.com/"
