nums = [4, 7, 3, 1]
for x in nums:
    print(x*2)

str = "testing for loops"
count = 0
for x in str:
  if x == 't':
    count += 1
print(count)


nums = [1, 2, 3, 4]
res = 0
for x in nums:
    if x%2==0:
        continue
    else:
        res += x
print(res)