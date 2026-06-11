from playwright.sync_api import expect


def test_textbox_locators_form(page) -> None:
    page.goto("https://demoqa.com/")
    page.get_by_role("link", name="Elements").click()
    page.get_by_role("link", name="Text Box").click()
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Nishant")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("Nishant@gmail.com")
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").fill("Golden Palms, Ring Road, Bangalore Karnataka")
    # locator by id
    # page.locator("#permanentAddress").click()
    # locator by class name
    # page.locator(".form-control").click()
    # locator by label
    # page.get_by_label("Permanent Address").click()
    # tag and id
    # page.locator("textarea#permanentAddress").click()
    # tag and class
    # page.locator("textarea.form-control").click()
    # xpath
    # page.locator("//textarea[@id='permanentAddress']").click()

    page.locator("#permanentAddress").fill("Same as Current Address")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Name:Nishant")).to_be_visible()
    expect(page.get_by_text("Email:Nishant@gmail.com")).to_be_visible()
    expect(page.get_by_text("Current Address :Golden Palms")).to_be_visible()
    expect(page.get_by_text("Permananet Address :Same as")).to_be_visible()
    print(f"Name: {page.get_by_text('Name:Nishant').inner_text()}")
    print(f"Email: {page.get_by_text('Email:Nishant@gmail.com').inner_text()}")
    print(f"Current Address: {page.get_by_text('Current Address :Golden Palms').inner_text()}")
    print(f"Permanent Address: {page.get_by_text('Permananet Address :Same as').inner_text()}")
    print("Test Passed")
