names=[]

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print("hello",name)







#with open("names.txt","r") as file:
 #   lines=file.readlines()

#for line in lines:
 #   print("hello,",line, end="")


#with open("names.txt","a") as file: this will close the file instead of using file.close()