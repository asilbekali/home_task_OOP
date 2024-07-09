# Task: Employe

import time

class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_id(self) -> int:
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_annual_salary(self) -> int:
        return self.salary * 12

    def raise_salary(self, percent: int):
        self.salary += self.salary * percent // 100
        return self.salary

    def to_string(self) -> str:
        return f"Employee[id={self.id}, name={self.get_name()}, salary={self.salary}]"

# User input
try:
    id = int(input("Enter employee ID: "))
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    salary = int(input("Enter salary: "))

    employee = Employee(id, first_name, last_name, salary)

    print(employee.to_string())

    while True:
        print("\nChoose an option:")
        print("1. get_id")
        print("2. get_first_name")
        print("3. get_last_name")
        print("4. get_name")
        print("5. get_salary")
        print("6. set_salary")
        print("7. get_annual_salary")
        print("8. raise_salary")
        print("9. to_string")
        print("10. exit")
        choice = int(input("Enter command: "))

        if choice == 1:
            print(employee.get_id())
        elif choice == 2:
            print(employee.get_first_name())
        elif choice == 3:
            print(employee.get_last_name())
        elif choice == 4:
            print(employee.get_name())
        elif choice == 5:
            print(employee.get_salary())
        elif choice == 6:
            new_salary = int(input("Enter new salary: "))
            employee.set_salary(new_salary)
            print("Salary updated.")
        elif choice == 7:
            print(employee.get_annual_salary())
        elif choice == 8:
            percent = int(input("Enter raise percentage: "))
            print(f"New salary: {employee.raise_salary(percent)}")
        elif choice == 9:
            print(employee.to_string())
        elif choice == 10:
            print("Exiting program.")
            break
        else:
            print("Invalid command!")

        time.sleep(1.5)

except ValueError as e:
    print(f"Invalid input: {e}")
