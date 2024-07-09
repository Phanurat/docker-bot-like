import sqlite3
import os

# เส้นทางไปยังไฟล์ Cookies ของ Chrome
cookie_file_path = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Profile 2\Network\Cookies')

try:
    # เชื่อมต่อกับฐานข้อมูล Cookies
    conn = sqlite3.connect(cookie_file_path)
    cursor = conn.cursor()

    # ดึงข้อมูล Cookies ของ Facebook
    cursor.execute("SELECT name, value FROM cookies WHERE host_key LIKE '%facebook.com%'")
    cookies = cursor.fetchall()

    # ปิดการเชื่อมต่อ
    conn.close()

    # สร้าง dictionary สำหรับเก็บ cookies
    facebook_cookies = {name: value for name, value in cookies}

    # แสดงผล Cookies ที่ต้องการ
    print(facebook_cookies)

    # หากต้องการคัดลอก Cookies ที่เฉพาะเจาะจง
    c_user = facebook_cookies.get('c_user', 'ไม่พบค่า c_user')
    xs = facebook_cookies.get('xs', 'ไม่พบค่า xs')
    datr = facebook_cookies.get('datr', 'ไม่พบค่า datr')
    fr = facebook_cookies.get('fr', 'ไม่พบค่า fr')

    print(f"c_user: {c_user}")
    print(f"xs: {xs}")
    print(f"datr: {datr}")
    print(f"fr: {fr}")

except sqlite3.OperationalError as e:
    print(f"เกิดข้อผิดพลาดในการเชื่อมต่อกับฐานข้อมูล: {e}")
except PermissionError as e:
    print(f"PermissionError: {e}")
    print("กรุณาตรวจสอบสิทธิ์การเข้าถึงไฟล์ Cookies")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")
