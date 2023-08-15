list1 = [10, 200, 4, 45, 99]
mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n = len(list1)
for i in range(2, n): 
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
 
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and secondmax != list1[i]:
        secondmax = list1[i]
print("Second highest number is : ",secondmax)


list=[1,2,3,4,5,6,8,9,35,67,34,89,456,78]
size=len(list)
print("Odd index elements are: ") 
for i in range(size):
    if(i%2!=0):
        print(list[i])
