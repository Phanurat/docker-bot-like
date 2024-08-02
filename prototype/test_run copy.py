from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import requests

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Input ID bot from API google sheet
target_b_id = 'b00009'

# Scroll post Facebook
def timeline_scroll(driver):
    scroll_random = random.uniform(4, 6)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(15)

# Sleep Break Bot automation
def break_time(driver):
    start_time = 100  # 1 hour 40 minutes = 6000 sec
    end_time = 200  # 3 hours 20 minutes = 12000 sec
    break_duration = random.randint(start_time, end_time)
    print(f"Time break is {break_duration} sec")
    print("--------------------------------")
    driver.quit()
    time.sleep(break_duration)

def check_login(driver):
    print("Start Bot Running!!!")
    url = 'https://www.facebook.com/'
    driver.get(url)

    # Print the title and URL
    print("Title:", driver.title)
    print("URL:", driver.current_url)

    bot_url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'
    try:
        response = requests.get(bot_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error calling API: {e}")
        return False

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
        print(f"Error extracting data: {e}")
        return False

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
            start_time = time.time()
            two_hour_time = 72  # 2 hours
            three_hour_time = 120  # 3.5 hours
            work_time = random.randint(two_hour_time, three_hour_time)
            print(f"Time to Work! {work_time} sec.")
            
            while time.time() - start_time < work_time:
                timeline_scroll(driver)
                time.sleep(3)

            break_time(driver)

            count += 1
            if count % 10 == 0:
                driver = get_driver()  # Restart the driver
                if not check_login(driver):
                    print("Login failed after restart.")
                    break
            time.sleep(1)

if __name__ == "__main__":
    main()
