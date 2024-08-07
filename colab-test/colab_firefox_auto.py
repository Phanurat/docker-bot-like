from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
import time
import random
import requests
import threading
import pytz

global target_b_id
target_b_id = 'b00009'

def get_driver():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Firefox(options=firefox_options)

    return driver

def link_comment():
    driver = get_driver()
    selected_link = "https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid0ADLEGEyKoe3PrcaFUzmRJu2U6hxuvfN28ZH51XFPhDcsbRT8RiLhm9rv4wgH3p7sl"
    driver.get(selected_link)

    time.sleep(5)

    try:
        xpaths = [
            '//div[@aria-label="Write a comment"]',
            '//div[@aria-label="Write a comment..."]',
            '//div[contains(@aria-label, "Write a comment")]',
            '//div[@role="textbox"]',
        ]
        comment_input = None
        
        for xpath in xpaths:
            try:
                comment_input = driver.find_element(By.XPATH, xpath)
                if comment_input:
                    break
            except:
                continue
        
        if not comment_input:
            raise Exception("No Comment")

        comment_input.click()
        time.sleep(2)
        
        # Random comment list
        #comment_text = random.choice(selected_comment)
        tz = pytz.timezone('Asia/Bangkok')

        # เวลาปัจจุบันในเขตเวลาที่กำหนด
        now = datetime.now(tz)
        text = "Hello Time at: " + str(now.hour) + ":" + str(now.minute)
        comment_text = text
        time.sleep(5)

        for char in comment_text:
            comment_input.send_keys(char)
            time.sleep(0.5)
        comment_input.send_keys(Keys.ENTER)

        print(f"Add comment '{comment_text}' Done!")

    except Exception as e:
        print(f"Can't Comment: {str(e)}")
        return
    
    print("Comment it Work!")
    # Add your comment functionality here


def timeline_scroll(driver):
    scroll_random = random.uniform(40, 200)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(15)

def main():
    driver = get_driver()
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
        print("เข้าสู่ระบบสำเร็จ")
        while True:
            while True:
                timeline_scroll()
                #random_time  = random.randint(300, 600)
                time.sleep(5)
                link_comment()
                time.sleep(5)
                url = 'https://www.facebook.com/'
                driver.get(url)
    else:
        print("การเข้าสู่ระบบล้มเหลว")
    
if __name__ == "__main__":
    main()