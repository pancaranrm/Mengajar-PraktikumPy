# from typing_extensions import Self

class Person:
    def __init__(self,name):
        self.name = name
        
    def say_hi(self):
        print(f"say hi {self.name}")
        
p = Person("Pancaran")
p.say_hi()



