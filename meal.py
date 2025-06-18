def main():
    meal_time=input("What time is it? ")
    time=convert(meal_time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours,minutes = time.split(":")       #get hour and minute
    new_minute =float(minutes) / 60        # convert time into float number
    return float(hours) + new_minute    # return the result to mian function

if __name__=="__main__":
    main()
