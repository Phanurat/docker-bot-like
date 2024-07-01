from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize WebDriver with the path to chromedriver using Service object
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.facebook.com/'
driver.get(url)

def notify():
    print("Opening Notifications!")
    driver.get('https://www.facebook.com/notifications')
    time.sleep(5)

def like_post():
    print("Like Post!!")
    driver.get('https://www.facebook.com/')
    try:
        like_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Like']")
        if like_buttons:
            random.choice(like_buttons).click()
            print("กดไลค์โพสต์สำเร็จ")
        else:
            print("ไม่พบปุ่มไลค์")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการกดไลค์โพสต์: {str(e)}")

def link_comment():
    print("Comment it Work!")
    # Add your comment functionality here

def read_story():
    print("Reading Story!!")
    # Add your read story functionality here

def event_random():
    list_event = ["story", "like_post", "like_comment", "notify"]
    random_event = random.choice(list_event)
    print("Event Next ==>", random_event)

    if random_event == "story":
        read_story()
    
    elif random_event == "like_post":
        like_post()
    
    elif random_event == "like_comment":
        link_comment()
    
    elif random_event == "notify":
        notify()

def timeline_scroll():
    scroll_random = random.uniform(4, 6)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)

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
            event_random()
            timeline_scroll()
            time.sleep(5)
    else:
        print("การเข้าสู่ระบบล้มเหลว")

    # ปิดเบราว์เซอร์
    driver.quit()

login_succ()