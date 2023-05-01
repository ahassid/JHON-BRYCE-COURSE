from _distutils_hack import override

from OOP.Animal import Animal


class Dog(Animal):
    print('Test 2 Start')

    def getSound(self):
        print('Wuf')


dog1 = Dog('JACK', 6)
avgChild2 = dog1.avg([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
print('The avg is ' + str(avgChild2))
dog1.getSound()
