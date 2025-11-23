# BaseTest class (Parent)
def teardown():
    print("Closing browser")


class BaseTest:
    def __init__(self):
        # Protected variable
        self._driver = "Chrome"

    def setup(self):
        print(f"Launching browser: {self._driver}")


# LoginTest class (Child)
class LoginTest(BaseTest):
    def __init__(self, username, password):
        super().__init__()   # Initialize BaseTest
        # Private variables (encapsulation)
        self.__username = username
        self.__password = password

    # Encapsulation: expose username via a getter
    def get_user(self):
        return self.__username

    def run_test(self):
        print(f"Running login test with user: {self.get_user()}")


# Execution
if __name__ == "__main__":
    test = LoginTest("admin", "password123")
    test.setup()
    test.run_test()
    teardown()

"""
- Inheritance → LoginTest inherits BaseTest.
- Encapsulation → Credentials stored as private (__username, __password) and accessed only via get_user().
- Protected variable → _driver in BaseTest is accessible to child classes but not meant for external use.
- Polymorphism-ready design → You could later extend BaseTest for other test types (e.g., SignupTest, PaymentTest).
"""