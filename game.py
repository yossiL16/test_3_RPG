from core.player import Player, PlayerGeneral
from core.goblin import Goblin, PlayerGeneral
from core.orc import Orc, PlayerGeneral
import random


class Game:

    @staticmethod
    def start():
        Game.show_menu()

    @staticmethod
    def show_menu():
        print("The battle begins, the game ends when it is the life of one of the players.")
        print("good luck")

    @staticmethod
    def choose_random_monster():
        orc = {
            "name": "Dvizard",
            "hp": 50,
            "type": "orc",
            "speed": random.randint(0, 5),
            "power": random.randint(10, 15),
            "armor_rating": random.randint(2, 8),
            "weapon": random.choice(["knife", "sword", "ax"])
        }

        goblin = {
            "name": "bob",
            "hp": 20,
            "type": "orc",
            "speed": random.randint(5, 10),
            "power": random.randint(5, 10),
            "armor_rating": 1,
            "weapon": random.choice(["knife", "sword", "ax"])
        }

        monster = random.choice([orc, goblin])
        if monster["type"] == "orc":
             monster1 = Orc(monster["name"], monster["hp"], monster["type"], monster["speed"], monster["power"],monster["armor_rating"], monster["weapon"])
             return monster1
        elif monster["type"] == "goblin":
            monster2 = Goblin(monster["name"], monster["hp"], monster["type"], monster["speed"], monster["power"],monster["armor_rating"], monster["weapon"])
            return monster2

    @staticmethod
    def roll_dice(sides):
        return random.randint(1, sides)


    @staticmethod
    def choose_random_player():

        fighter = {
            "name": "avi",
            "hp": 50,
            "speed": random.randint(5, 10),
            "power": random.randint(5, 10) + 2,
            "armor_rating": random.randint(5, 15),
            "profession": "fighter"
        }

        cure = {
            "name": "avi",
            "hp": 60,
            "speed": random.randint(5, 10),
            "power": random.randint(5, 10) + 2,
            "armor_rating": random.randint(5, 15),
            "profession": "cure"
        }

        player = random.choice([fighter, cure])

        if player["profession"] == "fighter":
            player1 = Player(player["name"], player["hp"], player["speed"], player["power"],player["armor_rating"], player["profession"])
            return player1
        elif player["profession"] == "cure":
            player2 = Player(player["name"], player["hp"], player["speed"], player["power"],player["armor_rating"], player["profession"])
            return player2




