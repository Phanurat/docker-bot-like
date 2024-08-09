from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta
import pytz
import time
import os

# Define time intervals
def get_intervals():
    now = datetime.now(tz)
    intervals = {
        'main_break': (now.replace(hour=21, minute=31, second=0, microsecond=0),
                       now.replace(hour=7, minute=0, second=0, microsecond=0)),
        'runs': [
            (now.replace(hour=7, minute=1, second=0, microsecond=0), now.replace(hour=8, minute=30, second=0, microsecond=0)),
            (now.replace(hour=9, minute=1, second=0, microsecond=0), now.replace(hour=10, minute=30, second=0, microsecond=0)),
            (now.replace(hour=11, minute=1, second=0, microsecond=0), now.replace(hour=12, minute=59, second=0, microsecond=0)),
            (now.replace(hour=14, minute=1, second=0, microsecond=0), now.replace(hour=15, minute=30, second=0, microsecond=0)),
            (now.replace(hour=16, minute=1, second=0, microsecond=0), now.replace(hour=17, minute=30, second=0, microsecond=0)),
            (now.replace(hour=18, minute=1, second=0, microsecond=0), now.replace(hour=19, minute=30, second=0, microsecond=0)),
            (now.replace(hour=20, minute=1, second=0, microsecond=0), now.replace(hour=21, minute=30, second=0, microsecond=0))
        ],
        'breaks': [
            (now.replace(hour=8, minute=31, second=0, microsecond=0), now.replace(hour=9, minute=0, second=0, microsecond=0)),
            (now.replace(hour=10, minute=31, second=0, microsecond=0), now.replace(hour=11, minute=0, second=0, microsecond=0)),
            (now.replace(hour=13, minute=0, second=0, microsecond=0), now.replace(hour=14, minute=0, second=0, microsecond=0)),
            (now.replace(hour=15, minute=31, second=0, microsecond=0), now.replace(hour=16, minute=0, second=0, microsecond=0)),
            (now.replace(hour=17, minute=31, second=0, microsecond=0), now.replace(hour=18, minute=0, second=0, microsecond=0)),
            (now.replace(hour=19, minute=31, second=0, microsecond=0), now.replace(hour=20, minute=0, second=0, microsecond=0))
        ]
    }
    return intervals

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
    driver.get('https://colab.research.google.com/drive/1RsiY9ojDK7ccb5E440fil4RaTz5y1z65?usp=sharing')
    time.sleep(15)
    
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        time.sleep(15)

        actions.send_keys(Keys.ENTER).perform()
        time.sleep(15)

        wait = WebDriverWait(driver, 20)
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
        password_field = driver.find_element(By.NAME, 'Passwd')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(25)

        actions.send_keys(Keys.ENTER).perform()
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        time.sleep(10)

        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.ENTER).perform()
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        time.sleep(30)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    email = os.getenv('GOOGLE_EMAIL', '6330102@kcs.ac.th')
    password = os.getenv('GOOGLE_PASSWORD', '1102300079370')

    tz = pytz.timezone('Asia/Bangkok')

    while True:
        now = datetime.now(tz)
        intervals = get_intervals()

        if intervals['main_break'][0] <= now or now < intervals['main_break'][1]:
            print("Main Break")
        else:
            for run, brk in zip(intervals['runs'], intervals['breaks']):
                if run[0] <= now < run[1]:
                    print(f"Running: {run[0].strftime('%H:%M')} - {run[1].strftime('%H:%M')}")
                    login_to_google(email, password)
                    time.sleep(5400)
                elif brk[0] <= now < brk[1]:
                    print(f"Break: {brk[0].strftime('%H:%M')} - {brk[1].strftime('%H:%M')}")

        time.sleep(60)  # Check every minute
