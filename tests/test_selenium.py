from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.selenium
def test_selenium():
    driver  = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    #assert driver.title == "OrangeHRM"
    driver.implicitly_wait(5)
    #driver.find_element(By.NAME, "username").send_keys("Admin")
    #driver.find_element(By.NAME, "password").send_keys("admin123")
    #driver.find_element(By.TAG_NAME, 'button').click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
    act_title = driver.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Login Test Passed")
    else:
        print("Login test failed")
    driver.quit()