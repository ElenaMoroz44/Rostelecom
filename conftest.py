import pytest
from playwright.sync_api import sync_playwright
from pages.registration_page import RegistrationPage

@pytest.fixture
def registration_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        reg_page = RegistrationPage(page)
        yield reg_page
        browser.close()
