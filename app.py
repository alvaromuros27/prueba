class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('hi, I am ' +self.name)
    
john = Person("John")
print(john.name)
john.talk()

bob = Person('bob')
