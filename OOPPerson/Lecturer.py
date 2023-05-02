from OOP_Person.Person import Person


class Lecturer(Person):

    def __init__(self, name, age, salary, courses):
        super().__init__(name, age)
        self.salary = 0
        self.courses = courses

    def salaryCalc(self, finalSalary, tax):
        finalSalary *= (100 - tax) / 100
        return finalSalary

    def getCourses(self):
        for course in self.courses:
            print(course)
