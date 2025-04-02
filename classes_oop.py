class SuperHero():

    def fly(self):
        return "superhero flying away."

class Bird():

    def fly(self):
        return "Bird is flying away"

for superNatural in [SuperHero(),Bird()]:
        print(superNatural.fly())
                         

hero = SuperHero()