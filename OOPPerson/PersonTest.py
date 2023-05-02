from OOP_Person.Lecturer import Lecturer
from OOP_Person.Student import Student

s1 = Student('Cristiano Ronaldo', 65)
s2 = Student()
l1 = Lecturer('Alexandra Stan', 12, 6000, ['Bio', 'Chimi', 'Phi'])

s1.getFirstName()
s2.getFirstName()
l1.getFirstName()
l1.getCourses()
avg = s1.avgCalc([1,5,9,3,7])
print(avg)
