from turtle import Turtle 

MOVE_DISTANCE = 20

class Snake:
    def __init__(self) -> None:
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.snake_segments = []
        self.make_snake()
        self.head = self.snake_segments[0]

    def make_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def move(self):
        for seg_num in range((len(self.snake_segments)-1),0,-1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def right(self):
        if self.head.heading() != 180:  # Prevent moving backward
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self,position):
            self.new_segment = Turtle("square")
            self.new_segment.color("white")
            self.new_segment.penup()
            self.new_segment.goto(position)
            self.snake_segments.append(self.new_segment)

    def extend(self):
        """Adds a new segment to the snake."""
        self.add_segment(self.snake_segments[-1].position())