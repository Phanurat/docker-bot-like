import time
import random

# a day have the time 86,400 sec
day_time = 86400
hour_time = 3600
eigth_hour_time = 28800

def event_random():
    print("Event Random")
    list_event = ["story", "like_post", "like_comment", "notify", "open_chat", "time_line"]
    
    random_event = random.choice(list_event)
    
    if random_event == "story":
        print("Reading Story")
    elif random_event == "like_post":
        print("Like Post Successfully")
    elif random_event == "like_comment":
        print("Like Post and Comment Post Successfully")
    elif random_event == "notify":
        print("Check Notify")
        random_notify = random.randint(0, 1)
        if random_notify == 1:
            print("Open Notify")
        else:
            print("No notify, time scroll")
            exit()
            
    elif random_event == "open_chat":
        print("Check Chat")
        random_chat = random.randint(0, 1)
        if random_chat == 1:
            print("Open Chat")
        else:
            print("No message")
            exit()

    elif random_event == "time_line":
        print("Scroll Time Line")
    
    print("---------------3 sec-----------------")
    time.sleep(3)

def break_time():
    break_duration = random.randint(5, 10)
    print(f"Time break is {break_duration} sec")
    print("--------------------------------")
    time.sleep(break_duration)

def main():
    print("Start Bot Running!!")

    while True:
        print("Loop Run")
        start_time = time.time()

        time_work = random.randint(30, 60)
        print(f"Time to Work! {time_work} sec.")

        while time.time() - start_time < time_work:
            event_random()

        break_time()

if __name__ == "__main__":
    main()
