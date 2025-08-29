from datetime import datetime as dt
import time as t

class Time:

    def currenttime():
        now = dt.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp)

    def calculatediffer():
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        d1 = dt.strptime(date1,"%Y-%m-%d")
        d2 = dt.strptime(date2,"%Y-%m-%d")
        differ = d2-d1

        print(differ)

    def customdate():
        now = dt.now()

        print("1. YYYY-MM-DD")
        print("2. DD-MM-YYYY")

        print("Select format to print date and time")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            print(timestamp)

        elif choice == 2:
            timestamp2 = now.strftime("%d-%m-%Y %H:%M:%S")
            print(timestamp2)

        else:
            print("Invalid number: ")

    def stopwatch():
        input("Press Enter to start stopwatch...")
        start = t.time()
        input("Press Enter to stop stopwatch...")
        end = t.time()
        print("Elapsed Time:", round(end - start, 2), "seconds")

    def countdown():
        sec = int(input("Enter countdown time (seconds): "))
        while sec:
            mins, secs = divmod(sec, 60)
            print(f"{mins:02}:{secs:02}", end="\r")
            t.sleep(1)
            sec -= 1
        print("Time's up!")