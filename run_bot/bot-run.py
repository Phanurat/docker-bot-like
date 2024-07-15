from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import random
import requests

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# b_id bot
target_b_id = 'b00007'

# URL ของหน้า Facebook ที่ต้องการเข้าถึง
url = 'https://www.facebook.com/'

# Open the web page
driver.get(url)

def open_chat_meessage():
    url_open_message = "https://www.facebook.com/messages/e2ee/t/"
    driver.get(url_open_message)
    time.sleep(4)
    print("Opened chat message.")

# Event reaction like post
def love_post():
    try:
        print("Trying to love a post...")
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
        print("Trying to care a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        care_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(care_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Care แสดงขึ้นมาและคลิก
        care_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Care']"))
        )
        care_button.click()
        print("Cared the post.")
    except Exception as e:
        print(f"Error caring post: {str(e)}")

def haha_post():
    try:
        print("Trying to haha a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        haha_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(haha_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Haha แสดงขึ้นมาและคลิก
        haha_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Haha']"))
        )
        haha_button.click()
        print("Haha the post.")
    except Exception as e:
        print(f"Error haha post: {str(e)}")

def sad_post():
    try:
        print("Trying to sad a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        sad_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(sad_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Sad แสดงขึ้นมาและคลิก
        sad_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Sad']"))
        )
        sad_button.click()
        print("Sad the post.")
    except Exception as e:
        print(f"Error sad post: {str(e)}")

def angry_post():
    try:
        print("Trying to angry a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        angry_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(angry_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Angry แสดงขึ้นมาและคลิก
        angry_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Angry']"))
        )
        angry_button.click()
        print("Angry the post.")
    except Exception as e:
        print(f"Error angry post: {str(e)}")

def wow_post():
    try:
        print("Trying to wow a post...")
        # เลื่อนเมาส์ไปที่ปุ่มไลค์เพื่อให้ตัวเลือก reaction แสดงขึ้นมา
        wow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(wow_button).perform()
        time.sleep(2)  # รอให้ตัวเลือก reaction แสดงขึ้นมา

        # รอให้ปุ่ม Wow แสดงขึ้นมาและคลิก
        wow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Wow']"))
        )
        wow_button.click()
        print("Wow the post.")
    except Exception as e:
        print(f"Error wow post: {str(e)}")

## end function reaction post facebook

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

        print("Fetched random links.")
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

        # ค่าเดิมจากสุ่มรอบแรง
        # selected_comment = random.choice(comments)

        # Try Test
        selected_comment = comments
        print("Fetched random comments.")
        return selected_comment

    else:
        print(f"Error Status Code: {response.status_code}")
        return None
    
selected_comment = get_random_comment() 

def notify():
    print("Check Notifications!")
    #driver.get('https://www.facebook.com/notifications')
    #time.sleep(5)
    try:
        new_notification = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Notifications") and contains(@aria-label, "unread")]')
        if new_notification.is_displayed():
            print("You have new notifications!")
            driver.get('https://www.facebook.com/notifications')
            time.sleep(5)
        else:
            print("No new notifications.")
    
    except Exception as e:
        print("No new notifications.")
        return
        
def like_post():
    print("Trying to like a post...")
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
            raise Exception("No Comment")

        comment_input.click()
        time.sleep(2)
        
        # Random comment list
        comment_text = random.choice(selected_comment)

        for char in comment_text:
            comment_input.send_keys(char)
            time.sleep(0.5)
        comment_input.send_keys(Keys.ENTER)

        print(f"Add comment '{comment_text}' Done!")

    except Exception as e:
        print(f"Can't Comment: {str(e)}")
        return
    
    print("Comment it Work!")
    # Add your comment functionality here

def read_story():
    print("Reading Story!!")
    # Add your read story functionality here

def event_random():
    list_event = ["story", "like_post", "like_comment", "notify", "open_chat", "time_line"]
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
    
    elif random_event == "open_chat":
        #open_chat_meessage()
        print('Open Chat Open with Comming Soon!')
    
    elif random_event == "time_line":
        scroll_random = random.uniform(4, 6)
        print("Timeline Scroll Monitor!!")
        for _ in range(int(scroll_random)):
            driver.execute_script("window.scrollBy(0, 180);")
            time.sleep(15)

def timeline_scroll():
    scroll_random = random.uniform(4, 6)
    print("Timeline Scroll Monitor!!")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)

def login_succ(target_b_id):
    # List of cookies you provided
    
    bot_url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'

    response = requests.get(bot_url)
    if response.status_code == 200:
        data = response.json()
        try:
            selected_data = []
            
            for item in data['data']:
                if item['b_id'] == target_b_id:
                    selected_data.append({
                        'b_id': item['b_id'],
                        'c_user': item['c_user'],
                        'xs': item['xs'],
                        'datr': item['datr'],
                        'fr': item['fr']
                    })
            if not selected_data:
                print(f"No data found for b_id = {target_b_id}")
                exit()
            item = selected_data[0]
            c_user = item['c_user']
            xs = item['xs']
            datr = item['datr']
            fr = item['fr']

        except KeyError as e:
            exit()
    else:
        print("Error call back API:", response.status_code)
        exit()

    cookies_list = [
        {
            'name': 'c_user',
            'value': str(c_user),
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
            'value': str(xs),
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
            'value': str(datr),
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
            'value': str(fr),
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

login_succ(target_b_id)
