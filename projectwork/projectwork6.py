filename = "journal.txt"

class adddata:
    def __init__(self,info):
        self.info = info
        
    def addinfo(self):
        AddInfo = open("journal.txt", "a")
        AddInfo.write("\n-------------------\n")
        AddInfo.write(self.info)
        AddInfo.close()
    
    def sawinfo(self):
        SawInfo = open("journal.txt", "r")
        print("\n----- All Data -----\n")
        print(SawInfo.read())
        SawInfo.close()
        
        
while True:
    print("\nplease select in options : ")
    print("1. Add a New Entry")
    print("2. View All Enties")
    print("3. search for an Entry")
    print("4. Delete All Entries")
    print("0. Exit")
    
    choice = int(input("\nEnter Your choice : "))
    
    if choice == 1:
        print("\nWrite info. to journal\n")
        Information = input()
        object = adddata(Information)
        object.addinfo()
        print("Information Added Successfully!\n")
    
    
    elif choice == 2:
        object1 = adddata(None)
        object1.sawinfo()
        
    elif choice == 3:
        keyword = input("Enter keyword to read info. : ")
        with open("journal.txt","r") as filename:
            for linenum,line in enumerate(filename):
                if keyword in line:
                    print(linenum , "-->", line)
    
    elif choice == 4:
        confirm = input("are you sure to delete all info (yes/no): ")
        if confirm.lower() == "yes":
            filename = open("journal.txt", "w")
            print("Information data Successfully!")
            filename.close()
        else:
            print("delete info canceled")

    elif  choice == 0:
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choise")