import threading
import time

counter = 0
counter_lock = threading.Lock()
completion_event = threading.Event()

class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(3):
            time.sleep(2)
            with counter_lock:
                counter += 1
                print(f"Counter đã tăng lên: {counter}")
        completion_event.set()

def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    print("Tất cả các threads đã hoàn thành công việc.")
    completion_event.clear()

if __name__ == "__main__":
    main()
