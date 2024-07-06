import requests

# URL ของ Web App ที่คุณสร้างขึ้น
url = 'https://script.google.com/macros/s/AKfycbzgQ6SmGCYyuX_elxSP1IETzfCjhQ-zVFpl7nNcZXr2J7V_Ws52n6i2CjKWxncQ0QDV/exec'

# ส่ง GET request เพื่อดึงข้อมูล
response = requests.get(url)

# ตรวจสอบสถานะของ response
if response.status_code == 200:
    data = response.json()

    try:
        # ดึงข้อมูลจาก JSON และแยกออกเป็นรายการแต่ละชนิดของคุกกี้
        b_id = [item['b_id'] for item in data['data']]
        c_user = [item['c_user'] for item in data['data']]
        xs = [item['xs'] for item in data['data']]
        datr = [item['datr'] for item in data['data']]
        fr = [item['fr'] for item in data['data']]

        # รวมข้อมูลเป็นรายการของคุกกี้
        cookies = {
            'b_id': b_id,
            'c_user': c_user,
            'xs': xs,
            'datr': datr,
            'fr': fr
        }

        # แสดงผลข้อมูล
        for cookie_type, values in cookies.items():
            print(f'{cookie_type}: {values}')

    except KeyError as e:
        print(f'เกิดข้อผิดพลาดในการดึงข้อมูล: {e}')

else:
    print('เกิดข้อผิดพลาดในการเรียกใช้ API:', response.status_code)
