import requests
import random

def get_link_post():
    # URL ของ Google Apps Script API
    api_link_url = "https://script.google.com/macros/s/AKfycbwex5szoBPlP4sW1c3lNLqecfAKwOnm6XnaiJUIaO33MSzhFXDXZTItwKH7cH1vCq3YIw/exec"

    # ส่งคำขอ GET ไปยัง API
    response = requests.get(api_link_url)

    # ตรวจสอบสถานะคำขอ
    if response.status_code == 200:
        # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
        data = response.json()

        # สร้าง list ของ comment
        links = [item['link'] for item in data['data']]

        # สุ่มเลือก comment 1 ตัว
        selected_link = random.choice(links)

        # แสดงผล comment ที่ถูกสุ่มเลือก
        print("Selected Link:", selected_link)

        return selected_link

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# เรียกใช้ฟังก์ชันเพื่อสุ่มเลือก comment และแสดงผล
selected_link = get_link_post()
print("Outside function:", selected_link)
