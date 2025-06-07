def main():
    while True:
        try:
            fraction=input("Fraction: ").strip()
            x,y=fraction.split("/")
            x=int(x)
            y=int(y)

            if y==0 or x>y:
                raise ValueError
            
            percentage=round((x/y)*100)

            if percentage<=1:
                print("E")
            elif percentage>=99:
                print("F")
            else:
                print(percentage,"%",sep="")
            break

        except(ValueError,ZeroDivisionError):
            pass

main()