import os
import time
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Headless Chrome options for Codespaces
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use a unique temporary user data directory
temp_dir = tempfile.mkdtemp()
chrome_options.add_argument(f"--user-data-dir={temp_dir}")

driver = webdriver.Chrome(options=chrome_options)

# Open the calculator HTML file
driver.get("file://" + os.getcwd() + "/calculator.html")
time.sleep(1)

# Test case: 2 + 3 = 5
driver.find_element(By.ID, "num1").send_keys("2")
driver.find_element(By.ID, "num2").send_keys("3")
driver.find_element(By.XPATH, "//button[text()='Add']").click()
time.sleep(1)

# Validate the result
result = driver.find_element(By.ID, "result").text
assert result == "Result: 5", f"Expected 'Result: 5' but got '{result}'"
print("Test Passed!")

driver.quit()
