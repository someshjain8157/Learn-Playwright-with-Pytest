from pages.ABTestPage import ABTestPage

def test_ab_testing(page: ABTestPage):
    # Open the A/B Testing page through the page object
    ab_test_page = ABTestPage.open(page)

    # Get the heading text
    heading = ab_test_page.get_header_text()

    # Print the heading
    print(f"Heading: {heading}")

    # Verify the heading is one of the expected A/B variants
    assert heading in ["A/B Test Control", "A/B Test Variation 1"]
