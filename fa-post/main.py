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
        'value': '19%3AzAyL2YXiSh_4pw%3A2%3A1720775422%3A-1%3A-1%3A%3AAcU_yRNYbIHyhj7OH_ZXO3GVduN1YqqJD8Y8inSDyQ',
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
        'value': '01ahWiYH59lE402S7.AWVlZai-QPKAJxKz0d-hIrUA-QM.BmkPL9..AAA.0.0.BmlNn8.AWUTRGQgj_Q',
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

    # Scroll through the timeline and fetch posts
    posts = []
    for _ in range(5):  # Adjust the range for more or fewer scrolls
        # Extract post content
        try:
            post_elements = driver.find_elements(By.XPATH, "//div[@data-pagelet='FeedUnit_{n}']")  # Adjust the XPath as needed

            for post_element in post_elements:
                try:
                    name = post_element.find_element(By.XPATH, ".//strong//span//a").text
                except Exception as e:
                    print(f"Error fetching name: {str(e)}")
                    name = "Unknown"

                try:
                    content = post_element.find_element(By.XPATH, ".//div[contains(@data-ad-comet-preview, 'message')]").text
                except Exception as e:
                    print(f"Error fetching content: {str(e)}")
                    content = "No content"

                try:
                    link = post_element.find_element(By.XPATH, ".//a[contains(@href, 'posts')]").get_attribute('href')
                except Exception as e:
                    print(f"Error fetching link: {str(e)}")
                    link = "No link"

                posts.append({
                    "name": name,
                    "content": content,
                    "link_post": link
                })

        except Exception as e:
            print(f"Error fetching posts: {str(e)}")

        # Scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    # Print fetched posts
    for post in posts:
        print("--------------------------------------------------------------")
        print(f"ชื่อคน: {post['name']}")
        print(f"content: {post['content']}")
        print(f"link_post: {post['link_post']}")
        print("--------------------------------------------------------------")

else:
    print("Login failed")

# Close the browser
driver.quit()
