from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1F1F1F")
screen.title("Snake")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')
    
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    #Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        # Make sure food does not render on top of snake
        for segment in snake.segments:
            if food.distance(segment) < 10:
                food.refresh()
        snake.extend()
        scoreboard.increment_score()
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
        snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()
            
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
