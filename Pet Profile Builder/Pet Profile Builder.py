class Pet:
    def __init__(self, name, animal, age, color):
        self.name = name
        self.animal = animal
        self.age = age
        self.color = color

    def show_profile(self):
        print("------PET PROFILE-------")
        print("Name: ", self.name)
        print("Animal: ", self.animal)
        print("Age: ", self.age)
        print("Color:", self.color)

#Creating objects
pet1 = Pet("Buddy", "Dog", 3, "Borwn")
pet2 = Pet("Mittens", "Cat", 2, "White")

#Displaying profiles
pet1.show_profile()
print()
pet2.show_profile()