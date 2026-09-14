from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Ferrum Circle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bumbo")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    secondGoblin = Goblin("Scribble")
    print(f"{secondGoblin.name} enters the arena with {secondGoblin.health} health.")
    
    print("But no hero has answered the call... yet.")

if __name__ == "__main__":
    main()
