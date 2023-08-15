#public
'''class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def getdata(self):
        print(self.name)
        print(self.id)

obj = employee("Sarah", 13)
obj.getdata()'''

#private
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)

obj1 = Base()
print(obj1.a)
