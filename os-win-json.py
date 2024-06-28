import json
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
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.facebook.com/'
driver.get(url)

# Load cookies from the JSON file
with open('json/cookies.json', 'r') as file:
    cookies_list = json.load(file)

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
        print("Like button not found")
else:
    print("Login failed")

# Close the browser
driver.quit()
