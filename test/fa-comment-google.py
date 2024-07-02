from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import requests
import random

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

def get_random_comment():
    #URL Google Apps Script
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]

        selected_comment = random.choice(comments)
        #print(selected_comment)
        return selected_comment
    
    else:
        print(f"Error Status code: {response.status_code}")
        return None
selected_comment = get_random_comment()


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
        'value': '28%3AvxWS-P6HoYsIsQ%3A2%3A1719890496%3A-1%3A-1',
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
        'value': 'L3KDZhBP2TiorgX_frlkQbvx',
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
        'value': '0TprfQir7mFxJRsv4.AWUzaEZ3Cj_mcixj-hKBc_gGinM.Bmg3I2..AAA.0.0.Bmg3I_.AWUID-x-DwU',
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
    
    # ไปที่โพสต์ที่ต้องการคอมเมนต์
    post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'
    driver.get(post_url)
    time.sleep(5)
    
    try:
        # ลองใช้ XPath ต่างๆ เพื่อหาช่องคอมเมนต์
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
            raise Exception("ไม่สามารถหาช่องคอมเมนต์ได้")
        
        comment_input.click()
        time.sleep(2)

        # พิมพ์คอมเมนต์
        comment_text = selected_comment
        comment_input.send_keys(comment_text)
        comment_input.send_keys(Keys.ENTER)
        print(f"เพิ่มคอมเมนต์ '{comment_text}' สำเร็จ")
    except Exception as e:
        print(f"ไม่สามารถเพิ่มคอมเมนต์ได้: {str(e)}")
else:
    print("การเข้าสู่ระบบล้มเหลว")

# ปิดเบราว์เซอร์
driver.quit()
