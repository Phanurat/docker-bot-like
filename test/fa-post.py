from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

# URL of the Facebook login page
url = 'https://www.facebook.com/'

# Open the web page
driver.get(url)

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
        'value': '45%3A-6ZMkdlT_BAOEA%3A2%3A1720756466%3A-1%3A-1%3A%3AAcXfBx_8Csqrpu-SwL5rr5C_5I-7r-PcO4hEs2AtuQ',
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
        'value': '__GMZCgwVF5BbyvAtfJojQwg',
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
        'value': '0n3O5VVBilRTVmWw2.AWWz9H5S-PRVlk8QOp3Vetf2BVs.BmkKjx..AAA.0.0.BmkKj1.AWUBDBRN0kI',
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
    print("Login successful")

    message = "Test Post"

    def post_status(message):
        url = 'https://www.facebook.com/profile.php'
        # Open the profile page
        driver.get(url)
        
        # Scroll down to make sure the post box is in view
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the scroll to complete
        
        # Navigate to the post box
        post = "What's on your mind?"
        post_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@aria-label="{post}"]'))
        )
        post_box.click()
        
        # Wait for the post dialog to appear
        time.sleep(2)
        
        # Find active element and enter the message
        active_post_box = driver.switch_to.active_element
        active_post_box.send_keys(message)
        
        # Wait for the message to be entered
        time.sleep(2)
        
        # Find and click the Post button
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Post"]'))
        )
        post_button.click()
        
        # Wait for the post to be published
        time.sleep(5)

    post_status(message)
else:
    print("Login failed")

# Close the browser
driver.quit()
