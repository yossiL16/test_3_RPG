import random
from random import choice


class PlayerGeneral:

    def __init__(self,name ,hp ,speed ,power ,armor_rating):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating




class Player(PlayerGeneral):

    def __init__(self,name ,hp ,speed ,power ,armor_rating,profession):
        super().__init__(name ,hp ,speed ,power ,armor_rating)
        self.profession = profession

    def speak(self):
        print(f"{self.name} is king!")

    def sttack(self,armor_rating, dice):

        if dice + self.speed > armor_rating:
            damage = random.randint(1,6) + self.power
            return damage
        else:
            return False







fighter = {
            "name": "avi",
            "hp":50,
           "speed":random.randint(5,10),
           "power":random.randint(5,10) + 2,
           "armor_rating": random.randint(5,15),
           "profession": "fighter"
           }

cure = {
        "name": "avi",
        "hp":60,
        "speed":random.randint(5,10),
        "power":random.randint(5,10) + 2,
        "armor_rating": random.randint(5,15),
        "profession": "cure"
        }



# listi = [fighter, cure]
# choice_player = random.choice(listi)
# print(choice_player)
# player = Player("yossi", choice_player["hp"], choice_player["speed"], choice_player["power"], choice_player["armor_rating"], choice_player["profession"])
# player.printi()
# player.speak()