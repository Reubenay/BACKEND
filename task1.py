class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display(self):
        print (f"i bought this cat named {self.name} of {self.species} species at age {self.age} .")

    def celebrate(self):
        self.age += 1
        print (f" Happy birthday {self.name}. you are {self.age} old") 


 
cat = Pet("karel", "Felis", 5)

cat.display()
cat.celebrate()