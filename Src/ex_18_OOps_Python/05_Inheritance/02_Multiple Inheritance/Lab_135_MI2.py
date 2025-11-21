class Father1:

    def money(self):
        print("F1 Money")

class Father2:
    def money(self):
        print("F2 Money")

class child(Father2, Father1):
    def give_money(self):
        self.money()
        print("Son")
C1=child()
C1.give_money()


