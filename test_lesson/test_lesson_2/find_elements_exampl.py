from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/forgot_password")

form = driver.find_element(By.CSS_SELECTOR, "#forgot_password")
print(form.text)
