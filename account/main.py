# Task U2
import time
class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        print(f"\nAccount ID: {self.id}\n")

    def get_name(self):
        print(f"\nAccount Name: {self.name}\n")

    def get_balance(self):
        print(f"\nBalance: {self.balance}\n")

    def credit(self, amount):
        self.balance += amount
        print(f"\nNew Balance: {self.balance}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nNew Balance: {self.balance}")
        else:
            print("\nInsufficient balance!!!")
            print(f"\nCurrent Balance: {self.balance}")

    def transfer(self, amount):
        if self.balance < amount:
            print("\nYour card does not have enough money")
        else:
            self.balance -= amount
            print(f"Amount of money left: {self.balance}")

    def string(self):
        print(f"\nID: {self.id}\nName: {self.name}\nBalance: {self.balance}")


try:
    banc_cart = Account(input("Enter Account id: "), input("Enter name: "), int(input("Enter balance: ")))

    while True:
        user_input = int(input("""\n0: Stop
1: Get ID
2: Get Name
3: Get Balance
4: Credit
5: Debit
6: Transfer
7: To String
Enter the action: """))

        if user_input == 1:
            banc_cart.get_id()
        elif user_input == 2:
            banc_cart.get_name()
        elif user_input == 3:
            banc_cart.get_balance()
        elif user_input == 4:
            amount = int(input("\nEnter amount: "))
            banc_cart.credit(amount)
        elif user_input == 5:
            amount = int(input("\nEnter amount: "))
            banc_cart.debit(amount)
        elif user_input == 6:
            amount = int(input("Enter Account amount: "))
            banc_cart.transfer(amount)
        elif user_input == 7:
            banc_cart.string()
        elif user_input == 0:
            break
        else:
            print("Invalid action. Please try again.")

        time.sleep(2.5)

except ValueError as e:
    print(f"Invalid input: {e}")


