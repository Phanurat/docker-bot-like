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

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#Input ID bot from API google sheet
target_b_id = 'b00009'

#scroll post facebook
def timeline_scroll():
    scroll_random = random.uniform(4, 6)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(15)

#Sleep Break Bot automation
def break_time():
    start_time = 252 # 7hours = 25200sec
    end_time = 306 # 8 half hours = 30600sec
    break_duration = random.randint(start_time, end_time)
    print(f"Time break is {break_duration} sec")
    print("--------------------------------")
    driver.quit()
    time.sleep(break_duration)

#main controll
def main(target_b_id):
    print("Start Bot Runing!!!")
    url = 'https://www.facebook.com/'
    driver.get(url)

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

    for cookie in cookies_list:
        if cookie['expires']:
            cookie['expires'] = int(cookie['expires'])
        driver.add_cookie(cookie)
    
    driver.refresh()
    url = 'https://www.facebook.com/'
    driver.get(url)
    
    title = driver.title
    

    time.sleep(5)

    if title == "Facebook":
        if "Facebook" in driver.title:
            print("เข้าสู่ระบบสำเร็จ")
            while True:
                #timeline_scroll()
                #time.sleep(3)
                #event_random()
                #time.sleep(5)
                print("Loop run bot automation!")
                start_time = time.time()
                two_hour_time = 72 #2hours = 7200sec
                hthere_hour_time = 126 #3.5 hours = 12600sec
                
                time_work = random.randint(two_hour_time, hthere_hour_time)
                print(f"Time to Work! {time_work} sec.")

                while time.time() - start_time < time_work:
                    timeline_scroll()
                    time.sleep(3)
                break_time()
        else:
            print("การเข้าสู่ระบบล้มเหลว")

        # ปิดเบราว์เซอร์
        driver.quit()
    driver.quit()

if __name__ == "__main__":
    main(target_b_id)