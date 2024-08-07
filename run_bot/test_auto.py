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
import pytz

# b_id bot
global target_b_id
target_b_id = 'b00012'


def link_comment():
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

def timeline_scroll():
    scroll_random = random.uniform(60, 120)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)

def break_time(check_days):
    driver.quit()
    start_time = 20
    end_time = 50
    break_duration = random.randint(start_time, end_time)

    print(f"Time break is {break_duration}")
    print("-" * 10)
    driver.quit()
    time.sleep(break_duration)

    while True:
        today = datetime.now()
        day_of_week = today.weekday()
        days = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
        #test_days ="อังคาร"
        
        if check_days == days[day_of_week]:
            print("Breaking!!")
            driver.quit()
            time.sleep(1)
        
        else:
            print("Start New Day, will be working!!")
            driver.quit()
            main()
    
def main():
    # Options for ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver using WebDriverManager
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    url = 'https://www.facebook.com/'
    driver.get(url)

    print("Start Bot Runing!!!")
    
    bot_url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'
    response = requests.get(bot_url)
    if response.status_code == 200:
        data = response.json()
        try:
            selected_data = []
            
            for item in data['data']:
                if item['b_id'] == target_b_id:
                    selected_data.append({
                        'b_id': item['b_id'],
                        'c_user': item['c_user'],
                        'xs': item['xs'],
                        'datr': item['datr'],
                        'fr': item['fr']
                    })
            if not selected_data:
                print(f"No data found for b_id = {target_b_id}")
                exit()
            item = selected_data[0]
            c_user = item['c_user']
            xs = item['xs']
            datr = item['datr']
            fr = item['fr']

        except KeyError as e:
            exit()
    else:
        print("Error call back API:", response.status_code)
        exit()

    cookies_list = [
        {
            'name': 'c_user',
            'value': str(c_user),
            'domain': '.facebook.com',
            'path': '/',
            'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
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
            'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
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
            'expires': datetime.strptime('2025-06-28T01:12:26.667Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
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
            'expires': datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        }
    ]

    # Add cookies to the browser
    for cookie in cookies_list:
        # Convert expires to int if it is not None
        if cookie['expires']:
            cookie['expires'] = int(cookie['expires'])
        driver.add_cookie(cookie)

    # Refresh the web page to use cookies
    driver.refresh()

    # Wait for the web page to load completely
    time.sleep(5)

    # Check login status
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

    # ปิดเบราว์เซอร์
    driver.quit()

if __name__ == "__main__":
    main()
