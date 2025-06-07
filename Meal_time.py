def main():
    meal_time=input("What time is it? ")
    time_float=convert(meal_time)

    if time_float>=7.0 and time_float <= 8.0:
        print("breakfast time")
    elif time_float>=12.0 and time_float <= 13.0:
        print("lunch time")
    elif time_float>=18.0  and time_float <= 19.0:
        print("dinner time")

def convert(time):
    hours,minutes=time.strip().split(":")
    return int(hours)+int(minutes)/60

main()