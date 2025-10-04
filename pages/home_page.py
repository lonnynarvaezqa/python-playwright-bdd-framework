from pages.base_page import BasePage
from pages.elements.home_page_elements import HomePageElements
from pages.elements.generic_page_elements import GenericPageElements

class HomePage(BasePage):

    def navigate(self):
        """Navigates to the base URL."""
        self.page.goto(HomePageElements.BASE_URL)

    def click_link_by_text(self, link_text):
        """Clicks a link based on its visible text."""
        # Playwright natively locates elements by visible text
        self.page.click(HomePageElements.LINK_BY_TEXT(link_text))

    def get_page_header(self):
        """Gets the text of the page's main header."""
        return self.page.inner_text(GenericPageElements.PAGE_HEADER)
