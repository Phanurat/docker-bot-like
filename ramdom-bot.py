import random
import time

val = int(input("1 login or 0 not login : "))

def event_random():
    list_event = ["story", "like_post", "like_comment", "notify"]
    random_event = random.choice(list_event)
    print("Event Next ==> ", random_event)
    return random_event

def timeline_scroll():
    scroll_random = random.uniform(6, 10)
    print("Scroll ==> ", scroll_random)
    number = 0
    for i in range(1, int(scroll_random)):
        time.sleep(2)
        number += 1
        print(f"Post : {number}")

def login_succ(val):
    if val == 1:
        print("Login Successfully!")

        while True:
            timeline_scroll()
            random_event = event_random()  # เรียกใช้ฟังก์ชัน event_random เพื่อรับค่า random_event
            print("return from function : ", random_event)
    else:
        print("Cannot Login!")

login_succ(val)
