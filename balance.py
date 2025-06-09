class Account:
    def __init__(self):
        self._balance = 0  # Use a private variable to avoid recursion

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()

    












'''
balance=0

def  main():
    print("Balance:",balance)
    deposit(100)
    withdrawal(50)
    print("Balance:",balance)

def deposit(n):
    global balance
    balance += n

def withdrawal(n):
    global balance
    balance -= n

if __name__=="__main__":
    main()
'''