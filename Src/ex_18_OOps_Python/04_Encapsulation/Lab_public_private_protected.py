class TestExample:

    def __init__(self):
        self.driver= "Chrome"
        self._config="STAGE"
        self.__api__key= "ABC11234"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"APIKey: {self.__api__key}")

    def __private_method1(self):
        pass
    def __private_method2(self):
        pass

    def work(self):
        self.__private_method1()
        self.__private_method2()


obj = TestExample()
obj.show()
obj.work()