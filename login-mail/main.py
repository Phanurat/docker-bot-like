from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.get('https://colab.research.google.com/drive/1RMATUumSYdvqzE_tzlgEM_x6gE76U9Od?usp=sharing')
    
    # Wait until the page is loaded
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Send ENTER key
        actions.send_keys(Keys.ENTER).perform()
        
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(5)

        actions.send_keys(Keys.ENTER).perform()
        
        print("Entered keys: ENTER")
        time.sleep(10)

        wait = WebDriverWait(driver, 20)
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
        password_field = driver.find_element(By.NAME, 'Passwd')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Login successful")
        time.sleep(20)
        # Send ENTER key
        actions.send_keys(Keys.ENTER).perform()
        
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(5)

        actions.send_keys(Keys.TAB).perform()
        time.sleep(5)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(5)
        # Send ENTER key
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(5)
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(20)

        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    email = "6330102@kcs.ac.th"
    password = "1102300079370"
    login_to_google(email, password)
