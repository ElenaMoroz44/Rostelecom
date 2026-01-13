from playwright.sync_api import Page

class RegistrationPage:
    URL = "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration"

    def __init__(self, page: Page):
        self.page = page

        # Поля
        self.first_name = page.locator("#kc-firstname")
        self.password = page.locator("#password")
        self.password_confirm = page.locator("#password-confirm")

        # Ошибки
        self.first_name_error = page.locator("#input-error-firstname")
        self.password_error = page.locator("#input-error-password")
        self.password_confirm_error = page.locator("#input-error-password-confirm")

    def open(self):
        self.page.goto(self.URL)

    # ===== Имя =====
    def fill_first_name(self, value: str):
        self.first_name.fill(value)
        self.first_name.blur()

    def get_first_name_error(self):
        if self.first_name_error.is_visible():
            return self.first_name_error.text_content()
        return None

    # ===== Пароль =====
    def fill_password(self, value: str):
        self.password.fill(value)
        self.password.blur()

    def fill_password_confirm(self, value: str):
        self.password_confirm.fill(value)
        self.password_confirm.blur()

    def get_password_error(self):
        if self.password_error.is_visible():
            return self.password_error.text_content()
        return None

    def get_password_confirm_error(self):
        if self.password_confirm_error.is_visible():
            return self.password_confirm_error.text_content()
        return None
