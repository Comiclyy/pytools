import threading

def send_message():
    print(f"\033[32mUploading to database 1% complete\033[0m")

    threads = []
    for i in range(100000):
        thread = threading.Thread(target=send_message, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

send_message()