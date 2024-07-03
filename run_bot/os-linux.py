from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import requests

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize WebDriver with the path to chromedriver using Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.facebook.com/'
driver.get(url)

def get_link_post():
    api_link_url = "https://script.google.com/macros/s/AKfycbwex5szoBPlP4sW1c3lNLqecfAKwOnm6XnaiJUIaO33MSzhFXDXZTItwKH7cH1vCq3YIw/exec"

    response = requests.get(api_link_url)

    if response.status_code == 200:
        data = response.json()
        links = [item['link'] for item in data['data']]
        return links
    else:
        print(f"Error Status Code: {response.status_code}")
        return []

def get_random_comment():
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]
        return random.choice(comments)
    else:
        print(f"Error Status Code: {response.status_code}")
        return ""

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
    selected_link = get_link_post()
    if not selected_link:
        print("ไม่มีลิงก์โพสต์ที่ได้รับมา")
        return

    post_url = random.choice(selected_link)
    driver.get(post_url)
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
            raise Exception("ไม่สามารถหาช่องคอมเมนต์ได้")

        comment_input.click()
        time.sleep(2)

        comment_text = get_random_comment()
        if not comment_text:
            print("ไม่มีคอมเมนต์ที่ได้รับมา")
            return

        comment_input.send_keys(comment_text)
        comment_input.send_keys(Keys.ENTER)
        print(f"เพิ่มคอมเมนต์ '{comment_text}' สำเร็จ")
    except Exception as e:
        print(f"ไม่สามารถเพิ่มคอมเมนต์ได้: {str(e)}")

def read_story():
    print("Reading Story!!")
    driver.get('https://www.facebook.com/stories')  # ปรับ URL ตามที่ต้องการ
    time.sleep(5)
    try:
        story_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Play']")
        if story_buttons:
            random.choice(story_buttons).click()
            print("กำลังดู Story")
        else:
            print("ไม่พบปุ่มเล่น Story")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดู Story: {str(e)}")

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
