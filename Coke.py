def main():
    amount_due=50
    while amount_due>0:
        print("amount_due:",amount_due)
        coin=int(input("Insert Coin:"))
        if (coin==5,10,25):
            amount_due=amount_due-coin
    print("Change Owed",amount_due)


main()