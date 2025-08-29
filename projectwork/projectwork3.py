amiii= []

print("\nwelcome to the student data organizer!\n")

 # add function
while True:
    print("\nselect an option:")
    print("1. add student")
    print("2. display all students")
    print("3. update student information")
    print("4. delete student")
    print("0. exit\n")
    
    
    num=int(input("enter your choice : "))
    
    
    if num==1:
        id=int(input("\nenter your id : "))
        age=int(input("enter your age : "))
        name=(input("enter your name : " ))
        grade=input(("enter your grade : "))
        dob=(input("enter your birth of date(YYYY-MM-DD : )"))
        subject=input(("enter your subjects : "))
        
        
        student = {
            "id":id,
            "name" : name,
            "age":age,
            "grade":grade,
            "date of birth":dob,
            "subject" :subject   
         }
        amiii.append(student)
    

        print("sucessfully added\n")
        
        
    elif num==2:
        if len(amiii)<=0:
            print("list is empty")
        else:    
            for student in amiii:
                print(f"student id {student["id"]} | name {student["name"]} | age {student["age"]} | grade {student["grade"]} | subject {student ["subject"]} ")
            
            
    elif num ==3:
        id=int(input("enter id to update details: "))
        for student in amiii:
            if student["id"]==id:
                age=int(input("enter your age : "))
                name=(input("enter your name : " ))
                grade=input(("enter your grade : "))
                student["age"] = age
                student["name"] = name
                student["grade"] = grade
                
                print("student update successfully!")
                
                
    elif num == 4:
        id=int(input("enter id to delete details: "))
        for student in amiii:
            if student["id"] ==id:
                amiii.remove(student)
                
                print("delete succesfully !")


    elif num ==0:
        print("good bye !")
        break
    
    else :
        print("invalid choice")
        