class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          
        self._balance = balance     

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{amount} so'm qo'shildi.")
        else:
            print("Noto‘g‘ri summa!")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{amount} so'm yechildi.")
        else:
            print("Balans yetarli emas!")

    def get_balance(self):
        return self._balance


account = BankAccount("Ali", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

print("Balans:", account.get_balance())
