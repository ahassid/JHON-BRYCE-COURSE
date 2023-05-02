from OOP_Person.Person import Person


class Student(Person):

    def __init__(self, name='Marcos Alonso', age=90):
        super().__init__(name, age)
        # self.degree = degree

    def getFirstName(self):
        print(self.name[3:9])

    def avgCalc(self, nums):
        sum = 0
        for num in nums:
            sum += num
        return sum / len(nums)
