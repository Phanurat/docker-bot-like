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
            'value': '27%3AO7lf2Br_zLQqDg%3A2%3A1719806925%3A-1%3A-1',
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
            'value': 'IGaBZofFdrTky3WbsH7c9oSG',
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
            'value': '0fAyHsfOcLQLhRWWF.AWWOpJ7tqCdu3z1cGNe2bqGMT-w.BmgWYg..AAA.0.0.BmgivP.AWUyO8hDlT0',
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
    #

    # ค้นหาโพสต์ที่ต้องการไลค์ (ในที่นี้จะใช้กดไลค์โพสต์ตัวแรกที่ปรากฏ)
    try:
        like_button = driver.find_element(By.XPATH, "//div[@aria-label='Like']")
        like_button.click()
        print("เข้าสู่ระบบสำเร็จ")
        print("กดไลค์โพสต์สำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการกดไลค์โพสต์: {str(e)}")

else:
    print("การเข้าสู่ระบบล้มเหลว")

# ปิดเบราว์เซอร์
driver.quit()
