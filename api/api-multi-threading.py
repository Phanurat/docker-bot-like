import requests
import threading
import time

def get_link():
    # URL ของ Google Apps Script API
    api_link_url = "https://script.google.com/macros/s/AKfycbyxlbV2VimWwSSBtPiAN0MfV9FDju6cwoOuQ3sM7mvzbnbTtTK7wyFdNPwNRJf1qoc4WQ/exec"

    # ส่งคำขอ GET ไปยัง API
    response = requests.get(api_link_url)

    # ตรวจสอบสถานะคำขอ
    if response.status_code == 200:
        # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
        data = response.json()

        # สร้าง list ของ comment
        links = [item['link'] for item in data['data']]

        print(f"Likes Post => {links}")

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def get_comment():
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

        # แสดงผล comment ที่ถูกสุ่มเลือก
        print("Selected comment:", comments)

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

start_time = time.time()

thread_link = threading.Thread(target=get_link)
thread_comment = threading.Thread(target=get_comment)

thread_link.start()
thread_comment.start()

thread_link.join()
thread_comment.join()

end_time = time.time()

print("Done")

execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")