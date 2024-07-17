from typing import List
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
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# b_id bot
target_b_id = 'b00008'

# URL ของหน้า Facebook ที่ต้องการเข้าถึง
url = 'https://www.facebook.com/'

# Open the web page
driver.get(url)

def open_chat_message():
    url_open_message = "https://www.facebook.com/messages/e2ee/t/"
    driver.get(url_open_message)
    time.sleep(4)
    logging.info("Opened chat message.")

# Function to perform reactions
def react_to_post(reaction: str):
    try:
        logging.info(f"Trying to react to a post with {reaction}...")
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(like_button).perform()
        time.sleep(2)

        reaction_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@aria-label='{reaction}']"))
        )
        reaction_button.click()
        logging.info(f"Reacted to the post with {reaction}.")
    except Exception as e:
        logging.error(f"Error reacting to post with {reaction}: {str(e)}")

# Map for reaction functions
reactions_map = {
    "like": "Like",
    "love": "Love",
    "care": "Care",
    "haha": "Haha",
    "sad": "Sad",
    "angry": "Angry",
    "wow": "Wow"
}

def get_random_link() -> List[str]:
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"
    response = requests.get(api_link_url)
    if response.status_code == 200:
        data = response.json()
        links = [item['link'] for item in data['data']]
        logging.info("Fetched random links.")
        return links
    else:
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")
        return []

selected_links = get_random_link()

def get_random_comment() -> List[str]:
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]
        logging.info("Fetched random comments.")
        return comments
    else:
        logging.error(f"Error Status Code: {response.status_code}")
        return []

selected_comments = get_random_comment()

def notify():
    logging.info("Check Notifications!")
    try:
        new_notification = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Notifications") and contains(@aria-label, "unread")]')
        if new_notification.is_displayed():
            logging.info("You have new notifications!")
            driver.get('https://www.facebook.com/notifications')
            time.sleep(5)
        else:
            logging.info("No new notifications.")
    except Exception as e:
        logging.info("No new notifications.")
        return

def like_post():
    logging.info("Trying to like a post...")
    driver.get('https://www.facebook.com/')
    try:
        like_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Like']")
        if like_buttons:
            random.choice(like_buttons).click()
            logging.info("Liked the post successfully.")
        else:
            logging.info("No like buttons found.")
    except Exception as e:
        logging.error(f"Error liking post: {str(e)}")

def link_comment():
    post_url = random.choice(selected_links)
    driver.get(post_url)
    time.sleep(5)

    selected_reaction = random.choice(list(reactions_map.keys()) + ["not_reaction"])
    if selected_reaction != "not_reaction":
        react_to_post(reactions_map[selected_reaction])
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
            raise Exception("No Comment Input Found")

        comment_input.click()
        time.sleep(2)
        
        comment_text = random.choice(selected_comments)
        for char in comment_text:
            comment_input.send_keys(char)
            time.sleep(0.5)
        comment_input.send_keys(Keys.ENTER)
        logging.info(f"Added comment '{comment_text}' successfully.")
    except Exception as e:
        logging.error(f"Error commenting on post: {str(e)}")

def read_story():
    logging.info("Reading Story!")
    # Implement your read story functionality here

def event_random():
    list_event = ["story", "like_post", "like_comment", "notify", "open_chat", "time_line"]
    random_event = random.choice(list_event)
    logging.info(f"Next Event: {random_event}")

    if random_event == "story":
        read_story()
    elif random_event == "like_post":
        like_post()
    elif random_event == "like_comment":
        link_comment()
    elif random_event == "notify":
        notify()
    elif random_event == "open_chat":
        open_chat_message()
    elif random_event == "time_line":
        timeline_scroll()

def timeline_scroll():
    scroll_random = random.uniform(4, 6)
    logging.info("Scrolling through the timeline.")
    for _ in range(int(scroll_random)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)

def break_automate():
    break_time = random.randint(5, 10)
    logging.info(f"End session! Taking a break for {break_time} seconds.")
    time.sleep(break_time)
    driver.quit()

def login_succ(target_b_id):
    api_url = f"https://script.google.com/macros/s/AKfycbxzvH6HDjW8aMF4mAxWud_w_4VEu8LEeoIlMfSk4OHU3SzLsUOTlTB-m3fKnZs_XpGb/exec?target_b_id={target_b_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        cookies = response.json()
        for cookie in cookies:
            driver.add_cookie(cookie)
        logging.info("Successfully added cookies.")
    else:
        logging.error(f"Failed to retrieve cookies. Status code: {response.status_code}")

    driver.get("https://www.facebook.com")
    time.sleep(3)

    for _ in range(10):
        event_random()
        time.sleep(5)

    break_automate()

login_succ(target_b_id)
