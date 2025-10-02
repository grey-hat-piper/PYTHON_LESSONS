#Assignment 1


#Superhero Class
class Hero:
    def __init__(self,name,age,ability,rescue):
        self.name = name
        self.age = age
        self.ability = ability
        self._rescue = rescue #Encapsulation

    def about(self):
        print(f"{self.name} is {self.age} and has {self.ability}")

#Assigning hero object
Hero_1 = Hero("Batman", 34, "intelligence and street fighting abilities","Numerous rescue")
Hero_1.about()
#Exploring encapsulation
print(Hero_1._rescue)

#Villain class inherit Hero class
class Villain (Hero):
    #Exploring Polymorphism
    def crimes(self):
        print("Numerous crimes")

#Assigning villain object
Villain_1 = Villain("Jocker", 30, "mastermind criminal abilities","No rescue")
Villain_1.about()
Villain_1.crimes()


#Assignment 2 --Polymorphism

#General class
class Vehicle:
    def move(self):
        return print('movement')

#Sub-class
class Car(Vehicle):
    def move():
        return print('Driving')
    
#Car movement
Car.move()

#Sub-class
class Plane(Vehicle):
    def move():
        return print('Flying')
    
#Plane movement
Plane.move()
