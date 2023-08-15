x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

Physics = int(input("Enter your physics marks: ")) 
Chemistry = int(input("Enter your chemistry marks: ")) 
Biology = int(input("Enter your biology marks: ")) 
Mathematics = int(input("Enter your mathematics marks: ")) 
Computer = int(input("Enter your computer marks: ")) 
total = (Physics + Chemistry + Biology + Mathematics + Computer)/5 
if(total>=90):
    print("YOUR GRADE IS GRADE A")
elif(total>=80):
    print("YOUR GRADE IS GRADE B")
elif(total>=70):
    print("YOUR GRADE IS GRADE C")
elif(total>=60):
    print("YOUR GRADE IS GRADE D")
elif(total>=40):
    print("YOUR GRADE IS GRADE E")
elif(total<40):
    print("YOUR GRADE ISGRADE F")
else:
    print("FAIL")