'''with open("friends.txt","w") as f:
    f.write("Namit\n")
    f.write("Nisha\n")
    f.write("Amit\n")
#taking 5 names from user and writing in a file    
    for i in range(5):
        name = input(f"Enter your {i} friends name: ")
        f.write(name)
        f.write('\n')'''

programming = ['python','java','cpp','dotnet']
with open("friends.txt","w") as f:
    f.writelines('\n'.join(programming)) #join() join all data of list with \n (python\njava\ncpp\ndotnet)

#append
with open("friends.txt","a") as f:
    f.write("\nHello")