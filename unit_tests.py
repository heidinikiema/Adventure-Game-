import unittest
from adventure_game import Character, Enemy, Town 

class TestCharacter(unittest.TestCase):
    """Tests for the Character class."""

    def setUp(self):
        """Sets up a test case with a Character instance."""
        self.character = Character("Hero", 100, 10)

    def test_initialization(self):
        """Test if the Character initializes with the correct attributes."""
        self.assertEqual(self.character.name, "Hero")
        self.assertEqual(self.character.health, 100)
        self.assertEqual(self.character.strength, 10)
        self.assertEqual(self.character.munnies, 30)
        self.assertEqual(self.character.level, 1)
        self.assertEqual(self.character.experience, 0)
        self.assertEqual(self.character.inventory, [])

    def test_add_munnies(self):
        """Test the add_munnies method for correctly updating munnies."""
        self.character.add_munnies(20)
        self.assertEqual(self.character.munnies, 50)

    def test_add_experience(self):
        """Test the add_experience method for correct experience and leveling up."""
        self.character.add_experience(50)
        self.assertEqual(self.character.experience, 50)
        self.character.add_experience(50)
        self.assertEqual(self.character.level, 2)
        self.assertEqual(self.character.experience, 0)

    def test_level_up(self):
        """Test the level_up method for correct level, health, and strength increase."""
        self.character.add_experience(100)
        self.assertEqual(self.character.level, 2)
        self.assertEqual(self.character.health, 120)
        self.assertEqual(self.character.strength, 15)

    def test_use_item(self):
        """Test use_item method for correct health restoration and item removal."""
        self.character.inventory.append("Health Potion")
        self.character.health = 50
        self.character.use_item()
        self.assertEqual(self.character.health, 100)
        self.assertNotIn("Health Potion", self.character.inventory)

    def test_buy_item(self):
        """Test buy_item method for correct item addition and munnies calculation."""
        self.character.buy_item("Sword", 20)
        self.assertIn("Sword", self.character.inventory)
        self.assertEqual(self.character.munnies, 10)

        self.character.munnies = 5
        self.character.buy_item("Shield", 10)
        self.assertNotIn("Shield", self.character.inventory)


class TestEnemy(unittest.TestCase):
    """Tests for the Enemy class."""

    def setUp(self):
        """Sets up a test case with an Enemy instance."""
        self.enemy = Enemy("Goblin", 30, 5, 20)

    def test_initialization(self):
        """Test if the Enemy initializes with the correct attributes."""
        self.assertEqual(self.enemy.name, "Goblin")
        self.assertEqual(self.enemy.health, 30)
        self.assertEqual(self.enemy.strength, 5)
        self.assertEqual(self.enemy.experience_reward, 20)


class TestTown(unittest.TestCase):
    """Tests for the Town class."""

    def setUp(self):
        """Sets up a test case with a Town instance."""
        self.town = Town("Greenville", {"Sword": 30, "Shield": 20})

    def test_initialization(self):
        """Test if the Town initializes with the correct name and shop items."""
        self.assertEqual(self.town.name, "Greenville")
        self.assertDictEqual(self.town.shop_items, {"Sword": 30, "Shield": 20})


if __name__ == '__main__':
    unittest.main()

