from OOP.Animal import Animal


class Cat(Animal):
    print('Test Start')
    cat1 = Animal()
    cat1.functionDemo()
    avgChild1 = (cat1.avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print('Gal is ' + str(avgChild1) + ' years old')

    def getSound(self):
        print('Meauw')
