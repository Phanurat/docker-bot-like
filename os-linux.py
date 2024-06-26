from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import time

# Path to your GeckoDriver (Linux server)
gecko_driver_path = '/path/geckodriver'

# Options for Firefox
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode
firefox_options.add_argument("--start-maximized")

# Initialize WebDriver
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# URL ของหน้า Facebook ที่ต้องการเข้าถึง
url = 'https://www.facebook.com/'

# เปิดหน้าเว็บ
driver.get(url)

# รายการคุกกี้ที่คุณให้มา
cookies_list = [
    {
        'name': 'c_user',
        'value': '100020688590532',
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
        'value': '11%3AinhoChAjm4XLPA%3A2%3A1719392933%3A-1%3A11361',
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
        'value': 'eOlPZjhhJxb4hoWIuz9f0v-b',
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
        'value': '1YmSZxru2wyb7mCNZ.AWUGodKebFijrAu25EovUc_QsZE.BmesVy..AAA.0.0.Bme9qs.AWVHmaoP3P0',
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
if "Facebook" in driver.title:
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("การเข้าสู่ระบบล้มเหลว")

# ปิดเบราว์เซอร์
driver.quit()
