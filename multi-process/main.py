from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process

def open_chrome(url):
    # Options for ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Initialize WebDriver using WebDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get(url)
    print(driver.title)
    driver.quit()

if __name__ == '__main__':
    urls = ['https://www.google.com/', 'https://www.facebook.com/', 'https://www.youtube.com/']
    processes = []
    
    for url in urls:
        p = Process(target=open_chrome, args=(url,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

