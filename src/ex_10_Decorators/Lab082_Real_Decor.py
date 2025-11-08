import time
import datetime


def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the log")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S'))
        func()
        end_time = time.time()
        print(datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S'))
        print("Total Time Take by Func -> ", round(end_time - start_time, 2), "seconds")
    return wrapper

@time_decorator
@print_logs
def test_ui_01():
    print("Executing UI Test Case 01")
    print("Executing UI Test Case 02")
    time.sleep(2)

@print_logs
@time_decorator
def test_ui_02():
    print("Executing UI Test Case 03")
    print("Executing UI Test Case 04")
    time.sleep(3)

test_ui_01()
test_ui_02()