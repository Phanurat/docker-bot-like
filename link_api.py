import requests

# URL ของ API ที่คุณต้องการเรียกใช้
api_url = "https://script.googleusercontent.com/macros/echo?user_content_key=2KUvNPkOCrvvTmnPD-p48Vel15O67fXJWhv4w2TIrEqAdXs9pVNyGIcYb-veFgFkgJgwSUWuO6aQduWdvXXW59SxbbrVo_NCm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnD9UDmum1UFPuRX5-kMXMjHPRFVDdPSh6jQWolqNm-y-hDkc_IF_uzMxupEOtZE3p58EeskxJgHpt1w1opwjDj3NI11xVAmW3Nz9Jw9Md8uu&lib=M4x5e_k9hAl1sBoY5DN00zqaPRHpjJtzs"

def check_and_process(data, key):
    link_found = False
    processed_value = None  # สร้างตัวแปรเพื่อเก็บค่าที่ return จาก process()
    for item in data['data']:
        if key in item and item[key]:
            link_found = True
            print("มี link ในคำสั่ง")
            processed_value = process(item[key])
            break
    if not link_found:
        print("ไม่มี link")
    
    return processed_value  # คืนค่าที่ได้จาก process() กลับไปให้ main program

def process(value):
    print(f"Processing value: {value}")
    test = value
    print("link:", test)
    return test
    # Add your processing logic here

# ส่งคำขอ GET ไปยัง API
response = requests.get(api_url)

# ตรวจสอบสถานะคำขอ
if response.status_code == 200:
    # แปลงข้อมูลที่ได้จาก API ให้เป็น JSON
    data = response.json()
    
    # ตรวจสอบและประมวลผลข้อมูล
    processed_value = check_and_process(data, 'Name')
    
    # ใช้ค่าที่ได้จากการประมวลผลไปทำอย่างอื่น
    if processed_value:
        print("Processed value outside function:", processed_value)
        # ทำอย่างอื่นๆ กับ processed_value ต่อไปตามต้องการ
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
