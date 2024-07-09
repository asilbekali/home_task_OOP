# Task: U3 date
import time

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Getters
    def get_days(self):
        return self.day

    def get_months(self):
        return self.month

    def get_years(self):
        return self.year

    # Setters
    def set_day(self, new_day):
        self.day = new_day

    def set_month(self, new_month):
        self.month = new_month

    def set_year(self, new_year):
        self.year = new_year

    def set_date(self, new_day, new_month, new_year):
        self.day = new_day
        self.month = new_month
        self.year = new_year

    def to_string(self):
        return f"\n{self.day:02d}/{self.month:02d}/{self.year}"

try:
    banc_cart = Date(int(input("\nEnter day: ")), int(input("Enter month: ")), int(input("Enter year: ")))

    while True:
        user = int(input("""\n0: Stop
1: Get day
2: Get month
3: Get year
4: Set day
5: Set month
6: Set year
7: Set date
8: To string
Enter your choice: """))
        if user == 0:
            exit()
        elif user == 1:
            print("Day:", banc_cart.get_days())
        elif user == 2:
            print("Month:", banc_cart.get_months())
        elif user == 3:
            print("Year:", banc_cart.get_years())
        elif user == 4:
            new_day = int(input("Enter new day: "))
            banc_cart.set_day(new_day)
        elif user == 5:
            new_month = int(input("Enter new month: "))
            banc_cart.set_month(new_month)
        elif user == 6:
            new_year = int(input("Enter new year: "))
            banc_cart.set_year(new_year)
        elif user == 7:
            new_day = int(input("Enter new day: "))
            new_month = int(input("Enter new month: "))
            new_year = int(input("Enter new year: "))
            if new_day <= 30 and new_month <= 12 and new_year >= 1000:
                banc_cart.set_day(new_day)
                banc_cart.set_month(new_month)
                banc_cart.set_year(new_year)
            else:
                print("Invalid date")
            banc_cart.set_date(new_day, new_month, new_year)
        elif user == 8:
            print("Date:", banc_cart.to_string())

        time.sleep(2)

except ValueError as e:
    print("Invalid input, please enter integers for day, month, and year.")
