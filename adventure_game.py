import random

class Character:
    """Represents a character in the game with a name, health, strength, and other attributes."""
    def __init__(self, name, health, strength, munnies=30, level=1, experience=0):
        """Initialize the character with name, health, strength, and default values for other properties."""
        self.name = name
        self.health = health
        self.strength = strength
        self.munnies = munnies
        self.level = level
        self.experience = experience
        self.inventory = []

    def add_munnies(self, amount):
        """Add an amount of munnies to the character's total."""
        self.munnies += amount

    def add_experience(self, amount):
        """Add experience to the character; level up if enough experience is gained."""
        self.experience += amount
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        """Increase the character's level and improve health and strength."""
        self.level += 1
        self.health += 20
        self.strength += 5
        self.experience = 0
        print(f"{self.name} has reached level {self.level}!")

    def use_item(self):
        """Use an item from the inventory, such as a health potion."""
        if "Health Potion" in self.inventory:
            self.health = 100
            self.inventory.remove("Health Potion")
            print(f"{self.name} used a Health Potion. Health restored to 100!")
        else:
            print("No Health Potions in inventory. Buy a Health Potion by selecting option 2 for shopping.")

    def buy_item(self, item, item_cost):
        """Buy an item if enough munnies are available."""
        if self.munnies >= item_cost:
            self.munnies -= item_cost
            self.inventory.append(item)
            print(f"{self.name} bought {item}. Remaining munnies: {self.munnies}")
        else:
            print(f"Not enough munnies. You have {self.munnies} munnies.")

class Enemy:
    """Represents an enemy in the game."""
    def __init__(self, name, health, strength, experience_reward):
        """Initialize the enemy with a name, health, strength, and experience reward."""
        self.name = name
        self.health = health
        self.strength = strength
        self.experience_reward = experience_reward

class Town:
    """Represents a town in the game where characters can visit shops."""
    def __init__(self, name, shop_items):
        """Initialize the town with a name and a list of shop items."""
        self.name = name
        self.shop_items = shop_items

    def enter_shop(self, character):
        """Allow a character to enter the shop and purchase items."""
        print(f"{character.name} entered a shop in {self.name}.")
        for item, cost in self.shop_items.items():
            print(f"{item}: {cost} munnies")
        print(f"You have {character.munnies} munnies.")
        choice = input("Continue shopping? (yes/no) ")
        if choice.lower() == 'yes':
            item = input("Enter the item name you want to buy: ")
            if item in self.shop_items:
                character.buy_item(item, self.shop_items[item])
            else:
                print("Item not found.")

def battle(character, enemy):
    """Conducts a battle between the character and an enemy."""
    print(f"A wild {enemy.name} appears!")
    while True:
        print(f"Enemy health: {enemy.health}/100, Your health: {character.health}/100")
        action = input("Choose an action: (1) Attack (2) Do not attack: ")
        if action == '1':
            enemy.health -= character.strength
            if enemy.health <= 0:
                enemy.health = 0
                print(f"{character.name} defeated {enemy.name}!")
                loot = random.randint(10, 50)
                character.add_munnies(loot)
                character.add_experience(enemy.experience_reward)
                print(f"{character.name} found {loot} munnies and has been leveled up!")
                return True
            character.health -= enemy.strength
        elif action == '2':
            print(f"{character.name} did not attack and lost 50 health.")
            character.health -= 50

        if character.health <= 0:
            character.health = 0
            print(f"{character.name} has been defeated by the {enemy.name}.")
            if "Health Potion" in character.inventory:
                use_potion = input("Would you like to use a Health Potion to restore your health to 100 and continue? (yes/no): ")
                if use_potion.lower() == 'yes':
                    character.use_item()
                    return True
            return False
        else:
            print(f"After the battle, {character.name}'s health is {character.health}/100.")

def main():
    """The main function to run the adventure game."""
    hero = Character("Hero", 100, 10)
    enemies = [Enemy("Goblin", 30, 5, 20), Enemy("Wolf", 40, 8, 30)]
    town = Town("Greenville", {"Sword": 30, "Shield": 20, "Health Potion": 50})

    while hero.health > 0:
        action = input("Do you want to (1) explore, (2) enter shop, or (3) quit? ")
        if action == '1':
            enemy = random.choice(enemies)
            if not battle(hero, enemy):
                print("Thank you for playing!")
                break
        elif action == '2':
            town.enter_shop(hero)
        elif action == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
