import time
import random

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
        print("Opening Notify")
    elif random_event == "open_chat":
        print("Opening Chat")
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
        print("----- 30 sec -----")
        event_random()
        time.sleep(30)
        break_time()

if __name__ == "__main__":
    main()
