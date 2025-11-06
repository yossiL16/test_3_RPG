import random
from core.player import Player, PlayerGeneral
from core.goblin import Goblin,PlayerGeneral
from core.orc import Orc, PlayerGeneral
from game import Game


def main():

    Game.start()

    player = Game.choose_random_player()
    monster = Game.choose_random_monster()
    dice_player = Game.roll_dice(6)
    dice_monster = Game.roll_dice(6)
    turn = None
    not_turn = None
    if dice_player >= dice_monster:
        turn = player
        not_turn = monster
    else:
        turn = monster
        not_turn = player
    while True:
        if turn == player:
            rezolt = turn.sttack(monster.armor_rating, dice_player)
            if rezolt != False:
                monster.hp -= rezolt
                turn, not_turn = monster, player
                continue
            else:
                turn, not_turn = monster, player
                continue

        elif turn == monster:
            rezolt = turn.sttack(monster.armor_rating, dice_player)
            if rezolt != False:
                player.hp -= rezolt
                turn, not_turn = player, monster
                continue
            else:
                turn, not_turn = player, monster
                continue







