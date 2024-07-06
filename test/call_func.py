import requests
import json

# URL ของ Web App ที่คุณสร้างขึ้น
url = 'https://script.google.com/macros/s/AKfycbzgQ6SmGCYyuX_elxSP1IETzfCjhQ-zVFpl7nNcZXr2J7V_Ws52n6i2CjKWxncQ0QDV/exec'

# ส่ง GET request เพื่อดึงข้อมูล
response = requests.get(url)

# ตรวจสอบสถานะของ response
if response.status_code == 200:
    data = response.json()

    print(json.dumps(data, indent=2))

else:
    print('เกิดข้อผิดพลาดในการเรียกใช้ API:', response.status_code)
