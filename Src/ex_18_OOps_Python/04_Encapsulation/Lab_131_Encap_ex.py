class Bank:
    def __init__(self,account_number,balance):
        self.balance=balance #public
        self.__account_number=account_number #private

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def show_me_account_number(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("Not allowed!")

icici= Bank(9876543210,1000)
icici.deposit(100)
icici.check_balance()
#print(icici.__account_number)
#if you are cashier you can see the account number because of encapsulation
icici.show_me_account_number(True)
