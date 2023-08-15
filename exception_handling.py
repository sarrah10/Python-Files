a = [1,2,3]
try:
    print(f"Second element is {a[1]}")
    # Throws error since there are only 3 elements in array
    print(f"Fourth element is {a[3]}")
except:
    print("An error occured")

# multiple exception handling
l=[1,2,3,4,5,6,7]
a=int(input("Enter num1: ")) 
b=int(input("Enter num2: ")) 
try:
    div=a/b 
    print(l[10])
    with open("exam.txt","r")as f: 
        print("file found")
except ZeroDivisionError: 
    print("denomiator can't be zero")
except IndexError:
    print("There is no index in list") 
except FileNotFoundError:
    print("There is no file with this name please try another") 
finally:
    print("EXECUTED")
