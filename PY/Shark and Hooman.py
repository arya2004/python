# Classes and Constructor and inheritance

class Earthling:
    def live(self):
        print("I stay on Earth")


class Mammals(Earthling):
    def __init__(self, language):
        self.outer_covering = "Skin"
        self.food = "Meat"
        self.language = language


class Aquatic(Earthling):
    def __init__(self, language):
        self.outer_covering = "Scale"
        self.food = "Fish"
        self.language = language


human = Mammals("speak")
print(f"Human eats {human.food}")
print(f"Human {human.language}")
human.live()

shark = Aquatic("Meow")
print(f"Terry the Shark has {shark.outer_covering}s")
print(f"Terry the Shark {shark.language}s")
shark.live()
