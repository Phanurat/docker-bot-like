from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import requests

target_b_id = 'b00009'

def break_automate():
    time_random = random.randint(30, 60)
    print(f"Break time: {time_random} seconds")
    time.sleep(time_random)
    main()

def get_driver():
    # Options for ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def timeline_scroll(driver):
    scroll_random = random.uniform(4, 6)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(15)

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
    time.sleep(5)  # Give the page some time to load

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
    if not check_login(driver):
        print("Failed to log in. Exiting.")
        driver.quit()
        return

    try:
        while True:
            start_time = time.time()
            two_hour_time = 72  # 2 hours in seconds
            three_hour_time = 120  # 3.5 hours in seconds
            work_time = random.randint(two_hour_time, three_hour_time)
            print(f"Automation time: {work_time} seconds")

            while time.time() - start_time < work_time:
                timeline_scroll(driver)
                time.sleep(3)

            driver.quit()
            break_automate()
            time.sleep(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
