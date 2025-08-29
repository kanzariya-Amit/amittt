import math
import random
from uuid import uuid4
from datetime_ops import Time
from File_ops import Filemodule

class MathModule:

    def factorial():
        num = int(input("Enter a number to calculate factorial: "))
        fact = math.factorial(num)
        print(fact)

    def compound_interest():
        p = float(input("Enter Principal amount: "))
        r = float(input("Enter Rate of Interest (%): "))
        t = float(input("Enter Time (years): "))
        n = int(input("Enter number of times interest compounded per year: "))

        amount = p * (1 + (r/100)/n) ** (n*t)
        ci = amount - p

        print(f"Compound Interest = {ci:.2f}")
        print(f"Total Amount = {amount:.2f}")

    def trigonometry():
        print("\nTrigonometric Operations:")
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. tan(x)")
        choice = int(input("Enter your choice: "))

        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)
        if choice == 1:
            print(f"sin({angle}) = {math.sin(radians):.4f}")
        elif choice == 2:
            print(f"cos({angle}) = {math.cos(radians):.4f}")
        elif choice == 3:
            print(f"tan({angle}) = {math.tan(radians):.4f}")
        else:
            print("Invalid choice!")

    
    def area_shapes():
        print("\nChoose Shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            r = float(input("Enter radius: "))
            print(f"Area of Circle = {math.pi * r * r:.2f}")
        elif choice == 2:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print(f"Area of Rectangle = {l * b:.2f}")
        elif choice == 3:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print(f"Area of Triangle = {0.5 * b * h:.2f}")
        elif choice == 4:
            s = float(input("Enter side: "))
            print(f"Area of Square = {s * s:.2f}")
        else:
            print("Invalid choice!")


class randommodule:
    def randomNumber():
        start = int(input("Enter the start range : "))
        end = int(input("Enter the end range : "))
        print("Random Numbers : ", random.randint(start, end))

    def randomList():
        size = int(input("Enter the size of list : "))
        start = int(input("Enter the start range : "))
        end = int(input("Enter the end range : "))

        listt = []
        for i in range(size):
            num = random.randint(start, end)
            listt.append(num)

        print("random List : ", listt)

    def randomPassword():
        length = int(input("Enter the length of password : "))
        if length <= 0:
            print("Password Length Must be Greater than 0.")
            return
            
        small_letters = 'abcdefghijklmnopqrstuvwxyz'
        capital_latters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        symbols = '!@#$%^&*()-_=+[{]}|;:,.<>?/~`'
        random_Pass = small_letters + capital_latters + digits + symbols

        password = ""
        for i in range(length):
            password += random.choice(random_Pass)

        print("Random Password :", password)

    def randomOtp():
        otp = ""
        for i in range(8):
            otp += str(random.randint(0,9))
        print("Random Otp : ", otp)

class Unique_identifier:
        
    def unique_ID():
        print("\nGenerate Unique Identifier (UUID):")
        unique_id = uuid4()
        print(f"Generated UUID: {unique_id}\n")
     
class ExplorreModule:
    def dir_func():
        print("\n-------------------------------------------")
        print("Explore Module Attributes:")
        module_name = input("Enter module name to explore: ")

        module = __import__(module_name)

        attributes = dir(module)

        print(f"\nAvailable Attributes in {module_name} module:")
        print(attributes)

        print("------------------------------------------\n")


   

print("-------------------------------------------------")
print("Welcome to Multi-Utility Toolkit")
print("------------------------------------------------")
print("Choose an option:")

while True:

    print("\n1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers")
    print("5. File Operations")
    print("6. Explore Module Attributes")
    print("7. Exit")
    print("---------------------------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        while True:
            print("\n1. Display current date and time ")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                Time.currenttime()

            elif choice == 2:
                Time.calculatediffer()

            elif choice == 3:
                Time.customdate()

            elif choice == 4:
                Time.stopwatch()

            elif choice == 5:
                Time.countdown()

            elif choice == 6:
                break

            else:
                print("Invalid choice!")

    elif choice == 2:
        while True:
            print("\n1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                MathModule.factorial()

            elif choice == 2:
                MathModule.compound_interest()

            elif choice == 3:
                MathModule.trigonometry()

            elif choice == 4:
                MathModule.area_shapes()

            elif choice == 5:
                break

            else:
                print("Invalid choice!")

    elif choice == 3:

        while True:
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            print("5. Back to Main Menu")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                randommodule.randomNumber()

            elif choice == 2:
                randommodule.randomList()

            elif choice == 3:
                randommodule.randomPassword()

            elif choice == 4:
                randommodule.randomOtp()

            elif choice == 5:
                break

            else:
                print("Invalid choice")
        
    elif choice == 4:
        Unique_identifier.unique_ID()

    elif choice == 5:
        while True:
            print("\nFile operations:")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. back to Main Menu")

            choice = int(input("Enter your choice: "))

            if  choice == 1:
                Filemodule.CreateFile()

            elif choice == 2:
                Filemodule.writeFile()

            elif choice == 3:
                Filemodule.readFile()

            elif choice == 4:
                Filemodule.appendFile()

            elif choice == 5:
                break

            else:
                print("Invalid Choice!")

    elif choice == 6:
        ExplorreModule.dir_func()

    elif choice == 7:
        print("Thanks for using Multi Utility Toolkit!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")