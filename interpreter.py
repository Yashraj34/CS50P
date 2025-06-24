x,y,z=input("Expression: ").split()

new_x=float(x)
new_z=float(z)

match y:
    case "+":
        print(round(new_x+new_z,1))
    case "-":
        print(round(new_x-new_z,1))
    case "/":
        print(round(new_x/new_z,1))
    case "*":
        print(round(new_x*new_z,1))
    case _:
        print("Not Valid")




