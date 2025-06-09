import re

email=input("What is your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
   



#[]set os characters
#[^]complementing the set
# + means 1 or more repetation
#\w any word character