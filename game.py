from goblin import Goblin
from hero import Hero
from boss import BOSS

ARENA_NAME = "The Ferrum Circle"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")



def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bumbo")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    secondGoblin = Goblin("Scribble")
    print(f"{secondGoblin.name} enters the arena with {secondGoblin.health} health.")

    FightMaster = Hero("FightMaster")
    print(f"{FightMaster.name} enters the arena with {FightMaster.health} health.")

    boss = BOSS("ScaryLarry")
    print("Boss has entered the battle")



    battle(FightMaster,boss)


if __name__ == "__main__":
    main()