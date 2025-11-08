def before_after_ui_test(func):
    def wrapper():
        print("Setting up UI Test Environment")
        func()
        print("Tearing down UI Test Environment")
    return wrapper

@before_after_ui_test
def test_UI():
    print("Executing UI Test Cases")

test_UI()