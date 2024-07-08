import requests
import json

# กำหนด b_id ที่ต้องการค้นหา        
target_b_id = 'b00001'

# URL ของ Web App ที่คุณสร้างขึ้น
url = 'https://script.google.com/macros/s/AKfycbxYQWVejdmhc3P99N0-qSgHDfcLX3PI1sQFJd2txN-eV0rKg0NqzF7tPBYjk1sGeAOz/exec'

# ส่ง GET request เพื่อดึงข้อมูล
response = requests.get(url)

# ตรวจสอบสถานะของ response
if response.status_code == 200:
    data = response.json()
    try:
        selected_data = []

        # วนลูปเพื่อค้นหาข้อมูลที่มี b_id เท่ากับ target_b_id
        for item in data['data']:
            if item['b_id'] == target_b_id:
                selected_data.append({
                    'b_id': item['b_id'],
                    'c_user': item['c_user'],
                    'xs': item['xs'],
                    'datr': item['datr'],
                    'fr': item['fr']
                })

        # แปลงข้อมูลเป็น JSON string และพิมพ์ออกมา
        selected_data_json = json.dumps(selected_data, indent=2)
        print(selected_data_json)

    except KeyError as e:
        print(f'เกิดข้อผิดพลาดในการดึงข้อมูล: {e}')

else:
    print('เกิดข้อผิดพลาดในการเรียกใช้ API:', response.status_code)
#Test data dic
print(item['c_user'])
print(item['xs'])
print(item['datr'])
print(item['fr'])
