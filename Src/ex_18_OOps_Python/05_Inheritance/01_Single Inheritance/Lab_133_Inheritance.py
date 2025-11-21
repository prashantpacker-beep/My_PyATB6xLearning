#A subclass/child inherits from one parent/base

#Single inheritance

class BaseTest:
    driver= "chrome"
    __driver2= "FF"

    def setup(self):
        print("Base set up with the browser and env " + self.__driver2)

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the testcase " + self.driver)
t= LoginTest()
t.run()
