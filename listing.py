#adding input at the end of the list
queue = ['John', 'Amy', 'Bob', 'Adam']
add = input()
queue.append(add)
print(queue)

#split() turns a string with a certain separator into a list.
str = "some text goes here"
x = str.split(' ')
print(x)

#replace # with space 
msg = input()
msg=msg.replace("#"," ")
print(msg)

#highest value returned in this is 0
def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)


def func(x):
  res = 0
  for i in range(x):
     res += i
  return res
print(func(3))