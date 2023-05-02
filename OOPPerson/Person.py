class Person:

    def __init__(self, name='Michael Jackson', age=6):
        self.name = name
        self.age = age

    def getFirstName(self):
        print(self.name[0:6])

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setAge(self, newAge):
        if newAge < 0:
            print('Invalid Age, please Enter new age')
        else:
            self.age = newAge

    def getAge(self):
        return self.age
