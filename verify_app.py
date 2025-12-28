from playwright.sync_api import sync_playwright, expect
import time

def verify_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the local server
        page.goto("http://localhost:8080")

        # Wait for the grid to be populated
        grid = page.locator("#product-grid")
        expect(grid).to_be_visible()

        # Check if cards are rendered
        cards = page.locator(".card")
        count = cards.count()
        print(f"Found {count} product cards.")

        if count == 0:
            print("Error: No product cards found!")
            browser.close()
            return

        # Take a screenshot of the grid
        page.screenshot(path="verification_grid.png")

        # Click on the first card to open modal
        first_card = cards.first
        first_card.click()

        # Wait for modal to be active
        modal = page.locator("#product-modal")
        expect(modal).to_have_class(re.compile(r"active"))

        # Take a screenshot of the modal
        page.screenshot(path="verification_modal.png")

        # Close the modal
        close_btn = page.locator(".close-btn")
        close_btn.click()

        # Wait for modal to close
        expect(modal).not_to_have_class(re.compile(r"active"))

        print("Verification successful!")
        browser.close()

if __name__ == "__main__":
    import re
    verify_app()
