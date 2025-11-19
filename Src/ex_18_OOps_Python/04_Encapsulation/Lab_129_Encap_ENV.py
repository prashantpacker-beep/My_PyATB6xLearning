from dotenv import load_dotenv
import os
load_dotenv()
class VWOLoginPage:
    def __init__(self,email_args,password_args):
        self.email=email_args
        self.password=password_args

    def login_confirmation(self):
        if self.email == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD"):
            print("Allowed to login")
        else:
            print("Login failed")

email=input("Enter your VWO email: ").strip()
password=input("Enter your VWO password: ").strip()

vwo_object_ref=VWOLoginPage(email,password)
vwo_object_ref.login_confirmation()