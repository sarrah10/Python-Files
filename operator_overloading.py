#addition overloading
class add:
    def __init__(self,x):
        self.x=x
    def __add__(self,temp):
        return self.x + temp.x
o1 = add(3)
o2 = add(4)
print(o1 + o2)

#multiplication overloading
class mul:
    def __init__(self,x):
        self.x=x
    def __mul__(self,temp):
        return self.x * temp.x
o1 = mul(3)
o2 = mul(4)
print(o1 * o2)

#less among two numbers
class check:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        if(self.x < other.x):
            return "o1 is less than o2"
        else:
            return "o2 is less than o1"
o1 = check(20)
o2 = check(3)
print(o1<o2)

        