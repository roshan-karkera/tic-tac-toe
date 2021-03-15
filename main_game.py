import board
import game

restart = "Y"
while(restart == "Y" or restart == "y"):
    game.game()
    restart = input("Do want to play Again?(y/n)")

