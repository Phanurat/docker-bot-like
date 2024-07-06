import requests

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

        return comments

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# เรียกใช้ฟังก์ชันเพื่อสุ่มเลือก comment และแสดงผล
comments = get_random_comment()

# ลำดับตัวเลข

# ใช้ for loop เพื่อแสดงตัวเลขทีละตัว
for number in comments:
    print(number)
