# class dogs(object):
#     def __init__(self):
#         print('You have created a dog!')
#     def speak(self):
#         pass

# tim = dogs()

# fred = dogs()


# class dogs(object):
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print('Hi! I am', self.name)

#     def changename(self,name):
#         self.name=name

#     def talk(self):
#         print('bark')
        
# class cats(dogs):
#     def __init__(self, name):
#         super().__init__(name)

#     def talk(self):
#         print('meow')

# cat=cats(input())
# cat.changename(input())
# cat.speak()
# cat.talk()

# tim = dogs('tim')
# fred = dogs('fred')   
# tim.changename('fred')
# tim.speak()
# fred.speak()
# numbers = eval(input())




class car(object):
    def __init__(self, name=None, model=None, year=None, price=None):
        self.name = name
        self.model = model
        self.year = year
        self.price = price

    def inform(self):
        print(f'car name: {self.name}', f'car model: {self.model}', f'car year: {self.year}', f'car price" {self.price}','', sep='\n')

    
class vehicle(car):
    def __init__(self, name=None, model=None, year=None, price=None, speed=None):
        super().__init__(name, model, year, price)
        self.speed=speed

if __name__ == "__main__":
    carset = vehicle('BMW', 'M5 COMPETITION', 2025, 222000)
    carset.inform()