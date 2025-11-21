class TestSuit:

    def info(self):
        print("This is GF- step1")

class BaseTest(TestSuit):
    def setup(self):
        print("Basetest-f-step2")

class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("Running test case")
test= UITest()
test.run()
