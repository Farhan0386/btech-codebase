class Student:
    _count = 0
    def __init__(self, roll_no, marks, grade):
        self.__roll_no=roll_no      
        self._grade=grade           
        self._marks=[]              
        self.gpa=marks              
        Student._count+=1

    @property
    def gpa(self):
        return sum(self._marks)/len(self._marks)/10

    @gpa.setter
    def gpa(self, marks):
        for i in marks:
            if 100<i<0:
                print("Marks must be between 0 and 100")
            else:
                self._marks=marks

    @classmethod
    def count(cls):
        return cls._count

s1=Student(2501730002, [80, 90, 85, 95, 88], "A")
s2=Student(2501730004, [70, 75, 80, 85, 78], "B")
print("-------------Student Records-------------")
print("Roll No:", s1._Student__roll_no)
print("GPA:", s1.gpa)
print("Total Students:", Student.count())