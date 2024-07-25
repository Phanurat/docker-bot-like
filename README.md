# Bot Facebook Login By Token Cookies
 Automation bot facebook

 ## Getting Started
 - Copy Cookies For Run Python Script

 ### Requement System
 - python version >= 3.8
 - Window10
 - Linux Ununtu

 ### Clone Project
 ```sh
git clone https://github.com/Phanurat/docker-bot-like.git
cd dokcer-bot-like
```

 ### Install Linux Ubuntu 
 ```sh
 sudo apt-get install python3
 ```
 #### install webdirver 
 ```sh
 pip install webdriver-manager
 ```
 Download Chromedriver
 ```sh
 wget https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
```
 Extract Zip
 ```sh
 unzip chromedriver_linux64.zip
```
 move
 ```sh
 sudo mv chromedriver /usr/local/bin/
```

## FireFox Browser use on Colab

```sh
    !apt-get update
    !apt-get install firefox
    !apt-get install -y xvfb
    !pip install pyvirtualdisplay selenium
    !wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
```
### Extract and move root path
```sh
    !tar -xvzf geckodriver-v0.32.0-linux64.tar.gz
    !rm geckodriver-v0.32.0-linux64.tar.gz
```
### Use Firefox python.ipynb
```sh
#Test use firefox
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
```
### Import code and show title to link driver to
```sh
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")

print(driver.title)

driver.quit()
```

## Google Colab
```sh
!pip install selenium
!pip install webdriver-manager
```

###  Install the Chrome browser
```sh
!apt-get update
!apt-get install -y wget unzip
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!dpkg -i google-chrome-stable_current_amd64.deb
!apt-get -f install -y
```
###  Install a compatible version of chromedriver
```sh
!wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!chmod +x chromedriver
!mv -f chromedriver /usr/local/bin/chromedriver
```
### Dowload Chromedrive
```sh
!wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb
!dpkg -i google-chrome-stable_114.0.5735.90-1_amd64.deb
!apt-get -f install -y
```

# USE COLAB 
## Run file /run_bot/main-colab.ipynb

###Step 1: Install and update necessary package
```sh
!apt-get update # Update package lists
!apt-get install -y wget unzip # Install wget and unzi
```
###Step 2: Install Google Chrome
```sh
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb # Download the Chrome .deb package
!dpkg -i google-chrome-stable_current_amd64.deb # Install the Chrome .deb package
!apt-get -f install -y # Fix any dependency issue
```

###Step 3: Install Chromedriver
```sh
!wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip # Download the Chromedriver zip
!unzip chromedriver_linux64.zip # Unzip the Chromedriver
!chmod +x chromedriver # Make Chromedriver executable
!mv -f chromedriver /usr/local/bin/chromedriver # Move Chromedriver to /usr/local/bin
```

###Step 4: Install Selenium and webdriver-manager
```sh
!pip install selenium webdriver-manager # Install Selenium and webdriver-manager
```
