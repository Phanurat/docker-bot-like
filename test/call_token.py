import requests

# URL ของ Web App ที่คุณสร้างขึ้น
url = 'https://script.google.com/macros/s/AKfycbwN5yqRe4uWwaEUtZ5emNhp4nr3Cwgh2J-Qn5mSiUDlr1wU3DlegiLfzHL0c0qeyFbN/exec'

# ส่ง GET request เพื่อดึงข้อมูล
response = requests.get(url)

# ตรวจสอบสถานะของ response
if response.status_code == 200:
    data = response.json()

    # ดึงข้อมูลจาก JSON และแยกออกเป็นรายการแต่ละชนิดของคุกกี้
    c_user = [item['c_user'] for item in data['data']]
    xs = [item['xs'] for item in data['data']]
    datr = [item['datr'] for item in data['data']]
    fr = [item['fr'] for item in data['data']]

    # รวมข้อมูลเป็นรายการของคุกกี้
    cookies = {
        'c_user': c_user,
        'xs': xs,
        'datr': datr,
        'fr': fr
    }

else:
    print('เกิดข้อผิดพลาดในการเรียกใช้ API:', response.status_code)

for cookie_type, values in cookies.items():
    print(f'{cookie_type}: {values}')