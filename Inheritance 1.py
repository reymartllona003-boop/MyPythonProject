#Inheretance 

from animal import Animal


class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    pass
        
dog = Dog("Scooby")
cat = Cat("Garfield")

print(dog.name)
dog.eat()
dog.sleep()
dog.speak()
print(cat.name)
cat.eat()
cat.sleep()