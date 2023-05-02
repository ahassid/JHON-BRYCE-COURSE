class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def functionDemo(self):
        print('Into Function Demo')

    def avg(self, nums):
        sum = 0
        for num in nums:
            sum += num
        return sum / len(nums)

    def getSound(self):
        pass
