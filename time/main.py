import time

class Time:
    def __init__(self, hour, minute, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def set_second(self, second):
        self.second = second

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def next_second(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def previous_second(self):
        self.second -= 1
        if self.second == -1:
            self.second = 59
            self.minute -= 1
            if self.minute == -1:
                self.minute = 59
                self.hour -= 1
                if self.hour == -1:
                    self.hour = 23

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

try:
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    second = int(input("Enter second: "))
    time_obj = Time(hour, minute, second)

    while True:
        print("\nCurrent Time:", time_obj)
        user_input = int(input("""\n0: Stop
1: Get Hour
2: Get Minute
3: Get Second
4: Set Time
5: Next Second
6: Previous Second
Enter the action: """))

        if user_input == 1:
            print(f"Hour: {time_obj.get_hour()}")
        elif user_input == 2:
            print(f"Minute: {time_obj.get_minute()}")
        elif user_input == 3:
            print(f"Second: {time_obj.get_second()}")
        elif user_input == 4:
            hour = int(input("Enter new hour: "))
            minute = int(input("Enter new minute: "))
            second = int(input("Enter new second: "))
            time_obj.set_time(hour, minute, second)
        elif user_input == 5:
            time_obj.next_second()
        elif user_input == 6:
            time_obj.previous_second()
        elif user_input == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid action. Please try again.")

        time.sleep(1.5)

except ValueError as e:
    print(f"Invalid input: {e}")
