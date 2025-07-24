import os
from playwright.sync_api import sync_playwright

def run_tests():
    html_path = "file://" + os.getcwd() + "/calculator.html"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(html_path)

        # Test Add: 2 + 3 = 5
        page.fill("#num1", "2")
        page.fill("#num2", "3")
        page.click("text=Add")
        result = page.inner_text("#result")
        assert result == "Result: 5", f"Add failed: got {result}"

        # Test Subtract: 5 - 2 = 3
        page.fill("#num1", "5")
        page.fill("#num2", "2")
        page.click("text=Subtract")
        result = page.inner_text("#result")
        assert result == "Result: 3", f"Subtract failed: got {result}"

        # Test Multiply: 4 * 3 = 12
        page.fill("#num1", "4")
        page.fill("#num2", "3")
        page.click("text=Multiply")
        result = page.inner_text("#result")
        assert result == "Result: 12", f"Multiply failed: got {result}"

        # Test Divide: 10 / 2 = 5 or 5.0
        page.fill("#num1", "10")
        page.fill("#num2", "2")
        page.click("text=Divide")
        result = page.inner_text("#result")
        assert result in ["Result: 5", "Result: 5.0"], f"Divide failed: got {result}"

        print("All tests passed successfully!")
        browser.close()

if __name__ == "__main__":
    run_tests()
