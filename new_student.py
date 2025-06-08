import csv
name=input("What is your name? ")
home=input("Where is youe home?")

with open("new_student.csv","a") as file:
    writer=csv.writer(file)
    writer.writerow([name,home])
