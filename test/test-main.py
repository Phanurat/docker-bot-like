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

# Initialize ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Facebook URL
url = 'https://www.facebook.com/'
driver.get(url)

# Global variables
target_b_id = 'b00007'

# Helper Functions
def add_cookies(target_b_id):
    bot_url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'
    response = requests.get(bot_url)
    if response.status_code != 200:
        print(f"Failed to get cookies data: {response.status_code}")
        return False
    
    data = response.json()
    cookies_list = []

    for item in data['data']:
        if item['b_id'] == target_b_id:
            cookies_list = [
                {
                    'name': 'c_user',
                    'value': str(item['c_user']),
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
                    'value': str(item['xs']),
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
                    'value': str(item['datr']),
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
                    'value': str(item['fr']),
                    'domain': '.facebook.com',
                    'path': '/',
                    'expires': datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
                    'httpOnly': True,
                    'secure': True,
                    'session': False,
                    'sameSite': 'None'
                }
            ]
            break

    if not cookies_list:
        print(f"No data found for b_id = {target_b_id}")
        return False

    for cookie in cookies_list:
        if cookie['expires']:
            cookie['expires'] = int(cookie['expires'])
        driver.add_cookie(cookie)
    
    driver.refresh()
    time.sleep(5)
    return True

def check_notifications():
    try:
        new_notification = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Notifications") and contains(@aria-label, "unread")]')
        if new_notification.is_displayed():
            print("You have new notifications!")
            driver.get('https://www.facebook.com/notifications')
            time.sleep(5)
        else:
            print("No new notifications.")
    except:
        print("No new notifications.")

def open_chat_message():
    driver.get("https://www.facebook.com/messages/e2ee/t/")
    time.sleep(4)
    print("Opened chat message.")

def react_to_post(reaction):
    try:
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
        print(f"{reaction} the post.")
    except Exception as e:
        print(f"Error reacting to post: {str(e)}")

def get_random_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return [item for item in data['data']]
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def get_random_link():
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"
    links = get_random_data(api_link_url)
    return [link['link'] for link in links] if links else None

def get_random_comment():
    api_comment_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"
    comments = get_random_data(api_comment_url)
    return [comment['comment'] for comment in comments] if comments else None

def comment_on_link():
    links = get_random_link()
    comments = get_random_comment()
    
    if not links or not comments:
        print("No links or comments to work with.")
        return

    post_url = random.choice(links)
    driver.get(post_url)
    time.sleep(5)

    reactions = ["Like", "Love", "Care", "Haha", "Wow", "Sad", "Angry", "not_reaction"]
    selected_reaction = random.choice(reactions)

    if selected_reaction != "not_reaction":
        react_to_post(selected_reaction)

    time.sleep(5)

    try:
        comment_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Write a comment"]'))
        )
        comment_input.click()
        time.sleep(2)

        comment_text = random.choice(comments)
        for char in comment_text:
            comment_input.send_keys(char)
            time.sleep(0.1)  # Reduce delay for faster typing
        comment_input.send_keys(Keys.ENTER)
        print(f"Added comment: {comment_text}")
    except Exception as e:
        print(f"Failed to add comment: {str(e)}")

def read_story():
    print("Reading Story...")
    # Implement story reading functionality here

def like_post():
    try:
        print("Liking a post...")
        driver.get('https://www.facebook.com/')
        like_buttons = driver.find_elements(By.XPATH, "//div[@aria-label='Like']")
        if like_buttons:
            random.choice(like_buttons).click()
            print("Liked a post.")
        else:
            print("No like buttons found.")
    except Exception as e:
        print(f"Error liking post: {str(e)}")

def perform_random_event():
    events = ["story", "like_post", "like_comment", "notify", "open_chat", "time_line"]
    event = random.choice(events)
    print(f"Next event: {event}")

    if event == "story":
        read_story()
    elif event == "like_post":
        like_post()
    elif event == "like_comment":
        comment_on_link()
    elif event == "notify":
        check_notifications()
    elif event == "open_chat":
        open_chat_message()
    elif event == "time_line":
        scroll_timeline()

def scroll_timeline():
    print("Scrolling through timeline...")
    for _ in range(random.randint(4, 6)):
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)

def main():
    if add_cookies(target_b_id):
        print("Successfully logged in.")
        while True:
            perform_random_event()
            scroll_timeline()
            time.sleep(random.randint(5, 10) * 60)
    else:
        print("Failed to log in.")

if __name__ == "__main__":
    main()
