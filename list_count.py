
# Python program to count the number of elements in a list using a dictionary
#Dictionary hold single value as an element

def count(list):
    num = {}  # Creating an empty dictionary
    for items in list:
        num[items] = list.count(items)

    for key,value in num.items():
        print ("% d : % d"%(key, value))
    
# Driver function
if __name__ == "__main__":
    list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    count(list)