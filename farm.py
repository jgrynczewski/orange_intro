# farm
class Cow:
    # inicjalizator (metoda magiczna)
    def __init__(self, name):
        """To tutaj grupuje się wszystkie cechy (atrybuty) klasy"""

        self.group = "Mammals"
        self.name = name

    def speak(self):
        print("Muuuuuuuuuuuuuuuu")

    def eat(self, meal):
        if meal == 3:
            print('To nie wiesz, że 3 się nie je, debilu!')
        else:
            print(f"Jem {meal}")


c = Cow("Mućka")
c.speak()
print(f"To jest krowa {c.name}")

c2 = Cow("Milka")
c2.speak()

c.eat("woda")
