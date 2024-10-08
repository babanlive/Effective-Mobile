import time

from chrome_driver import driver
from selenium.webdriver.common.by import By


url = "https://www.saucedemo.com/"
login = "standard_user"
password = "secret_sauce"

try:
    driver.get(url)
    driver.find_element(By.ID, "user-name").send_keys(login)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)

    driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

    assert "Sauce Labs Bolt T-Shirt" in driver.page_source

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("TestName")
    driver.find_element(By.ID, "last-name").send_keys("TestLastName")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    assert "Thank you for your order" in driver.page_source
    time.sleep(3)

except Exception as e:
    print(f"Error: {e}")
