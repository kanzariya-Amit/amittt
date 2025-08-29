import os

class Filemodule:
    def CreateFile():
        try:
            fileName = input("Enter the file name : ")
            file = open(fileName, "x")
            file.close()
            
        except:
            print("Something went wrong!")

        else:
            print("File Created Successfully!")

    def writeFile():
        try:
            fileName = input("Enter the file name : ")
            info = input("Enter the data to write : ")
            file = open(fileName, "w")
            file.write(info)
            file.close

        except:
            print("Something went wrong!")

        else:
            print("Data Written Successfully!")

    def readFile():
        try:
            filename = input("Enter file name : ")
            if os.path.exists(filename):
                file = open(filename, "r")
                Data = file.read()
                file.close()

                print("File Data : \n", Data, "\n")
            else:
                print("File Not Found!")
        except:
            print("Error Occured!")

    def appendFile():
        try:
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            file = open(filename, "a")
            file.write("\n" + data)
            file.close()

            print("Data appended successfully!\n")
        except:
            print("Something went wrong while appending to the file.")