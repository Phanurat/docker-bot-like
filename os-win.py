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
    
    # ไปที่ลิงก์ของโพสต์ที่ต้องการไลค์
    post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid0m9A3o2mDipAtwHi6KRLWVkezSoRR46jxvoS2gZE9a6hbPrrnwHtroF3bURvv3JRvl'
    driver.get(post_url)
    
    # รอเวลาให้หน้าเว็บโหลดเสร็จ
    time.sleep(5)
    
    # เลื่อนหน้าจอลงเพื่อค้นหาปุ่มไลค์
    for _ in range(5):  # ปรับจำนวนครั้งที่เลื่อนตามความจำเป็น
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)
        
    # รอให้ปุ่มไลค์ปรากฏขึ้น
    like_button = None
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Like"]')
    except:
        print("ไม่พบปุ่มไลค์")

    if like_button:
        # วางเมาส์บนปุ่มไลค์เพื่อเปิดไอคอน reactions
        webdriver.ActionChains(driver).move_to_element(like_button).perform()
        time.sleep(2)
        
        # คลิกปุ่มไลค์
        like_button.click()
        print("Post liked successfully")
    else:
        print("การเข้าสู่ระบบล้มเหลว")

# ปิดเบราว์เซอร์
driver.quit()
