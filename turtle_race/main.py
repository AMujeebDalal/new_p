from turtle import Turtle, Screen
import random
screen = Screen()


screen.setup(width=500, height=400)
colors = ['red', 'violet', 'indigo', 'blue', 'green', 'yellow']
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet in colors:
    is_race_on = True
all_turtle = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed()
    new_turtle.penup()
    new_turtle.goto(-240, -90 + i * 33)
    new_turtle.color(colors[i])
    all_turtle.append(new_turtle)

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 225:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The winning turtle is {winner}")
            else:
                print(f"You lost! The winning turtle is {winner}")
            is_race_on = False
        turtle.forward(random.randint(1, 12))

screen.exitonclick()
