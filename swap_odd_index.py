# Write a program to swap odd index elements in list.
list=[45,5,565,13,67,23,6,1,2,3]

size=len(list) 
even=0 
odd=1
 
print("Before Swaping: ") 
print(list)
print("After Swaping: ") 

while(True):

    if(even<size and odd<size):
        temp=list[even] 
        list[even]=list[odd] 
        list[odd]=temp 
        even+=2
        odd+=2 
    else:
        break 
print(list)
