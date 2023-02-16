import time

def timer():
    minutes = int(input("How many minutes do you want the timer to run for? "))
    seconds = minutes * 60
    end_time = time.time() + seconds
    message = input("What message should be displayed after the timer is over? ")
    while time.time() < end_time:
        time_left = int(end_time - time.time())
        print(f"Time left: {time_left // 60:02d}:{time_left % 60:02d}")
        time.sleep(1)
    print(message)

timer()
