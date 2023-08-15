#Types of method - instance, class, static
class student:
    university="MU"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def getinfo(self):
        print(self.name)
        print(self.rollno)
        print(self.university)
    @classmethod
    def change_university(cls,uname):
        cls.university=uname
    @staticmethod
    def subject(sub):
        return sub    

s=student("Namita",121)
s.getinfo()
s1=student("Naman",123)
s1.getinfo()
student.change_university("LNCT") #will go to uname and then will change the university in class
s1.getinfo()
s.getinfo()
t=s.subject("maths")
print(t)