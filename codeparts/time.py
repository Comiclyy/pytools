import random
import string
import colorama
from colorama import Fore, Style
import time
import datetime
import threading

def gettime():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p") # Format the datetime object to show time in 12-hour format
    print(current_time)
    time.sleep(1)

gettime()

if __name__ == "__main__":
    num_threads = 1
    threads = []
    
    while True:
        for i in range(num_threads):
            t = threading.Thread(target=gettime)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()