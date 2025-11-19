class VWOLoginPage:

    def __init__(self,email_args,password_args):
        self.email=email_args
        self.password=password_args

    def login_confirmation(self):
        if self.email =="pramod@gmail.com" and self.password =="Pass123":
            print("Allowed to login")
        else:
            print("Login failed")

email=input("Enter your VWO email: ")
password=input("Enter your VWO password: ")

vwo_object_ref=VWOLoginPage(email,password)
vwo_object_ref.login_confirmation()