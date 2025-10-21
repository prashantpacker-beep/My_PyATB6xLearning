print("Enter the which Test you want to run")
test_type=input("Enter the test type :API, UI, Performance, Security ")

match test_type:
    case "API":
        print("We are running the postman API Test case")
    case "UI":
        print("We are running the Selenium Test case")
    case "Performance":
        print("We are running the performance Test case")
    case "Security":
        print("We are running the security Test case")
    case _:
        print("Invalid Type")


#test_type=input("Enter the test type : ")
#if test_type == "API":
    #print("We are running the postman API Test case")
#elif test_type == "UI":
    #print("We are running the Selenium Test case")
#elif test_type == "Performance":
    #print("We are running the performance Test case")
#elif test_type == "Security":
    #print("We are running the security Test case")
#else :
    #print("Invalid Type")
