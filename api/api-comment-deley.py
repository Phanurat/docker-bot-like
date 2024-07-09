import requests
import random
import time

def get_random_comment():
    # URL ของ Google Apps Script API
    api_url = "https://script.google.com/macros/s/AKfycbyaklVb5CTX0yAopqNK_vgJHsgfnZC3LeqzdqqfPx7u-nfS-gTvbdcd22IwvfeRpJm8/exec"

    # ส่งคำขอ GET ไปยัง API
    response = requests.get(api_url)

    # ตรวจสอบสถานะคำขอ
    if response.status_code == 200:
        # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
        data = response.json()

        # สร้าง list ของ comment
        comments = [item['comment'] for item in data['data']]

        # สุ่มเลือก comment 1 ตัว
        selected_comment = random.choice(comments)

        # แสดงผล comment ที่ถูกสุ่มเลือกทีละตัวอักษร
        print("Selected comment:", end="")
        for char in selected_comment:
            print(char, end="", flush=True)
            time.sleep(0.5)
        print()  # สร้างบรรทัดใหม่หลังจากการแสดงผล

        return selected_comment

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# เรียกใช้ฟังก์ชันเพื่อสุ่มเลือก comment และแสดงผล
selected_comment = get_random_comment()
print("Outside function:", selected_comment)
