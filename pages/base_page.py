class BasePage:
    def __init__(self, page):
        # 'page' is the playwright.sync_api.Page instance
        self.page = page
