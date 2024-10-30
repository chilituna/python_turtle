from turtle import Turtle, Screen
import random

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

screen = Screen()
screen.setup(width=500, height=400)

game_continues = True
while game_continues:
    screen.bgcolor("black")
    screen.title = "Turtle Race"
    user_bet = int(screen.numinput(title="Make a bet!", prompt="Give number: [1]Purple [2]Blue [3]Green [4]Yellow [5]Orange [6]Red"))
    try:
        user_color = colors[user_bet - 1]
    except IndexError:
        print("Incorrect number given")

    turtles = []
    y = 70
    for i in range(6):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(colors[i])
        turtle.goto(x=-230, y=y)
        turtle.pendown()
        turtles.append(turtle)
        y -= 30

    game_is_on = True
    while game_is_on:
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.xcor() > 230:
                game_is_on = False
                if turtle.pencolor() == user_color:
                    play_more = screen.textinput(title="Race over!", prompt=f"You won! {turtle.pencolor()} was fastest. Play again? [y/n]")
                else:
                    play_more = screen.textinput(title="Race over!", prompt=f"You lose. {turtle.pencolor()} was fastest. Play again? [y/n]")
                if play_more == "y":
                    screen.clearscreen()
                    game_continues = True
                else:
                    game_continues = False
                break


screen.exitonclick()
