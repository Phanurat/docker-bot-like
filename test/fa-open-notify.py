from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL ของหน้า Facebook ที่ต้องการเข้าถึง
url = 'https://www.facebook.com/'

# เปิดหน้าเว็บ
driver.get(url)

# รายการคุกกี้ที่คุณให้มา
cookies_list = [
    {
        'name': 'c_user',
        'value': '61551780956965',
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
        'value': '33%3A6G4mSdVIL5wfOQ%3A2%3A1719565792%3A-1%3A-1%3A%3AAcVO1U7ZF1isKyX9_pqiEcC8h5pdZWG6GUDzHmuOXQ',
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
        'value': '9DV9ZozopZitRFfYOfDeZhrr',
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
        'value': '1c2kDQYAvYB0GJ58k.AWVV2qJZtlsr4c3SP8aggBOB-jc.BmfoVp..AAA.0.0.BmfoVp.AWXgufNOvaQ',
        'domain': '.facebook.com',
        'path': '/',
        'expires': datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
        'httpOnly': True,
        'secure': True,
        'session': False,
        'sameSite': 'None'
    }
]

# เพิ่มคุกกี้ในเบราว์เซอร์
for cookie in cookies_list:
    # Convert expires to int if it is not None
    if cookie['expires']:
        cookie['expires'] = int(cookie['expires'])
    driver.add_cookie(cookie)

# รีเฟรชหน้าเว็บเพื่อใช้คุกกี้
driver.refresh()

# รอเวลาให้หน้าเว็บโหลดเสร็จ
time.sleep(5)

# ตรวจสอบสถานะการเข้าสู่ระบบ
# ตรวจสอบสถานะการเข้าสู่ระบบ
if "Facebook" in driver.title:
    print("เข้าสู่ระบบสำเร็จ")
    #Read notification
    post_url = 'https://www.facebook.com/notifications'
    driver.get(post_url)
    time.sleep(5)
    post_url = 'https://www.facebook.com/'
    driver.get(post_url)
    time.sleep(5)
    
else:
    print("การเข้าสู่ระบบล้มเหลว")

# ปิดเบราว์เซอร์
driver.quit()
