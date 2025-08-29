array = []

filter_List =[]

print("\nwelcome to the data analyzer and transformer program")

while True:
    
    print("main manu:")
    print("1. input data")
    print("2. display data summary")
    print("3. calculate factorial")
    print("4. sort data")
    print("5. display dataset statistics")
    print("7. exit program")
    
    
    num=int(input("please enter your choice:"))
    
    
    
    if num == 1:
       value =int(input("how many number you want to add:"))
       for number in range(value):
           number = int(input("enter the number:"))
           array.append(number)
        
        
        
        
    elif num == 2:
        print("Data summery")
        print("- Total elemets : ", len(array))
        print("- Max value : ", max(array))
        print("- Min value : ", min(array))
        print("- Sum value:", sum(array))
        print("- Avg vaue : ", sum(array) / len(array))
        
        
        
    elif num == 3:
        def fact(a):
            if a <0:
                return"negative numbers"
            if a <=1:
                return 1 
            return a * fact (a - 1)
        number= int(input("\nenter a number to calculate its factorial :"))  
        print(f"\nfactorial of {number} is : {fact(number)}")
    
    
    
    elif num ==4:
        if len(array)<=0:
           print("List is empty.")

        else:
          value = int(input("Enter a threshold value to filter out data above this value : "))

          for i in array:
             if i>=value:
                filter_List.append(i)

        print(f"Filtered Data (valuess >= {value}): {filter_List}")
    
    
        
    elif  num== 5:
        def sort_data():
            array.sort()
            print ("sorted data in ascending order:")
            for value in array:
                print(value,end=".")
            print()
        
        sort_data()  
                              
         
                
    elif num ==6:
        print("- Max value : ", max(array))
        print("- Min value : ", min(array))
        print("- Sum value:", sum(array))
        print("- Avg vaue : ", sum(array) / len(array))
        
                         
                       
    elif num ==7:
        print("\nthankyou for using the data anayzer and transformer program. goodbye!")
        break
    
    else:
        print("\nInvalid num :")                                                     
        
        
        
                 
        
        