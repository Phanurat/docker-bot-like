from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def login_to_google(email, password):
    driver = get_driver()
    driver.get('https://accounts.google.com/signin')
    wait = WebDriverWait(driver, 20)

        # Enter email
    email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

        # Wait for the password field to appear
    wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
    password_field = driver.find_element(By.NAME, 'Passwd')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for the login process to complete
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Google Account")]')))
    print("Login successful")

     # Refresh page and open Colab
    driver.refresh()
    driver.get("https://colab.research.google.com/drive/1RMATUumSYdvqzE_tzlgEM_x6gE76U9Od?usp=sharing")

        # Wait for the page to load
    time.sleep(30)

        # Example of interacting with an element (if applicable)
        # button = driver.find_element(By.XPATH, '//button[text()="Run"]')  # Update selector as needed
        # button.click()
        # button.send_keys(Keys.CONTROL + Keys.RETURN)        
    time.sleep(250)  # Wait for the process to complete (adjust as needed)

if __name__ == "__main__":
    email = "6330102@kcs.ac.th"
    password = "1102300079370"

    if email and password:
        login_to_google(email, password)
    else:
        print("Please set the email and password")
