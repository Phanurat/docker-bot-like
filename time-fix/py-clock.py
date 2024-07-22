import datetime
import time

def is_in_time_range(start_time, end_time, current_time):
    return start_time <= current_time <= end_time

def check_time():
    while True:
        now = datetime.datetime.now()
        print(f"Time is {now.hour:02}:{now.minute:02}:{now.second:02}")

        # ทำงานที่ต้องการในช่วงเวลา 08:00 - 08:30 AM
        morning_start = now.replace(hour=8, minute=0, second=0, microsecond=0)
        morning_end = now.replace(hour=8, minute=30, second=0, microsecond=0)

        # ทำงานที่ต้องการในช่วงเวลา 12:00 - 12:30 AM
        noon_start = now.replace(hour=12, minute=0, second=0, microsecond=0)
        noon_end = now.replace(hour=12, minute=30, second=0, microsecond=0)

        # ทำงานที่ต้องการในช่วงเวลา 17:00 - 17:30 PM
        end_work = now.replace(hour=17, minute=0, second=0, microsecond=0)
        fi_end_work = now.replace(hour=17, minute=30, second=0, microsecond=0)

        # ทำงานที่ต้องการในช่วงเวลา 19:00 - 19:30 PM
        back_work = now.replace(hour=19, minute=0, second=0, microsecond=0)
        fi_back_work = now.replace(hour=19, minute=30, second=0, microsecond=0)

        # ทำงานที่ต้องการในช่วงเวลา 9:40 - 11:50 PM
        time_home = now.replace(hour=9, minute=40, second=0, microsecond=0)
        end_time_home = now.replace(hour=11, minute=50, second=0, microsecond=0)

        # ทำงานที่ต้องการในช่วงเวลา 13:00 - 20:40 PM
        night_time = now.replace(hour=13, minute=00, second=0, microsecond=0)
        end_night = now.replace(hour=20, minute=40, second=0, microsecond=0)

        
        if is_in_time_range(morning_start, morning_end, now):
            print("In the time range of 08:00 - 08:30 AM")
            # ทำงานที่ต้องการในช่วงเวลา 08:00 - 08:30 AM

        elif is_in_time_range(noon_start, noon_end, now):
            print("In the time range of 12:00 - 12:30 PM")
            # ทำงานที่ต้องการในช่วงเวลา 12:00 - 12:30 PM
        
        elif is_in_time_range(end_work, fi_end_work, now):
            print("In the time range of 17:00 - 17:30 AM")
        
        elif is_in_time_range(back_work, fi_back_work, now):
            print("In the time range of 19:00 - 19:30 AM")

        elif is_in_time_range(time_home, end_time_home, now):
            print("In the time range of 09:40 - 11:50 AM")

        elif is_in_time_range(night_time, end_night, now):
            print("In the time range of 13:00 - 20:40 AM")

        time.sleep(30)  # ตรวจสอบทุก 30 วินาที

if __name__ == "__main__":
    check_time()
