class Animal:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_head = 1
        self.num_body = 1

    def breath(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()    

    def breath(self):
        super().breath()
        print("Doing this underwater.")

    def swim(self):
        print("moving in the water.")


nemo = Fish()
nemo.swim()
print(nemo.num_eyes)
nemo.breath()