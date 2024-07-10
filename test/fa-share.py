from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

def login_and_post():
    # Configure ChromeDriver options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # URL of the Facebook login page
    url = 'https://www.facebook.com/'

    try:
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
                'value': '13%3AF_hwo-RDE3f17A%3A2%3A1720507723%3A-1%3A-1%3A%3AAcVC8c8tbR4-LA4Vv3wp19DIYUvaKRzszfWCM1MJ0Q',
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
                'value': '1j39NyLJ2YqgvD8j2.AWWnw_G0lVxPG8Ca3k6vMO7WloE.BmjhDl..AAA.0.0.BmjhDl.AWVH8LHQaTI',
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
        WebDriverWait(driver, 10).until(EC.title_contains("Facebook"))
        print("Logged in successfully")

        # Navigate to the Facebook profile page (you may adjust the URL as needed)
        driver.get("https://www.facebook.com")

        # Wait for the profile page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-contents='true']")))

        # Find the post field and input your message
        post_message = "Hello, this is a test post using Selenium WebDriver!"
        post_field = driver.find_element(By.XPATH, "//div[@data-contents='true']")
        post_field.send_keys(post_message)

        # Click on the Post button
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='mount_0_0_Ph']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div"))
        )
        post_button.click()
        print("Successfully Posted On Facebook")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Quit the WebDriver
        driver.quit()

# Call the function to login and post on Facebook
login_and_post()
