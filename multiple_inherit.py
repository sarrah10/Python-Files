class Mother:
    mothername = ""
    def  mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class Child(Mother,Father):
    def parents(self):
        print("Mother name: ", self.mothername)
        print("Father name: ", self.fathername)

obj = Child()
obj.mothername = "Arwa"
obj.fathername = "Murtaza"
obj.parents()

