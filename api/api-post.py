import requests
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time

# Define the target b_id
target_b_id = 'b00012'
url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'

# Send GET request to fetch data
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    try:
        selected_data = [item for item in data['data'] if item['b_id'] == target_b_id]
        if not selected_data:
            print(f"No data found for b_id = {target_b_id}")
            exit()

        item = selected_data[0]
        c_user = item['c_user']
        xs = item['xs']
        datr = item['datr']
        fr = item['fr']

    except KeyError as e:
        print(f'Error retrieving data: {e}')
        exit()

else:
    print('API request error:', response.status_code)
    exit()

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Facebook
driver.get('https://www.facebook.com')

# Define cookies
cookies_list = [
    {'name': 'c_user', 'value': c_user, 'domain': '.facebook.com', 'path': '/', 'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(), 'httpOnly': False, 'secure': True, 'session': False, 'sameSite': 'None'},
    {'name': 'xs', 'value': xs, 'domain': '.facebook.com', 'path': '/', 'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(), 'httpOnly': True, 'secure': True, 'session': False, 'sameSite': 'None'},
    {'name': 'datr', 'value': datr, 'domain': '.facebook.com', 'path': '/', 'expires': datetime.strptime('2025-06-28T01:12:26.667Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(), 'httpOnly': True, 'secure': True, 'session': False, 'sameSite': 'None'},
    {'name': 'fr', 'value': fr, 'domain': '.facebook.com', 'path': '/', 'expires': datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(), 'httpOnly': True, 'secure': True, 'session': False, 'sameSite': 'None'}
]

# Add cookies
for cookie in cookies_list:
    if cookie['value']:
        cookie['expires'] = int(cookie['expires']) if cookie.get('expires') else None
        driver.add_cookie(cookie)

# Refresh page to apply cookies
driver.refresh()
time.sleep(5)

# Check login status
if "Facebook" in driver.title:
    print("Login successful")

    cookies = "ps_n=1;ps_l=1;sb=5o9lZqfD3uxVf7Awmyey52Jk;datr=5o9lZp_zZR7S04tn5dD3UR57;c_user=100091056858327;fr=1LZsHRc5od7pEQ7Se.AWVYim7KB1AqgvFP_2sCOaKY-TM.Bmqvew..AAA.0.0.Bmqvew.AWUJjWu60Uk;xs=35%3AYjr2hbeI7fDd_g%3A2%3A1717932013%3A-1%3A6280%3A%3AAcV9gQHXMIPfSWHy1MG86_o4zCQppAaC0JfDGyQuXks;wd=1653x822;dpr=1.125;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1722480560557%2C%22v%22%3A1%7D;"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9,vi;q=0.8,fr-FR;q=0.7,fr;q=0.6,vi-VN;q=0.5,nl;q=0.4",
        "cache-control": "max-age=0",
        "cookie": cookies,
        "dpr": "1.25",
        "origin": "https://mbasic.facebook.com",
        "priority": "u=0, i",
        "referer": "https://mbasic.facebook.com/",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-full-version-list": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.185\", \"Google Chrome\";v=\"126.0.6478.185\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "\"\"",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "viewport-width": "980"
    }

    response = requests.get("https://m.facebook.com/", headers=headers)

    # Helper function to safely extract data
    def safe_search(pattern, text):
        match = re.search(pattern, text)
        return match.group(1) if match else None

    user = safe_search(r"\"USER_ID\":\"([^\"]*)\"", response.text)
    fb_dtsg = safe_search(r"\"DTSGInitialData\",\\[\\],{\"token\":\"([^\"]+)\"", response.text)
    lsd = safe_search(r"\"LSD\",\\[\\],{\"token\":\"([^\"]+)\"", response.text)
    jazoest = safe_search(r"(?:^|&)jazoest=(\d+)", response.text)
    spin_r = safe_search(r"\"__spin_r\":(\d+)", response.text)
    spin_t = safe_search(r"\"__spin_t\":(\d+)", response.text)
    hsi = safe_search(r"\"hsi\":\"(\d+)", response.text)
    req = safe_search(r"_req=(\d+)", response.text)
    rev = safe_search(r"\"server_revision\":(.*?),", response.text)
    hs = safe_search(r"\"haste_session\":\"(.*?)\",", response.text)

    if not all([user, fb_dtsg, lsd, jazoest, spin_r, spin_t, hsi, req, rev, hs]):
        print("Failed to retrieve some of the required tokens.")
        driver.quit()
        exit()

    post_data = {
        "fb_dtsg": fb_dtsg,
        "jazoest": jazoest,
        "privacyx": "300645083384735",
        "r2a": "1",
        "xhpc_timeline": "1",
        "target": user,
        "c_src": "timeline_self",
        "cwevent": "composer_entry",
        "referrer": "timeline",
        "ctype": "inline",
        "cver": "amber",
        "rst_icv": "",
        "xc_message": "Your message here",
        "view_post": "Post"
    }

    post_headers = headers.copy()
    post_headers["referer"] = f"https://mbasic.facebook.com/{user}"

    response = requests.post(f"https://mbasic.facebook.com/composer/mbasic/?av={user}&eav=AfaTJ-9sPWfjAPAaJcmpNLp3EkfZ5cM5gz_t3dlaeVcpJ3Fi9-20SZiUrip00TolP_A&paipv=0&refid=17", data=post_data, headers=post_headers)

    if response.status_code == 200:
        print("Post successful")
    else:
        print("Post failed")
else:
    print("Login failed")

# Close the browser
driver.quit()
