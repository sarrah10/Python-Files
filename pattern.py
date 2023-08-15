n=int(input("Enter no of rows: "))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1 or i==j or j==n-i-1):
            print('*',end="")
        else:
            print(" ",end="")
    print()