import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.onkey(player.move,"w")


screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if random.randint(1,6) == 1:
        car_manager.make_cars()
    #Generate cars constantly 
    car_manager.move()
    screen.update()

    if player.ycor() > 280:
        player.next_level()
        car_manager.level_up()
        scoreboard.score += 1
        scoreboard.update_score()
        screen.update()
    
    for cars in car_manager.allcars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
