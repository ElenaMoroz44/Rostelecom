def test_password_too_short_ui(registration_page):
    registration_page.open()
    registration_page.fill_password("Abc12")

    error = registration_page.get_password_error()
    assert error is not None
    assert "не менее 8" in error


def test_password_without_uppercase_ui(registration_page):
    registration_page.open()
    registration_page.fill_password("abcdef12")

    error = registration_page.get_password_error()
    assert error is not None
    assert "заглавн" in error


def test_password_with_cyrillic_ui(registration_page):
    registration_page.open()
    registration_page.fill_password("Abcде123")

    error = registration_page.get_password_error()
    assert error is not None
    assert "латин" in error


def test_passwords_not_matching_ui(registration_page):
    registration_page.open()
    registration_page.fill_password("Abcdef12")
    registration_page.fill_password_confirm("Abcdef13")

    error = registration_page.get_password_confirm_error()
    assert error is not None
    assert "не совпадают" in error


def test_valid_password_ui(registration_page):
    registration_page.open()
    registration_page.fill_password("Abcdef12")
    registration_page.fill_password_confirm("Abcdef12")

    assert registration_page.get_password_error() is None
    assert registration_page.get_password_confirm_error() is None
