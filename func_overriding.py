class one:
    def show(self):
        print("show from one")
class two():
    def show(self):
        print("show from two")

class three(two,one):  
    def display():
        print("I am of no use")

#MRO (method resolution order) -if same name function is coming from a class then it will call the first one
# (left to right)
obj = three()
obj.show()