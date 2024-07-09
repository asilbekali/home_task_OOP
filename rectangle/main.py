#Task: U5 rectangle

import time

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_height(self):
        return f"Height is: {self.height}"

    def set_height(self, new_height):
        self.height = new_height

    def get_width(self):
        return f"Width is: {self.width}"

    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return f"Area is: {self.height * self.width}"

    def get_perimeter(self):
        return f"Perimeter is: {2 * (self.height + self.width)}"

    def get_info(self):
        return f"Height: {self.height}\nWidth: {self.width}\nArea: {self.get_area()}\nPerimeter: {self.get_perimeter()}"

try:
    user = Rectangle(int(input("Enter width: ")), int(input("Enter height: ")))

    while True:
        user_input = int(input("""\n1: Get height
2: Set height
3: Get width
4: Set width
5: Get area
6: Get perimeter
7: Get info
8: Exit
Enter command: """))

        def find(data):
            if data == 1:
                print(user.get_height())
            elif data == 2:
                new_height = int(input("Enter new height: "))
                user.set_height(new_height)
                print("Height updated.")
            elif data == 3:
                print(user.get_width())
            elif data == 4:
                new_width = int(input("Enter new width: "))
                user.set_width(new_width)
                print("Width updated.")
            elif data == 5:
                print(user.get_area())
            elif data == 6:
                print(user.get_perimeter())
            elif data == 7:
                print(user.get_info())
            elif data == 8:
                print("Thank you!")
                exit()
            else:
                print("Invalid command!")
            time.sleep(1.5)

        find(user_input)
except ValueError:
    print("Invalid input! Please enter only numbers.")
