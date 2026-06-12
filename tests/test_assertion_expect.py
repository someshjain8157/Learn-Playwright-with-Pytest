from playwright.sync_api import expect


def test_assertion_expect(page):
    page.goto("https://bootswatch.com/default")

    # -------------------------------------------------
    # 1. Page Assertions
    # -------------------------------------------------

    expect(page).to_have_title("Bootswatch: Default")

    # -------------------------------------------------
    # 2. Element Visibility
    # -------------------------------------------------

    navbar = page.locator("nav.navbar").first
    expect(navbar).to_be_visible()

    # -------------------------------------------------
    # 3. Element Text
    # -------------------------------------------------

    heading = page.locator("h1").first
    expect(heading).to_have_text("Default")

    # Partial text
    expect(heading).to_contain_text("Default")

    # -------------------------------------------------
    # 4. Element Attribute
    # -------------------------------------------------

    github_link = page.get_by_role("link", name="GitHub").first
    expect(github_link).to_have_attribute(
        "href",
        "https://github.com/thomaspark/bootswatch"
    )

    # -------------------------------------------------
    # 5. Input Field
    # -------------------------------------------------

    text_input = page.locator("#floatingInput")

    expect(text_input).to_be_visible()
    expect(text_input).to_be_enabled()

    text_input.fill("somesh@test.com")

    expect(text_input).to_have_value("somesh@test.com")

    # -------------------------------------------------
    # 6. Placeholder
    # -------------------------------------------------

    expect(text_input).to_have_attribute(
        "placeholder",
        "name@example.com"
    )

    # -------------------------------------------------
    # 7. Checkbox
    # -------------------------------------------------

    checkbox = page.locator("input[type='checkbox']").nth(1)
    checkbox_label = page.locator("label[for='btncheck2']")

    expect(checkbox).not_to_be_checked()

    checkbox_label.click()

    expect(checkbox).to_be_checked()

    checkbox_label.click()

    expect(checkbox).not_to_be_checked()

    # -------------------------------------------------
    # 8. Radio Button
    # -------------------------------------------------

    radio = page.locator("input[type='radio']").first
    radio_label = page.locator("label[for='btnradio1']")

    radio_label.click()

    expect(radio).to_be_checked()

    # -------------------------------------------------
    # 9. Button State
    # -------------------------------------------------

    button = page.get_by_role("button", name="Primary").first

    expect(button).to_be_visible()
    expect(button).to_be_enabled()

    # -------------------------------------------------
    # 12. CSS Class
    # -------------------------------------------------

    expect(button).to_have_class("btn btn-primary")

    # -------------------------------------------------
    # 13. URL Assertion
    # -------------------------------------------------

    expect(page).to_have_url("https://bootswatch.com/default/")

    # -------------------------------------------------
    # 14. Text Exists Anywhere
    # -------------------------------------------------

    expect(page.locator("body")).to_contain_text("Typography")

    # -------------------------------------------------
    # 15. Hidden Element
    # -------------------------------------------------

    hidden_element = page.locator(".non-existing-element")

    expect(hidden_element).to_have_count(0)

    # -------------------------------------------------
    # 16. Dropdown Example
    # -------------------------------------------------

    dropdown = page.locator("select").first

    dropdown.select_option(index=1)

    expect(dropdown).to_have_value("2")

    # -------------------------------------------------
    # 17. Editable State
    # -------------------------------------------------

    expect(text_input).to_be_editable()

    # -------------------------------------------------
    # 18. Focus Assertion
    # -------------------------------------------------

    text_input.click()

    expect(text_input).to_be_focused()

    print("All assertions passed.")