def test_name_too_short_ui(registration_page):
    registration_page.open()
    registration_page.fill_first_name("А")

    error = registration_page.get_first_name_error()
    assert error is not None
    assert "минимум" in error


def test_name_min_length_ui(registration_page):
    registration_page.open()
    registration_page.fill_first_name("Ан")

    assert registration_page.get_first_name_error() is None


def test_name_with_dash_ui(registration_page):
    registration_page.open()
    registration_page.fill_first_name("Ан-на")

    assert registration_page.get_first_name_error() is None


def test_name_latin_ui(registration_page):
    registration_page.open()
    registration_page.fill_first_name("Ivan")

    error = registration_page.get_first_name_error()
    assert error is not None


def test_name_empty_ui(registration_page):
    registration_page.open()
    registration_page.fill_first_name("")

    error = registration_page.get_first_name_error()
    assert error is not None
