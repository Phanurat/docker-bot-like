from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # ตั้งค่าโปรไฟล์
    path_to_user_data = 'C:/Users/Jakkranukoolki/AppData/Local/Google/Chrome/User Data'
    profile_name = 'Profile 2'
    chrome_options.add_argument(f"--user-data-dir={path_to_user_data}")
    chrome_options.add_argument(f"--profile-directory={profile_name}")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# ใช้ฟังก์ชัน get_driver() เพื่อเปิดเบราว์เซอร์
driver = get_driver()

# เปิดเว็บไซต์
driver.get('https://www.google.com')

# รอให้คุณดูผลลัพธ์
input("Press Enter to close the browser...")

# ปิดเบราว์เซอร์
driver.quit()
