class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def Name(self):
        print("What is your name?")
        self.owner = input()
    def deposit(self):
        d = input()
        self.balance = self.balance + int(d)
    def withdraw(self):
        w = input()
        w = int(w)
        if self.balance < w:
            print("You don't have enough money on your bank account")
        else:
            self.balance = self.balance - w
    def bal(self):
        print(self.balance)
Pablo = Account("Pavel")
Pablo.deposit()
Pablo.bal()
Pablo.withdraw()
Pablo.bal()