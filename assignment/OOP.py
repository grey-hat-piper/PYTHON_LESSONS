#Assignment 1


#Superhero Class
class Hero:
    def __init__(self,name,age,ability):
        self.name = name
        self.age = age
        self.ability = ability

    def about(self):
        print(f"{self.name} is {self.age} and has {self.ability}")

#Assigning hero object
Hero_1 = Hero("Batman", 34, "intelligence and street fighting abilities")
Hero_1.about()

#Villain class inherit Hero class
class Villain (Hero):
    #Exploring Polymorphism
    def crimes(self):
        print("Numerous crimes")

#Assigning villain object
Villain_1 = Villain("Jocker", 30, "mastermind criminal abilities")
Villain_1.about()
Villain_1.crimes()