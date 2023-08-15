#The function map takes a function and an iterable as arguments(list), and returns a new iterable with the 
# function applied to each argument.
def func(x):
    return x + 5
nums = [10,20,30,40,50]
result = list(map(func,nums))
print(result)

# The function filter filters an iterable by leaving only the items that match a condition
num = [11,22,33,44,55]
res = list(filter(lambda x: x%2==0, num))
print(res)