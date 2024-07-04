from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.facebook.com/'
driver.get(url)

#event reaction like post
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

def care_post():
    try:
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        care_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(care_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
        care_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Care']"))
        )
        care_button.click()
        print("Care the post.")
    except Exception as e:
        print(f"Error Caring post: {str(e)}")
    
def haha_post():
    try:
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        haha_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(haha_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
        haha_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Haha']"))
        )
        haha_button.click()
        print("Haha the post.")
    except Exception as e:
        print(f"Error Haha post: {str(e)}")

def sad_post():
    try:
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        sad_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(sad_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
        sad_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Sad']"))
        )
        sad_button.click()
        print("Sad the post.")
    except Exception as e:
        print(f"Error Sad post: {str(e)}")

def angry_post():
    try:
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        angry_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(angry_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
        angry_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Angry']"))
        )
        angry_button.click()
        print("Angry the post.")
    except Exception as e:
        print(f"Error Angry post: {str(e)}")

def wow_post():
    try:
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        wow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(wow_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Love แสดงขึ้นมาและคลิก
        wow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Wow']"))
        )
        wow_button.click()
        print("Wow the post.")
    except Exception as e:
        print(f"Error Wow post: {str(e)}")

## end function reaction post facebook

def get_random_link():
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"
    response = requests.get(api_link_url)

    if response.status_code == 200:
        data = response.json()
        
        links = [item['link'] for item in data['data']]
        
        return links
    
    else:
        print(f"Failed to data. Status code: {response.status_code}")
        return links
    
selected_link = get_random_link()

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
    
    #post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'
    post_url = random.choice(selected_link)
    driver.get(post_url)
    time.sleep(5)

    reaction_random = ["like", "love", "care", "haha", "wow", "sad", "angry", "not_reaction"]

    selected_reaction = random.choice(reaction_random)

    if selected_reaction == "like":
        like_post()
    elif selected_reaction == "love":
        love_post()
    elif selected_reaction == "care":
        care_post()
    elif selected_reaction == "haha":
        haha_post()
    elif selected_reaction == "wow":
        wow_post()
    elif selected_reaction == "sad":
        sad_post()
    elif selected_reaction == "angry":
        angry_post()

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