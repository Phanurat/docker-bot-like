from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Open the web page
driver.get(url)

def login_succ():
    # List of cookies you provided
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
        
        # เข้าสู่หน้าโพสต์ที่ต้องการกดเลิฟ
        post_link = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid0Q8GREAvWkAuirbFDdW2RfYw5eDYYYGk1ifit1dTMSBmpaXHNdqR4KwAUzcGH9Kj1l'  # ใส่ลิงก์ของโพสต์ที่คุณต้องการกดเลิฟ
        driver.get(post_link)
        time.sleep(5)  # รอให้หน้าโพสต์โหลดเสร็จ

        # กดเลิฟโพสต์
        def love_post():
            try:
                # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
                like_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
                )
                actions = ActionChains(driver)
                actions.move_to_element(like_button).perform()
                time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

                # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
                love_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Love']"))
                )
                love_button.click()
                print("Loved the post.")
            except Exception as e:
                print(f"Error loving post: {str(e)}")

        # เรียกใช้ฟังก์ชันกดเลิฟโพสต์
        love_post()
        
    else:
        print("การเข้าสู่ระบบล้มเหลว")

    # ปิดเบราว์เซอร์
    driver.quit()

# Run the login function
login_succ()
