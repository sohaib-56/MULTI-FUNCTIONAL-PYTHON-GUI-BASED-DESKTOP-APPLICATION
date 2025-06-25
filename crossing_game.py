import time
from turtle import Screen
from crossing_score import Scoreboard
from crossing_cars import Cars
from crossing_player import Player
import games_section


def start_crossing_game():

    try:
        
        screen = Screen()
        screen.title("MS Builds - Turtle Trek Game")
        screen.setup(width=600,height=600)
        screen.tracer(0)


        score = Scoreboard()
        player = Player()
        cars = Cars()

        screen.listen()
        screen.onkey(player.move,"Up")



        flag = True

        while flag:
            screen.update()
            time.sleep(0.1)
            cars.generate()
            cars.move()
            for car in cars.all_cars:
                if car.distance(player) < 20:
                    score.game_over()
                    flag = False



            if player.ycor() > 285:
                score.increment_level()
                player.replace_player()
                cars.increase_speed()



        screen.exitonclick()
        games_section.games()


    except:
        print("Something might be fishy going on.")
        screen.exitonclick()
        games_section.games()







if __name__ == "__main__":
    start_crossing_game()


