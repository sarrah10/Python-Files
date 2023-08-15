#multilevel and hybrid inheritence
class student:
    def __init__(self,name,stream,enroll):
        self.name=name
        self.stream=stream
        self.enroll=enroll
    def getinfo(self):
        print(self.name)
        print(self.stream)
        print(self.enroll)

class MST(student):
    def __init__(self, name, stream, enroll):
        super().__init__(name, stream, enroll)
        
    def set_mstmarks(self,python, java):
        self.python=python
        self.java=java

class EST(student):
    # def __init__(self, name, stream, enroll):
        # super().__init__(name, stream, enroll)
        
    def set_estmarks(self,python1, java1):
        self.python1=python1
        self.java1=java1

class result(MST,EST):
        
    def finalresult(self):
        self.FinalPython = self.python + self.python1
        self.FinalJava = self.java + self.java1
        super().getinfo()
        print(f"Total Python: {self.FinalPython} \nTotal Java : {self.FinalJava}")

    def percentage(self):
        a = self.FinalPython/100*100
        b = self.FinalJava/100*100
        print("Python Percentage: ",a)
        print("Java Percentage: ",b)


r1 = result("sarrah","SACS",1013)
r1.set_mstmarks(23,22)
r1.set_estmarks(62,57)
r1.finalresult()
r1.percentage()

