import time
def print_logs(func):
    def wrapper():
        print("start of the logs")
        func()
        print("end of the logs")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start time")
        func()
        end_time = time.time()
        print("end time")
        print("Total time taken by function ",end_time - start_time)
    return wrapper()



@print_logs
@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@print_logs
@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)
