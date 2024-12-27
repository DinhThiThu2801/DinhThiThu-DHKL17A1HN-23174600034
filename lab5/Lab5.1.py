import time

class SimpleTask:
    def run_task(self):
        for i in range(1, 6):
            print('Đã in lần thứ:', i)
            time.sleep(1)  
def main():
    task = SimpleTask()
    task.run_task()

if __name__ == "__main__":
    main()
