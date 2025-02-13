#Inheritance
#How does inheritance work in terms of code? 
class Animal():
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")

#In order to get this fish class to inherit from another classs all we have to do is add a set of parentheses after the name 
#of the class and then provide the class we want to inherit it from
#for example 
class Fish(Animal):
    def __init__(self):
        #Then in order to get everything that an animal has and its attributes and methods 
        #We have to add this super().__init__()
        super().__init__()
    
    #What if we wanted to inherit a method from the superclass but want to modify it a bit? 
    def breathe(self):
        #This means that we're going to do everything the breathe method from the superclass does 
        super().breathe()
        print("doing this underwater.")

    
    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

#What does this mean it allows us to take an existing class somebody has created and then build on top of that 


