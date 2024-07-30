import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/index.htm")

# TC001; Register a user
driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.NAME, "customer.firstName").send_keys("Ayobami")
driver.find_element(By.NAME, "customer.lastName").send_keys("Adeniji")
driver.find_element(By.NAME, "customer.address.street").send_keys("poland")
driver.find_element(By.NAME, "customer.address.city").send_keys("poland")
driver.find_element(By.NAME, "customer.address.state").send_keys("poland")
driver.find_element(By.NAME, "customer.address.zipCode").send_keys("0123")
driver.find_element(By.NAME, "customer.phoneNumber").send_keys("12345678")
driver.find_element(By.NAME, "customer.ssn").send_keys("0800000000")
driver.find_element(By.NAME, "customer.username").send_keys("standard2")
driver.find_element(By.NAME, "customer.password").send_keys("secret")
driver.find_element(By.NAME, "repeatedPassword").send_keys("secret")
driver.find_element(By.CLASS_NAME, "button").click()
time.sleep(5)

# TC002; Signing in with a user
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.find_element(By.NAME, "username").send_keys("samm")
driver.find_element(By.NAME, "password").send_keys("secret")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Log In']"))
    )
finally:
    driver.find_element(By.XPATH, "//input[@value='Log In']").click()

# TC003; Applying for a Loan

driver.find_element(By.XPATH, "//a[normalize-space()='Request Loan']").click()
driver.find_element(By.ID, "amount").send_keys("10000")
driver.find_element(By.ID, "downPayment").send_keys("3000")
driver.find_element(By.XPATH, "//input[@value='Apply Now']").click()
#driver.find_element(By.NAME, "").send_keys("")






time.sleep(5)






driver.close()
