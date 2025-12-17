#Multi inheretance 


class Animal():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"This {self.name} animal is Eating")
    def sleep(self):
        print(f"This {self.name} animal is Sleeping")


class Prey(Animal):
    def flee(self):
        print(f"This {self.name} animal is flee")
class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} animal is Hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("kuneho")
hawk = Hawk("Agila")
fish = Fish("Isda")

rabbit.flee()
hawk.hunt()
fish.hunt()

rabbit.sleep()