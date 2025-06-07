name=input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")




#old method
'''  
if name=="Harry" or name=="Hermione" or name=="Ron":
    print("Gryffindor")
elif name=="Draco":
    print("slyntherin")
else:
    print("Who?")
    '''