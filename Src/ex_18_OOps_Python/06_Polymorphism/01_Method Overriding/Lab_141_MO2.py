class TesSuit:
    def info(self):
        print("Test suit information")

class BaseTest(TesSuit):
    def setup(self):
        print("base setup")

    def run(self):
        print("base test execution")

class LoginTest(BaseTest):
    def run(self):    #Overriding
        print("Login test execution")

class APITest(BaseTest):
    def run(self):  #Overriding
        print("API test execution")




#t= LoginTest()
#t=APITest()
t= BaseTest()
t.run()


