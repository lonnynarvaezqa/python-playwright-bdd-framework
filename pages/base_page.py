# pages/base_page.py

class BasePage:
    def __init__(self, page):
        # 'page' es la instancia de playwright.sync_api.Page
        self.page = page