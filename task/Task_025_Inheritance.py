class BaseTest:
    _driver = "chrome"

    def setup(self):
        print("Launching Browser" + self._driver)

    def teardown(self):
        print("Closing Browser")

class LoginTest(BaseTest):
    __username = "prashant"
    __password = "Pass143"

    def get_user(self):
        return self.__username

    def run_test(self):
        print("Running login test with user: " + self.__username)

login = LoginTest()
login.setup()
login.run_test()
login.teardown()




