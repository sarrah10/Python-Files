import random 
def guess():
    num = random.randint(1, 20) 
    chance = 0
    while (chance != 3):
        num1 = int(input("Guess a number between 1 to 20:")) 
        if (num == num1):
            print("you guess correct num") 
            print(name,"Congratulations! You Win") 
            chance+=1
            break
        elif (num > num1):
            print("you guess smaller number") 
            chance+=1
 
        elif (num < num1):
            print("you guess greater number") 
            chance+=1
    if(chance==3):
        print(name," You Crossed Attempt Limit")

        print("Are you want to continue press yes/no") 
        a=input()
        if(a=='yes'or a=='y' or a=='YES'):
            guess() 
        else:
            print("Thank you for playing") 
name = input("Enter your name: ") 
guess()
