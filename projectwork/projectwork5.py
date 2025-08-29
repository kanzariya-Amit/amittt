# Main Class

class employee():
    def __init__(self,id,name,age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        
         
    def getinfo(self):
        print(f"id: {self.id} | name: {self.name} | age: {self.age} | salary: {self.salary}")

# Manager Class

class manager(employee):
    def __init__(self, id, name, age, salary, department):
        super().__init__(id, name, age, salary)
        self.department = department
        
        
    def getinfo(self):
        print(f"id: {self.id} | name: {self.name} | age: {self.age} | salary: {self.salary} | department: {self.department}")
        
# developer Class
        
class developer(employee):
    def __init__(self, id, name, age, salary,pgl):
        super().__init__(id, name, age, salary)
        self.pgl = pgl
    
    
    def getinfo(self):
        print(f"id: {self.id} | name: {self.name} | age: {self.age} | salary: {self.salary} | pgl: {self.pgl}")
     
        
# Lists (EmployeeData , ManagerData , DeveloperData) 

EmployeeData = []   
ManagerData = []  
DeveloperData = [] 
           
    
print("\n---python oop project: employee management system---")

# Maun loop:

while True:
    print("\nchoose in operation")
    print("1. creat a employee")
    print("2. creat in manager")
    print("3. creat a developer")
    print("4. show detail")
    print("5. compare salaries")
    print("0. exit\n")
    
    choice=int(input("please enter your choice: "))
    
    # Employee Details:       
    if choice == 1:
        name = input("\nenter your name: ")
        age = int(input("enter your age: "))
        id = input("enter your id: ")
        salary = int(input("enter yout salary: "))
         
        obj = employee(id,name,age,salary)
        
        EmployeeData.append(obj)
        
    # Manager Details:       
    elif choice ==2:
        name = input("\nenter your name: ")
        age = int(input("enter your age: "))
        id = input("enter your id: ")
        salary = int(input("enter yout salary: "))
        department =input("enter your department: ")
        
        obj2 =manager(id,name,age,salary,department)
        
        ManagerData.append(obj2)
        
    # Developer Details:       
    elif choice ==3:
        name = input("\nenter your name: ")
        age = int(input("enter your age: "))
        id = input("enter your id: ")
        salary = int(input("enter yout salary: "))
        pgl =input("enter your programming language: ")
        
        obj3 = developer(id,name,age,salary,pgl)
        
        DeveloperData.append(obj3)
        
    # Saw Details:    
    elif choice ==4:
        print("\nchoose detail to saw: ")
        
        print("1. Employee")
        print("2. Manager")
        print("3. Developer")
        
        choice=int(input("\nplease enter your choice: "))
        
        if choice==1:
            for amii in EmployeeData:
                amii.getinfo()
                
        elif choice==2:
            for amii in ManagerData:
                amii.getinfo()
        
        elif choice==3:
            for amii in DeveloperData:
                amii.getinfo()
    
    # Salary Compair:
    elif choice ==5:   
        firstId = input("enter your first person ID: ")
        secondId = input("enter your second person ID: ")
        
        firstperson = None      
        secondperson = None      
        
        for obj in EmployeeData+ManagerData+DeveloperData:
            if obj.id == firstId:
                firstperson = obj
            if obj.id == secondId:
                secondperson = obj
        
        if firstperson.salary > secondperson.salary:
            print(f"{firstperson.name} {firstperson.id} has a higher salary then {secondperson.name} {secondperson.id}")
        elif secondperson.salary > firstperson.salary:
            print(f"{secondperson.name} {secondperson.id} has a higher salary then {firstperson.name} {firstperson.id}")
        elif firstperson.salary == secondperson.salary:
            print("Both have the same salary.")
        else:
            print("ID not found!")

     # Code Exit:   
    elif choice == 6:
        print("exiting system. all resources have been freed.")
        print("goodbye!")
        break
    
    # Invalid Choise    
    else:
        print("invalid choice")