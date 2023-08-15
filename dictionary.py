#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))