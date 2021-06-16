from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def num_of_sound(self):
        pass
    def make_sound(self):
        pass

class Cat(Animal):
    def num_of_sound(self):
        return 2
    def make_sound(self):
        return 'meow ' * self.num_of_sound()
    def moew(self):
        return 'Cat said: '

class Dog(Animal):
    def num_of_sound(self):
        return 3
    def make_sound(self):
        return 'Gow '* self.num_of_sound()
    def bark(self):
        return 'Dog said: '

c = Cat()
print(c.make_sound())

d = Dog()
print(d.bark() + d.make_sound())