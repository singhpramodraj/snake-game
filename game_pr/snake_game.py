from turtle import Turtle, Screen
import time
from snake import Snake
from snake_food import Food
from Score_board import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
game_is_on=True
# making the tracer off so that it does not start printing as soon the command is given in th ecode
screen.tracer(0)

# step 1 - creating the snake body with help of three squares
snake = Snake()
food = Food()
scoreboard=Scoreboard()

# this will pop up the screen the time when all above commands are hit

# now controlling snake
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.2)
    # for t in turtles:
    #     t.forward(20)
    #     # screen.update()
    #     #  time.sleep(1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.set_new()
        scoreboard.increase_score()
        snake.extend_snake()

    # Detect the wall
    if snake.head.xcor() >280 or snake.head.ycor()>280 or snake.head.ycor()<-280 or snake.head.xcor() <-280:
        scoreboard.reset()
        snake.reset_snake()


    # detecting the collision of snake with itself
    for segment in snake.segments[1:]:

       # if segment == snake.head: # here because obviously distance of head from itself will eb less than 10
          #  pass
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset_snake()


screen.exitonclick()