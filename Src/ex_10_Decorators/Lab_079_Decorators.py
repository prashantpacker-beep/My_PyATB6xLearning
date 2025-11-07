
def add_security (func):

    def wrapper():
        print("1.Before the function is called")
        print("2.Add helmet, dashcash, gloves.knee guard, license")
        func()
        print("3.After the function is called")
        print("4.secure drive leave all the items")
    return wrapper()








@add_security
def drive_ola_scooter():
    print ("I am driving ola scooter")

@add_security
def drive_zep_scooter():
    print("Driving zep scooter")
