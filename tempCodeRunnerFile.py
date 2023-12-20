from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SauceDemo:
    def test_blank_areas(self):
        driver = webdriver.Chrome()
        driver.get("http://www.saucedemo.com")
        driver.maximize_window() 
    
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required "
        print(f"TEST SONUCU: {testResult}")
        
testClass = Test_SauceDemo()
testClass.test_blank_areas()