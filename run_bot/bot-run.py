from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import random
import time
import requests

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

def get_random_link():
    # URL ของ Google Apps Script API
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"

    # ส่งคำขอ GET ไปยัง API
    response = requests.get(api_link_url)

    # ตรวจสอบสถานะคำขอ
    if response.status_code == 200:
        # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
        data = response.json()

        # สร้าง list ของ comment
        links = [item['link'] for item in data['data']]

        return links

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

selected_link = get_random_link()

def get_random_comment():
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]

        #ค่าเดิมจากสุ่มรอบแรง
        #selected_comment = random.choice(comments)

        #Try Test
        selected_comment = comments
        return selected_comment

    else:
        print(f"Error Status Code: {response.status_code}")
        return None
    
selected_comment = get_random_comment() 

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
    #post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'
    post_url = selected_link
    driver.get(random.choice(post_url))
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
        
        #random comment list
        comment_text = random.choice(selected_comment)
        comment_input.send_keys(comment_text)
        comment_input.send_keys(Keys.ENTER)
        print(f"Add comment'{comment_text}' Done!")

    except Exception as e:
        print(f"Can't Comment: {str(e)}")
    
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
        while True:
            event_random()
            timeline_scroll()
            time.sleep(5)
    else:
        print("การเข้าสู่ระบบล้มเหลว")

    # ปิดเบราว์เซอร์
    driver.quit()

login_succ()