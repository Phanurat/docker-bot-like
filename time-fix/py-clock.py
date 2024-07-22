import datetime
import time

def is_in_time_range(start_time, end_time, current_time):
    return start_time <= current_time <= end_time

def check_time():
    while True:
        now = datetime.datetime.now()
        print(f"Time is {now.hour:02}:{now.minute:02}:{now.second:02}")

        # กำหนดช่วงเวลา
        morning_start = now.replace(hour=8, minute=0, second=0, microsecond=0)
        morning_end = now.replace(hour=8, minute=30, second=0, microsecond=0)
        noon_start = now.replace(hour=12, minute=0, second=0, microsecond=0)
        noon_end = now.replace(hour=12, minute=30, second=0, microsecond=0)

        if is_in_time_range(morning_start, morning_end, now):
            print("In the time range of 08:00 - 08:30 AM")
            # ทำงานที่ต้องการในช่วงเวลา 08:00 - 08:30 AM

        elif is_in_time_range(noon_start, noon_end, now):
            print("In the time range of 12:00 - 12:30 PM")
            # ทำงานที่ต้องการในช่วงเวลา 12:00 - 12:30 PM

        time.sleep(30)  # ตรวจสอบทุก 30 วินาที

if __name__ == "__main__":
    check_time()
