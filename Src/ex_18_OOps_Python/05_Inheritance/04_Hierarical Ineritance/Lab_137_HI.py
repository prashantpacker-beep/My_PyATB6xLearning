class BaseTest:

    def setup(self):
        print("Setup from BaseTest")

class LoginTest(BaseTest):

    def run(self):
        print("Running login test")

class SignupTest(BaseTest):
    def run(self):
        print("Running signup test")
login = LoginTest()
login.setup()
login.run()
signup = SignupTest()
signup.setup()
signup.run()