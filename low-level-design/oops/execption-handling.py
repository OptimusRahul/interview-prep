num1 = 10
num2 = 0

# raise Exception("This is a test exception")

try:
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print(result)
finally:
    print("Finally block executed")

print("Program continues...")


class Main:
    @staticmethod
    def checkAge(age: int):
        if age < 18:
            raise Exception("Not eligible to vote")
        else:
            print("Eligible to vote")

    @staticmethod
    def divide():
        result = 10 / 0

    @staticmethod
    def main():
        # Main.checkAge(15)

        try:
            Main.divide()
        except ArithmeticError as e:
            print("Error: 🔥 " + str(e))

if __name__ == "__main__":
    # try:
    Main.main()
    # except Exception as e:
        # print("Error: " + str(e))

class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message

if __name__ == "__main__":
    try:
        raise CustomException("This is a custom exception")
    except CustomException as e:
        print("Error: 🔥 " + str(e))