from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def laon(self):
        pass

class Prashant(Father):
    def laon(self):
        print("Giving the 50K loan")

prashant=Prashant("Prashant kavinkar")
prashant.laon()