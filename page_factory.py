from playwright.sync_api import Browser, BrowserContext, Page


class PageFactory:
    def __init__(self, browser: Browser):
        self.browser = browser

    def create_context(
            self,
            login: str,
            password: str,
    ) -> BrowserContext:
        return self.browser.new_context(
            http_credentials={
                'username': login,
                'password': password
            }
        )
    def create_page(self, context: BrowserContext) -> Page:
        return context.new_page()