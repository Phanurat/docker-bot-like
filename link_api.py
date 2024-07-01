import requests
import os

# URL ของ API ที่คุณต้องการเรียกใช้
api_url = "https://script.googleusercontent.com/macros/echo?user_content_key=2KUvNPkOCrvvTmnPD-p48Vel15O67fXJWhv4w2TIrEqAdXs9pVNyGIcYb-veFgFkgJgwSUWuO6aQduWdvXXW59SxbbrVo_NCm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnD9UDmum1UFPuRX5-kMXMjHPRFVDdPSh6jQWolqNm-y-hDkc_IF_uzMxupEOtZE3p58EeskxJgHpt1w1opwjDj3NI11xVAmW3Nz9Jw9Md8uu&lib=M4x5e_k9hAl1sBoY5DN00zqaPRHpjJtzs"

def check_and_process(data, key):
    for item in data['data']:
        if key in item and item[key] and not item.get('Status') == 'Used':
            print("มี link ในคำสั่ง")
            process(item[key])
            item['Status'] = 'Used'
        else:
            print("ไม่มี link หรือเคยใช้ link แล้ว")

def process(value):
    print(f"Processing value: {value}")
    # Add your processing logic here

# ส่งคำขอ GET ไปยัง API
response = requests.get(api_url)

# ตรวจสอบสถานะคำขอ
if response.status_code == 200:
    # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
    data = response.json()
    
    # ตรวจสอบและประมวลผลข้อมูล
    check_and_process(data, 'Name')
    
    # แสดงผลข้อมูลที่ได้หลังจากปรับปรุงสถานะ
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
