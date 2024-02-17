from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from scoore_board import ScooreBoard
from difficulty import Difficulty

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
counter = 0

Snake = Snake()
food = Food()
scoore_board = ScooreBoard(counter)
difficulty = Difficulty()

user_level = False
while user_level not in ["easy", "medium", "hard", "wtf"]:
    user_level = screen.textinput("Choose a difficulty level!", "Type a level: easy, medium, hard, wtf").lower()
    screen.listen()
    screen.onkeypress(Snake.up, "Up")
    screen.onkeypress(Snake.down, "Down")
    screen.onkeypress(Snake.left, "Left")
    screen.onkeypress(Snake.right, "Right")

game_is_on = True
while game_is_on:

    screen.update()
    difficulty.set_difficulty(user_level)
    Snake.move()

    if Snake.head.distance(food) < 15:
        food.refresh()
        scoore_board.write(counter)
        scoore_board.scoore()
        Snake.extend()

    if Snake.head.xcor() > 350 or Snake.head.xcor() < -350 or Snake.head.ycor() < -350 or Snake.head.ycor() > 350:
        scoore_board.game_over()
        game_is_on = False

    for segment in Snake.whole_snake[1:]:
        if Snake.head.distance(segment) < 5:
            scoore_board.game_over()
            game_is_on = False


screen.exitonclick()