from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

def get_driver():
    # Options for ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    # Set language to English
    chrome_options.add_argument("--lang=en")

    # Initialize WebDriver using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def login_to_google(email, password):
    driver = get_driver()
    try:
        driver.get('https://accounts.google.com/signin')

        # Wait for the email input field to be present
        wait = WebDriverWait(driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        # Wait for the password input field to be present
        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
        password_field.send_keys(password)

        # Wait for the "Next" button to be clickable and click it
        next_button = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
        next_button.click()

        # Wait for the login process to complete
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="profileIdentifier"]')))
        print("Login successful")
        time.sleep(120)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    # Retrieve credentials from environment variables
    #email = os.getenv('GOOGLE_EMAIL')
    #password = os.getenv('GOOGLE_PASSWORD')
    email = "nara0220024@hotmail.com"
    password = "Pass0220024"

    if email and password:
        login_to_google(email, password)
    else:
        print("Please set the GOOGLE_EMAIL and GOOGLE_PASSWORD environment variables")
