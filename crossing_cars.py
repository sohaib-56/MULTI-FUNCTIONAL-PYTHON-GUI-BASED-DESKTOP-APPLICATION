from turtle import Turtle
import random


COLORS = [
    "#FFFF00", "#008000", "#0000FF", "#A52A2A", "#FFA500", "#B22222",
    "#954b32", "#355d7b", "#aa9a29", "#8a1f14", "#86a3b8", "#c55c49",
    "#2f7956", "#492b23", "#91b295", "#0e6246", "#a08e9e", "#362d32",
    "#654b4d", "#243c4a", "#135659", "#529481", "#931113", "#1b4466",
    "#0c4640", "#6b7f99", "#a86366"
    ]

MOVING_DISTANCE = 5 


class Cars:
    """ This will create the cars and manages their speed """
    
    def __init__(self):
        self.all_cars = []
        self.speed = MOVING_DISTANCE
        
    
    def generate(self):
        rand_number = random.randint(1,6)
        if rand_number == 1:
            tur = Turtle("square")
            tur.shapesize(stretch_wid=1,stretch_len=2)
            tur.penup()
            tur.color(random.choice(COLORS))
            tur.goto(290,random.randint(-230,220))
            self.all_cars.append(tur)

                
    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    
    def increase_speed(self):
        self.speed += 10
        


