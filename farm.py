# farm
class Cow:
    # inicjalizator (metoda magiczna)
    def __init__(self, name, age):
        """To tutaj grupuje się wszystkie cechy (atrybuty) klasy"""

        # zestaw wszystkich atrybutów nazywany jest stanem obiektu
        self.name = name
        self.age = age
        self.hungry = True

    # metoda czytająca stan obiektu (atrubut name)
    def speak(self):
        print(f"Muuuuuuuuuuuuuuuu, jestem krowa o imieniu {self.name}")

    # metody modyfikujące stan obiektu
    def eat(self, meal):
        if self.hungry:
            if meal == 3:
                print('To nie wiesz, że 3 się nie je, debilu!')
            else:
                print(f"Jem {meal}")
                self.hungry = False
        else:
            print("Ha, nie jestem głodna. I co mi zrobisz?")

    def run(self):
        print("Biegam, biegam, biegam ...")
        self.hungry = True
        print("aż zgłodniałam")

    def get_older(self):
        self.age += 1


c = Cow("Mućka", 2)
c.speak()
c.eat("trawa")
c.eat("woda")
c.run()
c.eat("woda")

print(f"Krowa {c.name} ma {c.age} lat.")
c.get_older()
print(f"Krowa {c.name} ma {c.age} lat.")
