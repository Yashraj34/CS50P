x=int(input("What is x? "))
y=int(input("What is y? "))

print('''Choose operation from these:
        1.addition
        2.subtraction
        3.multiplication
        4.division''')
z="" 

while(True):
    choice=int(input("Pick a number: "))
    if (choice==1):
        z=x+y
        print(Float(z))
        break     
    elif(choice==2):
        z=x-y
        print(float(z))
        break
    elif(choice==3):
        z=x*y
        print(float(z))
        break    
    elif(choice==4):
        z=x/y
        print(float(z))
        break      
    else:
        print("Invalid")



