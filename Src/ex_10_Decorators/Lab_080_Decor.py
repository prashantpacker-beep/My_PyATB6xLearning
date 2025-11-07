def before_after_ti_test(func):
    def wrapper():
        print("Before running the UI code")
        func()
        print("After running the UI code")
    return wrapper()








@before_after_ti_test
def test_ui():
    print("Hi, I am Running the UI Test")
