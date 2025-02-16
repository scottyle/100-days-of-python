from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.allcars = []
        self.penup()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def make_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        y_position = random.randint(-280,280)
        new_car.goto(x=300,y=y_position)
        self.allcars.append(new_car)
    
    def move(self):
        for cars in self.allcars:
            cars.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
