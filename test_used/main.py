import datetime
import time
import random

global test_day
test_day = "อังคาร"

def break_time(check_days):
    start_time = 10
    end_time = 15
    break_duration = random.randint(start_time, end_time)
    
    print(f"Time break is {break_duration} sec")
    print("-" * 10)
    time.sleep(break_duration)

    today = datetime.datetime.now()
    day_of_week = today.weekday()
    days = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]

    if test_day == days[day_of_week]:
        print("Breaking!!!")
        time.sleep(1)
    else:
        print("Start New Day, will be working!!")

def main():
    status = int(input("Run Bot automation? 1 (yes) or 0 (no) ==> "))
    
    if status == 1:
        print("Start Bot Running!!")

        while True:
            today = datetime.datetime.now()
            day_of_week = today.weekday()
            days = ["จันทร์", "อังคาร", "พุธ", "พฤหัสบดี", "ศุกร์", "เสาร์", "อาทิตย์"]
            print(f"วันนี้เป็นวัน {days[day_of_week]}")
            check_days = days[day_of_week]

            while True:
                break_time(check_days)
                start_time = 10
                end_time = 15
                time_work = random.randint(start_time, end_time)
                print(f"Time to Work! {time_work} sec")
                set_time = time.time()

                while time.time() - set_time < time_work:
                    print(f"Process Working!!")
                    time.sleep(1)
                
                break_time(check_days)

                # Check if it's a new day
                if datetime.datetime.now().day != today.day:
                    print("Changed day!")
                    today = datetime.datetime.now()
                    day_of_week = today.weekday()
                    print(f"New day is {days[day_of_week]}")
                    break

    else:
        print("Program to Close or Error")

if __name__ == "__main__":
    main()
