from turtle import Turtle

POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.new_turtles = []
        self.create_snake()
        self.head = self.new_turtles[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        rashid = Turtle("square")
        rashid.color("white")
        rashid.penup()
        rashid.goto(position)
        self.new_turtles.append(rashid)

    def extend(self):
        self.add_block(self.new_turtles[-1].position())

    def move(self):
        for tur in range(len(self.new_turtles) - 1, 0, -1):
            new_x = self.new_turtles[tur - 1].xcor()
            new_y = self.new_turtles[tur - 1].ycor()
            self.new_turtles[tur].goto(new_x, new_y)
        self.new_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def game_over(self):
        if self.head.heading() >= 300 or self.head.heading() <= -300:
            print("Game Over")

    def reset(self):
        for block in self.new_turtles:
            block.goto(1000, 1000)
        self.new_turtles.clear()
        self.create_snake()
        self.head = self.new_turtles[0]


