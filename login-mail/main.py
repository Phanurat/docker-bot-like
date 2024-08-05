from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--lang=en")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

cookies_file = "cookies.json"

def load_cookies(driver, cookies_file):
    driver.get("https://accounts.google.com/")
    time.sleep(5)  # Wait for the page to load

    # Load cookies
    with open(cookies_file, "r") as file:
        cookies = json.load(file)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()  # Refresh to apply cookies

def main():
    driver = get_driver()
    
    try:
        load_cookies(driver, "login-mail/cookies.json")  # Adjust path to your cookies file
        driver.get("https://colab.research.google.com/drive/1RMATUumSYdvqzE_tzlgEM_x6gE76U9Od?usp=sharing")
        time.sleep(30)  # Wait for Colab to load
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
