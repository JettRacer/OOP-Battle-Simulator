import random
from enemy import Enemy



class BOSS(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health = 150)
        self.attack_power = 25

    def attack(self):
        "Return a random amount of damage."
        attackStyle = random.randint(1,3)
        if attackStyle == 1:
            print("FIREBALL")
            return 15
        elif attackStyle == 2:
            print("LAZERBEAM")
            return 20
        elif attackStyle == 3:
            print("Sword Swing")
            return self.attack_power 


        
