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

# ทดสอบเปิดเว็บไซต์
#driver.get('https://facebook.com')
#print(driver.title)

# ปิดเบราว์เซอร์
#driver.quit()

# List of cookies to add
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
        'value': '2%3ABwASFB4r47bAtQ%3A2%3A1719545387%3A-1%3A-1',
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
        'value': '6Cx-Zhni96Lh6q9j_Cjqpzo5',
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
        'value': '0dJySyDQ0Kl4a1EZ0.AWV1ESOocP2GBVatKHgOWkH2GMM.Bmfizo..AAA.0.0.Bmfi4t.AWWnm5QpXj0',
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

# Refresh the web page to use the cookies
driver.refresh()

# Wait for the web page to load completely
time.sleep(5)

# Check login status
if "Facebook" in driver.title:
    print("Logged in successfully")

    # Go to the link of the post to like
    post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid0m9A3o2mDipAtwHi6KRLWVkezSoRR46jxvoS2gZE9a6hbPrrnwHtroF3bURvv3JRvl'
    driver.get(post_url)

    # Wait for the web page to load completely
    time.sleep(5)

    # Scroll down to find the like button
    for _ in range(5):  # Adjust the number of scrolls as necessary
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)

    # Wait for the like button to appear
    like_button = None
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Like"]')
    except:
        print("Like button not found")

    if like_button:
        # Hover over the like button to reveal reactions icon
        webdriver.ActionChains(driver).move_to_element(like_button).perform()
        time.sleep(2)

        # Click the like button
        like_button.click()
        print("Post liked successfully")
    else:
        print("Login failed")

# Close the browser
driver.quit()
