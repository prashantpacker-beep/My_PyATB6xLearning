
class Car:
    name=None
    make=None
    model=None

    def __init__(self, o_name, o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with name" + self.name)
        print("Starting a car with Make: " + self.make)
        print("Starting a car with Model: " + self.model)

lambo=Car("lambo","V6","2023")
lambo.start_engine()

mg_hector=Car("mg_hector","V6","2023")
mg_hector.start_engine()
