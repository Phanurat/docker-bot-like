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

# กำหนดเขตเวลา
tz = pytz.timezone('Asia/Bangkok')

# เวลาปัจจุบันในเขตเวลาที่กำหนด
now = datetime.now(tz)

# กำหนดเวลา main break และ end main break
main_break_start = now.replace(hour=21, minute=31, second=0, microsecond=0)
main_break_end = now.replace(hour=7, minute=0, second=0, microsecond=0)

# run and break intervals for the next day
first_run_start = now.replace(hour=7, minute=1, second=0, microsecond=0)
first_run_end = now.replace(hour=8, minute=30, second=0, microsecond=0)

first_break_start = now.replace(hour=8, minute=31, second=0, microsecond=0)
first_break_end = now.replace(hour=9, minute=0, second=0, microsecond=0)

run_two_start = now.replace(hour=9, minute=1, second=0, microsecond=0)
run_two_end = now.replace(hour=10, minute=30, second=0, microsecond=0)

break_two_start = now.replace(hour=10, minute=31, second=0, microsecond=0)
break_two_end = now.replace(hour=11, minute=0, second=0, microsecond=0)

three_run_start = now.replace(hour=11, minute=1, second=0, microsecond=0)
three_run_end = now.replace(hour=12, minute=59, second=0, microsecond=0)

break_three_start = now.replace(hour=13, minute=0, second=0, microsecond=0)
break_three_end = now.replace(hour=14, minute=0, second=0, microsecond=0)

four_run_start = now.replace(hour=14, minute=1, second=0, microsecond=0)
four_run_end = now.replace(hour=15, minute=30, second=0, microsecond=0)

break_four_start = now.replace(hour=15, minute=31, second=0, microsecond=0)
break_four_end = now.replace(hour=16, minute=0, second=0, microsecond=0)

five_run_start = now.replace(hour=16, minute=1, second=0, microsecond=0)
five_run_end = now.replace(hour=17, minute=30, second=0, microsecond=0)

break_five_start = now.replace(hour=17, minute=31, second=0, microsecond=0)
break_five_end = now.replace(hour=18, minute=0, second=0, microsecond=0)

six_run_start = now.replace(hour=18, minute=1, second=0, microsecond=0)
six_run_end = now.replace(hour=19, minute=30, second=0, microsecond=0)

break_six_start = now.replace(hour=19, minute=31, second=0, microsecond=0)
break_six_end = now.replace(hour=20, minute=0, second=0, microsecond=0)

seven_run_start = now.replace(hour=20, minute=1, second=0, microsecond=0)
seven_run_end = now.replace(hour=21, minute=30, second=0, microsecond=0)

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
    
    # Wait until the page is loaded
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Send ENTER key
        # actions.send_keys(Keys.ENTER).perform()
        
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(15)

        actions.send_keys(Keys.ENTER).perform()
        
        print("Entered keys: ENTER")
        time.sleep(15)

        wait = WebDriverWait(driver, 20)
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
        password_field = driver.find_element(By.NAME, 'Passwd')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Login successful")
        time.sleep(25)
        # Send ENTER key
        actions.send_keys(Keys.ENTER).perform()
        
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(10)

        actions.send_keys(Keys.TAB).perform()
        time.sleep(10)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(10)
        # Send ENTER key
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        # Send CONTROL key
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
        print("Entered keys: ENTER + CONTROL")
        time.sleep(30)
        driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    email = "6330102@kcs.ac.th"
    password = "1102300079370"
    while True:
        now = datetime.now(tz)
        # ตรวจสอบว่าปัจจุบันอยู่ในช่วง main break หรือไม่
        if main_break_start == now or now < main_break_end:
            print("main break")
            print(f"{now.hour}:{now.minute}")

        elif first_run_start <= now < first_run_end:
            print("Running 1")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif first_break_start <= now < first_break_end:
            print("Mini Break 1")
            print(f"{now.hour}:{now.minute}")
        
        elif run_two_start <= now < run_two_end:
            print("Running 2")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif break_two_start <= now < break_two_end:
            print("Mini Break 2")
            print(f"{now.hour}:{now.minute}")
        
        elif three_run_start <= now < three_run_end:
            print("Running 3")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif break_three_start <= now < break_three_end:
            print("Mini Break 3")
            print(f"{now.hour}:{now.minute}")
        
        elif four_run_start <= now < four_run_end:
            print("Running 4")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif break_four_start <= now < break_four_end:
            print("Mini Break 4")
            print(f"{now.hour}:{now.minute}")
        
        elif five_run_start <= now < five_run_end:
            print("Running 5")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif break_five_start <= now < break_five_end:
            print("Mini Break 5")
            print(f"{now.hour}:{now.minute}")
        
        elif six_run_start <= now < six_run_end:
            print("Running 6")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        
        elif break_six_start <= now < break_six_end:
            print("Mini Break 6")
            print(f"{now.hour}:{now.minute}")
        
        elif seven_run_start <= now < seven_run_end:
            print("Running 7")
            print(f"{now.hour}:{now.minute}")
            login_to_google(email, password)
            time.sleep(5400)
        #time.sleep(600)  # หยุดโปรแกรมเป็นเวลา 10 วินาทีเพื่อประหยัดพลังงาน
        
