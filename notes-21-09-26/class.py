# class dogs(object):
#     def __init__(self):
#         print('You have created a dog!')
#     def speak(self):
#         pass

# tim = dogs()

# fred = dogs()


class dogs(object):
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('Hi! I am', self.name)

tim = dogs('tim')
fred = dogs('fred')

tim.speak()
fred.speak()