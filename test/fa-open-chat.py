import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# กำหนด b_id ที่ต้องการค้นหา        
target_b_id = 'b00003'
url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'

# ส่ง GET request เพื่อดึงข้อมูล
response = requests.get(url)
# ตรวจสอบสถานะของ response
if response.status_code == 200:
    data = response.json()
    try:
        selected_data = []

        # วนลูปเพื่อค้นหาข้อมูลที่มี b_id เท่ากับ target_b_id
        for item in data['data']:
            if item['b_id'] == target_b_id:
                selected_data.append({
                    'b_id': item['b_id'],
                    'c_user': item['c_user'],
                    'xs': item['xs'],
                    'datr': item['datr'],
                    'fr': item['fr']
                })

        # ตรวจสอบว่า selected_data มีข้อมูล
        if not selected_data:
            print(f"No data found for b_id = {target_b_id}")
            exit()

        # ดึงข้อมูลคุกกี้จาก selected_data
        item = selected_data[0]
        c_user = item['c_user']
        xs = item['xs']
        datr = item['datr']
        fr = item['fr']

    except KeyError as e:
        print(f'เกิดข้อผิดพลาดในการดึงข้อมูล: {e}')
        exit()

else:
    print('เกิดข้อผิดพลาดในการเรียกใช้ API:', response.status_code)
    exit()

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the Facebook profile page you want to access
url = 'https://www.facebook.com'

# Open the web page
driver.get(url)

# List of cookies you provided
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

# ตรวจสอบให้แน่ใจว่าค่าของคุกกี้ไม่เป็น None ก่อนที่จะเพิ่มเข้าในเบราว์เซอร์
for cookie in cookies_list:
    if not cookie['value']:
        print(f"Cookie {cookie['name']} has an empty value. Skipping this cookie.")
        continue
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
    print("Login successful")
    # URL of the Facebook profile page you want to access
    url = 'https://www.facebook.com/messages/e2ee/t/'

    # Open the web page
    driver.get(url)
    time.sleep(25)
else:
    print("Login failed")

# Close the browser
driver.quit()
