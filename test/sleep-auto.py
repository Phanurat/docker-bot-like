import time

def break_automate():
    print("Break time : 5sec")
    time.sleep(5)

def play_automate():
    i = 1
    while True:
        print("Processing :", i)
        i += 1
        if i % 10 == 0:  # หยุดพักทุกๆ 10 ครั้ง
            break_automate()
        time.sleep(1)  # หน่วงเวลา 1 วินาทีระหว่างการแสดงผลแต่ละครั้ง

play_automate()
