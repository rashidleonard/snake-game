import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

rashid = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(rashid.up, "Up")
screen.onkey(rashid.down, "Down")
screen.onkey(rashid.right, "Right")
screen.onkey(rashid.left, "Left")

""""This loop also works together with the x_positions. but I'll change to the lesson being thought.
what i did below is actually my own thing"""

# x_positions = [0, -20, -40]
# for turtle in range(0, 3):
#     rashid = Turtle("square")
#     rashid.color("white")
#     rashid.penup()
#     rashid.goto(x_positions[turtle], 0)

# positions = [(-20, 0), (-40, 0), (-60, 0)]
# new_turtles = []

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    rashid.move()

    # Detecting food collision
    if rashid.head.distance(food) < 15:
        food.food_location()
        rashid.extend()
        score.new_score()
        # score.update_scoreboard()

    # detecting collision with wall
    if rashid.head.xcor() >= 290 or rashid.head.xcor() <= -290 or rashid.head.ycor() >= 290 or \
            rashid.head.ycor() <= -290:
        # game_on = False
        # score.game_over()
        # (both lines are commented out to prevent the game from pausing when the snake collide with the tail)
        score.reset()
        rashid.reset()

    # detecting collision with tail
    for block in rashid.new_turtles:
        if block == rashid.new_turtles[0]:
            pass
        elif rashid.head.distance(block) < 10:
            # game_on = False
            # score.game_over()
            # (both lines are commented out to prevent the game from pausing when the snake collide with the tail)
            score.reset()
            rashid.reset()

        # when i run this code, the game does not stop even though the snake bites its tail
        # I should revisit sometime
screen.exitonclick()
