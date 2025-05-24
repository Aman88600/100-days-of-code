class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and Exhale")

class Fish(Animal):
    def __init__(self):
        # With this we will have all the attributes and methods of Animal class
        super().__init__()

    # Modifying the inherited function
    def breathe(self):
        super().breathe()
        print('Under water')
    def swim(self):
        print('swim in water')

    
nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)