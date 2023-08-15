year=int(input("Enter year to check leap or not: ")) 
if(year%4==0 and year%100!=0):
    print(year,"is leap year.") 
elif(year%100==0):
    print(year, "is leap year.") 
elif(year%400==0):
    print(year, "is leap year.") 
else:
    print(year, "is not leap year.")

num=int(input("Enter a number: ")) 
for i in range(1,num+1):
    if(i%3==0 and i%5==0): 
        print("FizzBuzz")
    elif(i%3==0): 
        print("Fizz")
    elif(i%5==0): 
        print("Buzz")
    else:
        print(i)
