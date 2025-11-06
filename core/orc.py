import random
from core.player import PlayerGeneral


class Orc(PlayerGeneral):
    def __init__(self, name,type ,hp, speed, power, armor_rating,weapon):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = type
        self.weapon = weapon

    def speak(self):
        print(f"the Orc {self.name} is furious")

    def sttack(self, armor_rating, dice, weapon):

        if dice + self.speed > armor_rating:
            damage = random.randint(1, 6) + self.power
            if weapon == "knife":
                damage *= 0.5
            elif weapon == "sword":
                damage *= 1
            elif weapon == "ax":
                damage *= 1.5

            return damage
        else:
            return False



orc = {
        "name": "Dvizard",
        "hp": 50,
       "type": "orc",
       "speed": random.randint(0,5),
       "power": random.randint(10,15),
       "armor_rating": random.randint(2,8),
       "weapon": random.choice(["knife", "sword", "ax"])
}

