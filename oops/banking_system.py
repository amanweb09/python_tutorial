from random import randint


class Bank_Account:
    def __init__(self) -> None:
        self.account_number = randint(10000000, 99999999)
        self.name = input("What's your name? ")
        self.balance = 0

    def show_balance(self) -> None:
        print(self.balance)

    def deposit(self) -> None:
        amt = int(input("Enter amount -->"))
        self.balance += amt

    def withdraw(self) -> None:
        amt = int(input("Enter amount -->"))

        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt


accounts: list = []

while True:
    print(
        "1. Create an account \n 2. Show balance \n 3. Deposit \n 4. Withdraw \n 5. Exit"
    )

    choice = int(input("Enter choice -> "))

    if choice == 1:
        acc = Bank_Account()
        accounts.append(acc)
        print(acc.account_number)
    if choice == 2:
        acc_no = int(input("Enter acc number = "))
        for acc in accounts:
            if acc.account_number == acc_no:
                acc.show_balance()
    if choice == 3:
        acc_no = int(input("Enter acc number = "))
        for acc in accounts:
            if acc.account_number == acc_no:
                acc.deposit()

    if choice == 4:
        acc_no = int(input("Enter acc number = "))
        for acc in accounts:
            if acc.account_number == acc_no:
                acc.withdraw()
    if choice == 5:
        break
