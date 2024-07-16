import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random

target_b_id = 'b00007'

def break_automate():
    time_random = random.randint(5, 10)
    print("Break time:", time_random, "seconds")
    time.sleep(time_random)
    
def get_driver():
    # Options for ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def check_login(driver):
    url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            selected_data = [item for item in data['data'] if item['b_id'] == target_b_id]

            if not selected_data:
                print(f"No data found for b_id = {target_b_id}")
                return False

            item = selected_data[0]
            c_user = item['c_user']
            xs = item['xs']
            datr = item['datr']
            fr = item['fr']

        except KeyError as e:
            print(f'Error extracting data: {e}')
            return False

    else:
        print('Error calling API:', response.status_code)
        return False

    url = 'https://www.facebook.com'
    driver.get(url)

    cookies_list = [
        {
            'name': 'c_user',
            'value': str(c_user),
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': False,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'xs',
            'value': str(xs),
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'datr',
            'value': str(datr),
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-06-28T01:12:26.667Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'fr',
            'value': str(fr),
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        }
    ]

    for cookie in cookies_list:
        if cookie['value']:
            driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(5)

    if "Facebook" in driver.title:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False

def main():
    driver = get_driver()
    if check_login(driver):
        count = 1
        while True:
            work_time = random.randint(5, 10)
            print("Automation time:", work_time, "seconds")
            time.sleep(work_time)  # Wait for random time

            count += 1
            if count % 10 == 0:
                driver.quit()  # Quit the current driver
                break_automate()
                driver = get_driver()  # Restart the driver
                check_login(driver)
            time.sleep(1)

if __name__ == "__main__":
    main()
