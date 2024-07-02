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

# URL of the Facebook page to access
url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'

# Open the web page
driver.get(url)

# List of cookies provided
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
        'value': '27%3AO7lf2Br_zLQqDg%3A2%3A1719806925%3A-1%3A-1',
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
        'value': 'IGaBZofFdrTky3WbsH7c9oSG',
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
        'value': '0fAyHsfOcLQLhRWWF.AWWOpJ7tqCdu3z1cGNe2bqGMT-w.BmgWYg..AAA.0.0.BmgivP.AWUyO8hDlT0',
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
    driver.add_cookie(cookie)

# Refresh the web page to use cookies
driver.refresh()

# Wait for the web page to finish loading
time.sleep(5)

# Check login status
if "Facebook" in driver.title:
    print("เข้าสู่ระบบสำเร็จ")
    
    # Navigate to the link of the post to like
    post_url = 'https://www.facebook.com/phanurat.jakkranukoolkit/posts/pfbid02TN75sqFQbG626rmyEfJgoVRY6tCqa56HHufVxocvfecMCJKLoZZtWo5ZeDEtcn6ol'
    driver.get(post_url)
    
    # Wait for the web page to finish loading
    time.sleep(5)
    
    # Scroll down to find the like button
    for _ in range(5):  # Adjust the number of times to scroll as needed
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)
        
    # Wait for the like button to appear
    like_button = None
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Like"]')
    except:
        print("ไม่พบปุ่มไลค์")

    if like_button:
        # Hover over the like button to reveal the reactions icon
        webdriver.ActionChains(driver).move_to_element(like_button).perform()
        time.sleep(2)
        
        # Click the like button
        like_button.click()
        print("ไลค์โพสต์สำเร็จ")
        
        # Wait for the comment input area to be visible
        try:
            comment_input = driver.find_element(By.XPATH, '//div[@role="textbox" and @aria-label="Comment on this post"]')
            comment_input.click()
            time.sleep(2)
            
            # Enter the comment text
            comment_text = "Hello from the automated bot!"
            comment_input.send_keys(comment_text)
            comment_input.send_keys(Keys.ENTER)
            print(f"เพิ่มคอมเมนต์ '{comment_text}' สำเร็จ")
            
        except Exception as e:
            print(f"ไม่สามารถเพิ่มคอมเมนต์ได้: {str(e)}")

            
    else:
        print("ไม่สามารถหาปุ่มไลค์ได้ หรือ การเข้าสู่ระบบล้มเหลว")

else:
    print("การเข้าสู่ระบบล้มเหลว")

# Close the browser
driver.quit()
