class Person:
   #attribute
    name= None
    id= None
    age = None
    email= None
    height= None
    gender= None
    phone_no= None
    address= None
    #behaviour
    def talk(self):    #self will be first argument in every method
         print("I can Talk")

    def sleep(self,name):     # arg with no return
        print("I am sleeping")
        print("sleep",name)

    def sleep2(self,name):    #arg with return
        print("I am sleeping")
        return None
    def walk(self):
        print("I am walking")

    def walk_return(self):    #No args with return
        print("I am walking")

def outside():
    print("I am outside")

#create an object of class
#Objectref= class name()--->object

prashant= Person()
print(prashant.name) #--Attribute
prashant.talk() #---Behaviour
prashant.sleep("pinki")








