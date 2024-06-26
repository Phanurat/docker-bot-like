import requests
from datetime import datetime

# รายการคุกกี้ที่คุณให้มา
cookies_list = [
    {
        'name': 'c_user',
        'value': '100020688590532',
        'domain': '.facebook.com',
        'path': '/',
        'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
        'httpOnly': False,
        'secure': True,
        'session': False,
        'sameSite': 'None'
    },
    {
        'name': 'xs',
        'value': '11%3AinhoChAjm4XLPA%3A2%3A1719392933%3A-1%3A11361',
        'domain': '.facebook.com',
        'path': '/',
        'expires': datetime.strptime('2025-05-29T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
        'httpOnly': True,
        'secure': True,
        'session': False,
        'sameSite': 'None'
    },
    {
        'name': 'datr',
        'value': 'eOlPZjhhJxb4hoWIuz9f0v-b',
        'domain': '.facebook.com',
        'path': '/',
        'expires': datetime.strptime('2025-06-28T01:12:26.667Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
        'httpOnly': True,
        'secure': True,
        'session': False,
        'sameSite': 'None'
    },
    {
        'name': 'fr',
        'value': '1YmSZxru2wyb7mCNZ.AWUGodKebFijrAu25EovUc_QsZE.BmesVy..AAA.0.0.Bme9qs.AWVHmaoP3P0',
        'domain': '.facebook.com',
        'path': '/',
        'expires': datetime.strptime('2024-08-27T06:53:31.187Z', '%Y-%m-%dT%H:%M:%S.%fZ').timestamp(),
        'httpOnly': True,
        'secure': True,
        'session': False,
        'sameSite': 'None'
    }
]

# แปลงรายการคุกกี้เป็นรูปแบบที่ไลบรารี requests เข้าใจ
cookies = {cookie['name']: cookie['value'] for cookie in cookies_list}

# URL ของหน้า Facebook ที่ต้องการเข้าถึง
url = 'https://www.facebook.com/'

# ส่งคำขอ HTTP ด้วยคุกกี้
response = requests.get(url, cookies=cookies)

# ตรวจสอบสถานะการตอบกลับ
if response.status_code == 200:
    print('เข้าสู่ระบบสำเร็จ')
    # แสดงเนื้อหาของหน้า
    print(response.text)
else:
    print('การเข้าสู่ระบบล้มเหลว')
    print(f'Status code: {response.status_code}')
