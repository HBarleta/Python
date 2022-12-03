class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food) :
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet('Roger', "Dog", ["laydown, shake, bark"], 100, 150)

    def walk(self):
        print(f"{self.first_name} took {self.pet.name} for a walk")
        Pet.play(self.pet)
        return self#walks ninja's pet invoking the pet play() method
    def feed(self):
        print(f"{self.first_name} eats a {self.treats}")
        print(f"{self.first_name} throws a {self.pet_food} for {self.pet.name}")
        Pet.eat(self.pet)
        return self# feeds the ninja's pet invoking the eat() method
    def bathe(self):
        print(f"{self.first_name} gave his pet {self.pet.name} a bath!")
        Pet.noise(self.pet)
        return self#cleans the ninja's pet invoking the noise() method
    
    
    
    
    
class Pet:
    
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
        
    def sleep(self):
        print(f"{self.name} fell asleep ZZZzzZzz...")
        self.energy += 25
        print(f"{self.name} is now at {self.energy} energy!")
        return self#increases pet energy by 25
    
    def eat(self):
        print("Thanks for the treat hooman!")
        print(f"{self.name}'s health was at {self.health} and energy {self.energy}")
        self.energy += 5
        self.health += 10#increases pet energy by 5 and leath by 10
        print(f"{self.name} is now at {self.health} health and {self.energy} energy!")
        return self
    
    def play(self):
        print(f"{self.name} went for some walkies!")
        self.health += 5#increases pet's health by 5
        print(f"{self.name} is now at {self.health} health!")
        return self
    
    def noise(self):
        print("*MOOOOOOOO*")
        return self#prints the pet's sound
    
    
jack = Ninja('Jack', 'Ma', 'bacon', 'Chicken Jerky')
jack.feed()
jack.bathe()
jack.walk()