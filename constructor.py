class construct:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        self.answer = self.num1 + self.num2
        print("Addition of two numbers: "+str(self.answer))

obj = construct(100,200)
obj.addition()

# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj