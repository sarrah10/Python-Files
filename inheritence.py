# A Python program to demonstrate inheritance

class Person(object):

    def __init__(self, name, id):
	    self.name = name
	    self.id = id
	    
    def Display(self):
	    print(self.name, self.id)

emp = Person("Satyam", 102) # An Object of Person
emp.Display()

class Emp(Person):

    def Print(self):
	    print("Emp class called")	
Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()
# Calling child class function
Emp_details.Print()

# Python program to demonstrate
# single inheritance

# Base class
class Parent:
	def func1(self):
		print("This function is in parent class.")

# Derived class


class Child(Parent):
	def func2(self):
		print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()
