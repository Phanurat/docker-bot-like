import time
import random

def notify():
    print("Read Notify Done")

def like_post():
    list_emoji = ["Like", "Love", "MiniLove", "Haha", "Sad", "Hate"]
    random_emoji = random.choice(list_emoji)
    print("Emoje Post ==> ", random_emoji)
    return random_emoji

def like_comment():
    print("Comment ==> the comment for post to and the comments")
    like_post()

def read_story():
    print("Read Story")
    like_post()

def event_random():
    list_event = ["story", "like_post", "like_comment", "notify"]
    random_event = random.choice(list_event)
    print("Event Next ==> ", random_event)

    if random_event == "story":
        read_story()

    elif random_event == "like_post":
        like_post()

    elif random_event == "like_comment":
        like_comment()

    elif random_event == "notify":
        notify()

    return random_event

def timeline_scroll():
    scroll_random = random.uniform(6, 10)
    print("Scroll ==> ", scroll_random)
    number = 0
    for i in range(1, int(scroll_random)):
        time.sleep(2)
        number += 1
        print(f"Post : {number}")

def break_automate():
    break_time = random.randint(5, 10)
    print("Break time is = ", break_time, "sec")
    time.sleep(break_time)

def play_automate():
    print("Login Successfully!")
    i = 1
    while True:
        print("Processing :", i)
        range_time = random.randint(5, 10)
        print("Range is =", range_time)
        
        for _ in range(range_time):
            timeline_scroll()
            random_event = event_random()  # Call event_random function to get random_event
            print("Return from function : ", random_event)
        
        break_automate()  # Take a break after the loop
        i += 1
        time.sleep(1)  # Wait for 1 second before next iteration

# Run the automation
play_automate()
