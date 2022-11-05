import time
from turtle import Screen
from turtle_crossing_game.player import Player
from turtle_crossing_game.car_manager import CarManager
from turtle_crossing_game.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly spawn cars and move it.
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the player has reached the other side.
    if player.ycor() > 280:
        player.reset_player()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
