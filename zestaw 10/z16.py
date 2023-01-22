import random

class account():

    def __init__(self):
        self.account_num = self.account_num_gen()
        self.balance = 0.0

    def account_num_gen(self):
        self.account_num = ""
        # first two digits
        self.account_num += str(random.randint(0, 9))
        self.account_num += str(random.randint(0, 9))
        self.account_num += " "

        # 6 sets of 4-digit numbers
        for self.i in range(6):
            self.account_num += str(random.randint(0, 9))
            self.account_num += str(random.randint(0, 9))
            self.account_num += str(random.randint(0, 9))
            self.account_num += str(random.randint(0, 9))
            self.account_num += " "
        # removing last space at the end of account number
        self.account_num = self.account_num.strip()

        return self.account_num


    def deposit(self, ammount):
        self.balance += float(ammount)
        print(f"Your balance is now: {self.balance}")

    def withdrawl(self, ammount):
        ammount = float(ammount)
        if self.balance - ammount >= 0.0:
            self.balance = self.balance - ammount
            print(f"Your balance is now: {self.balance}")
        else:
            print(f"You can not withdrawl that ammount (Your balance is {self.balance})")

        

    def account_details(self):
        print("Account detailes")
        print("================")
        print("Account number:")
        print(self.account_num)
        print("Account balance:")
        print(self.balance)


    
account1 = account()
account1.account_details()
account1.deposit(100.67)
account1.withdrawl(40.67)
account1.withdrawl(440.67)
