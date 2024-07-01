from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the Facebook profile page you want to access
url = 'https://www.facebook.com/phanurat.jakkranukoolkit'

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
        'value': '33%3A6G4mSdVIL5wfOQ%3A2%3A1719565792%3A-1%3A-1',
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
        'value': '9DV9ZozopZitRFfYOfDeZhrr',
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
        'value': '1aEI7b51g68G8tVZ6.AWWn_uziFl2gSX0P-aIcVa65zDo.BmfnS-..AAA.0.0.Bmfn3i.AWUsEx6r6U8',
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

    try:
        # Find all posts on the Facebook page
        posts = driver.find_elements(By.XPATH, "//div[@data-pagelet='FeedUnit_{n}']")
        for post in posts:
            try:
                # Click on the comment box of the post
                comment_box = post.find_element(By.XPATH, ".//textarea[contains(@aria-label, 'Comment on this post')]")
                comment_box.click()
                time.sleep(2)  # Wait for the comment box to open
                comment_box.send_keys("Hello from Python Selenium!")  # Type the comment
                comment_box.send_keys(Keys.ENTER)  # Press Enter to post the comment

                print("Commented successfully")
            except Exception as e:
                print(f"Error commenting on post: {str(e)}")
    except Exception as e:
        print(f"Error finding or commenting on posts: {str(e)}")

else:
    print("Login failed")

# Close the browser
driver.quit()
