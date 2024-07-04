# ใช้ภาพพื้นฐานจาก selenium/standalone-chrome
FROM selenium/standalone-chrome:latest

# ติดตั้ง Python 3 และ pip
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip

# ติดตั้ง WebDriver Manager
RUN pip3 install selenium webdriver-manager requests

# คัดลอกไฟล์โค้ดไปยัง container
COPY event-link-post.py /run_bot/os-linux.py

# ตั้งค่า directory ทำงาน
WORKDIR /run_bot

# รันไฟล์โค้ดเมื่อ container เริ่มทำงาน
CMD ["python3", "event-link-post.py"]
