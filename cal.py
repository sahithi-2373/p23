import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file://" + os.getcwd() + "/calculator.html")
time.sleep(1)

# Test case: 2 + 3 = 5
driver.find_element(By.ID, "num1").send_keys("2")
driver.find_element(By.ID, "num2").send_keys("3")
driver.find_element(By.XPATH, "//button[text()='Add']").click()
time.sleep(1)

result = driver.find_element(By.ID, "result").text
assert result == "Result: 5", f"Expected 'Result: 5' but got '{result}'"
print("Test Passed!")

driver.quit()
