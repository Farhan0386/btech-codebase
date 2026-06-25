class Animal:              
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):                
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   
        self.breed = breed

    def fetch(self):               
        return f"{self.name} fetches the ball!"

d = Dog("Bruno", "Labrador")
print(d.speak())
print(d.fetch())