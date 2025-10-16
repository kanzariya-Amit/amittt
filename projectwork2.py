print("Welcome to the pattern generation and number analyzer!\n")

while True:
    print("\nSelect an option:")
    print("1. Generate a pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter the number of rows for the pattern: "))
        for i in range(1, num + 1):
            print("*" * i)
    
    elif choice == 2:
        s_choice = int(input("Enter the start of the range: "))
        e_choice = int(input("Enter the end of the range: "))
        
        for i in range(s_choice, e_choice):
            if i % 2 == 0:
                print(f"Number {i} is Even.")
            else:
                print(f"Number {i} is Odd.")
        
        total = 0
        for i in range(s_choice, e_choice+1):
            total += i
            
        print(f"The sum of numbers from {s_choice} to {e_choice} is: {total}")
    
    elif choice == 3:
        print("Exiting the program. Goodbye!\n")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
        
        