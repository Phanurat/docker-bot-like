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

# URL of the Facebook page you want to access
url = 'https://www.facebook.com/'

# Open the web page
driver.get(url)

def get_random_comment():
    # URL of Google Apps Script API
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        comments = [item['comment'] for item in data['data']]

        selected_comment = random.choice(comments)
        return selected_comment
    
    else:
        print(f"Error Status code: {response.status_code}")
        return None

selected_comment = get_random_comment()

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
        'value': '13%3AF_hwo-RDE3f17A%3A2%3A1720507723%3A-1%3A-1%3A%3AAcWoZWqhPYZifyy-wKqyF7bRknYAmZYMXDrvQXIEJg',
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
        'value': 'Tt2MZqlcsW5DdHzwIMHV6aR2',
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
        'value': '10NpXlDmIlfZAIY4B.AWW1OCuxDctfVNNIXA5rCKn9_F8.BmjOAs..AAA.0.0.BmjOEC.AWXKxjDp0bk',
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
    if cookie['expires']:
        cookie['expires'] = int(cookie['expires'])
    driver.add_cookie(cookie)

# Refresh the web page to use cookies
driver.refresh()

# Wait for the web page to load completely
time.sleep(5)

# Check login status
if "Facebook" in driver.title:
    print("Login successful")

    try:
        # Go to the post where you want to comment
        post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'
        driver.get(post_url)
        time.sleep(5)

        # Find and click on the comment box using a more reliable XPath
        comment_input = driver.find_element(By.XPATH, '//div[@role="textbox"][@contenteditable="true"]')
        comment_input.click()
        time.sleep(2)

        # Type and post comment character by character
        for char in selected_comment:
            comment_input.send_keys(char)
            time.sleep(0.5)  # Adjust as needed for typing speed
        comment_input.send_keys(Keys.ENTER)
        print(f"Successfully commented: '{selected_comment}'")

    except Exception as e:
        print(f"Error commenting on post: {str(e)}")


else:
    print("Login failed")

# Close the browser
driver.quit()
