from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome()

class Test_Enterance:
    def test_enterance(self):
        driver.get("http://www.saucedemo.com")
        driver.maximize_window()    
            
        

class Test_SauceDemo:
     def test_blank_areas(self):
        testClassEnterance =Test_Enterance()
        testClassEnterance.test_enterance()
    
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        
     def test_blank_password(self):
        testClassEnterance =Test_Enterance()
        testClassEnterance.test_enterance()
    
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        
     def test_invalid_login(self):
        testClassEnterance =Test_Enterance()
        testClassEnterance.test_enterance()
       
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        
     def test_successful_login(self):
        testClassEnterance =Test_Enterance()
        testClassEnterance.test_enterance()
        
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(3)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        get_url= driver.current_url
        if get_url == "https://www.saucedemo.com/inventory.html":
            print("KULLANICI GİRİŞİ BAŞARILI")
        else:
            print("KULLANICI SAYFAYA YÖNLENDİRİLEMEDİ")
        listOfCourses = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
        testResult = len(listOfCourses) == 6
        print (f"TEST SONUCU: {testResult}")
            
            
    
    
    
testClass = Test_SauceDemo()
testClass.test_blank_areas()
testClass.test_blank_password()
testClass.test_invalid_login()
testClass.test_successful_login()
