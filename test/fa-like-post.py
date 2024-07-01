from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import requests

# Options for ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver using WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL API
api_url = "https://script.google.com/macros/s/AKfycbzP9ClJHYTkQ9UtWgV-rsLr0Z-gLdsxMA-amAGiPpt1ZWtvfIKTSQj2uXk1JX5__SvgTw/exec"

def check_and_process(data, key):
    link_found = False
    process_link = None
    for item in data['data']:
        if key in item and item[key]:
            link_found = True
            print("Have Link")
            process_link = process(item[key])
            break
    if not link_found:
        print("Don't have link")
        process_link = 'https://www.facebook.com/'  # Default URL to visit if no link found
    
    return process_link

def process(value):
    print(f"Processing value: {value}")
    return value

# Fetch data from API
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    url_to_visit = check_and_process(data, 'link')

    # Open the web page
    driver.get(url_to_visit)

    # List of cookies you provided
    cookies_list = [
        {
            'name': 'c_user',
            'value': '61551780956965',
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': False,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'xs',
            'value': '27%3AO7lf2Br_zLQqDg%3A2%3A1719806925%3A-1%3A-1',
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'datr',
            'value': 'IGaBZofFdrTky3WbsH7c9oSG',
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2025-06-28T01:12:26.667Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        },
        {
            'name': 'fr',
            'value': '0fAyHsfOcLQLhRWWF.AWWOpJ7tqCdu3z1cGNe2bqGMT-w.BmgWYg..AAA.0.0.BmgivP.AWUyO8hDlT0',
            'domain': '.facebook.com',
            'path': '/',
            'expires': int(datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()),
            'httpOnly': True,
            'secure': True,
            'session': False,
            'sameSite': 'None'
        }
    ]

    # Add cookies to the browser
    for cookie in cookies_list:
        driver.add_cookie(cookie)

    # Refresh the web page to use cookies
    driver.refresh()

    # Wait for the web page to load completely
    time.sleep(5)

    # Check login status
    if "Facebook" in driver.title:
        # Assuming you want to like the first post that appears
        try:
            like_button = driver.find_element(By.XPATH, "//div[@aria-label='Like']")
            like_button.click()
            print("Logged in successfully and liked the post.")
        except Exception as e:
            print(f"Error liking post: {str(e)}")
    else:
        print("Login failed or title does not match 'Facebook'.")

else:
    print(f"Failed to fetch data from API. Status Code: {response.status_code}")

# Close the browser
driver.quit()
