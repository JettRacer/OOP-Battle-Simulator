import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
     # Create the Hero's attributes here.
      self.name = name
      self.health = 125
      self.attack_power = 20
      self.armor = 5

    def attack(self):
        # Return a random value from 1 through this Hero's attack power.
        return random.randiant(1, self.attack_power)

    def take_damage(self, damage):
       # Subtract damage, but do not allow health to fall below 0.
       damage = damage - self.armor 
       self.health = max(0, self.health - damage)
   

    def is_alive(self):
       # Return a Boolean based on this Hero's health.
 