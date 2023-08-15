#The raise statement allows the programmer to force a specific exception to occur. 
age = int(input("Enter your age: "))
if(age<18):
    raise Exception("Age should be greater than 18")
else:
    print("You are eligible for voting")