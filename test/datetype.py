import datetime
import time
import random

def break_time(check_days):
    start_time = 10  # 7 hours = 25200 sec
    end_time = 15    # 8.5 hours = 30600 sec
    break_duration = random.randint(start_time, end_time)
    print(f"Time break is {break_duration} sec")
    print("--------------------------------")
    time.sleep(break_duration)

    while True:
        today = datetime.datetime.now()
        day_of_week = today.weekday()
        days = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
        test_day = "อังคาร"
        #print(f"วันนี้เป็นวัน {days[day_of_week]}")
        if check_days == days[day_of_week]:
        #if test_day == days[day_of_week]:
            print("Breaking!!")
            time.sleep(1)
        else:
            print("Start New Days")
            return days[day_of_week]  # Return the new day

def main():
    print("Start Bot Running!!")

    while True:
        # Get current day
        today = datetime.datetime.now()
        day_of_week = today.weekday()
        days = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
        print(f"วันนี้เป็นวัน {days[day_of_week]}")
        check_days = days[day_of_week]

        while True:
            # Check if it's a new day
            if datetime.datetime.now().day != today.day:
                print("เปลี่ยนวันแล้ว!")
                today = datetime.datetime.now()
                day_of_week = today.weekday()
                print(f"วันใหม่เป็น {days[day_of_week]}")
                break

            # Determine work time
            two_hour_time = 10     # 2 hours in seconds
            three_half_hour_time = 15  # 3.5 hours in seconds
            time_work = random.randint(two_hour_time, three_half_hour_time)
            print(f"Time to Work! {time_work} sec.")

            start_time = time.time()
            while time.time() - start_time < time_work:
                print(f"Process Working!!")
                time.sleep(1)  # Simulating work process

            check_days = break_time(check_days)  # Check and handle break time

            # Check if it's a new day again after the break
            if datetime.datetime.now().day != today.day:
                print("เปลี่ยนวันแล้ว!")
                today = datetime.datetime.now()
                day_of_week = today.weekday()
                print(f"วันใหม่เป็น {days[day_of_week]}")
                break

if __name__ == "__main__":
    main()
