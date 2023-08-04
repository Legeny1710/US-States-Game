import turtle
import pandas as pd

img = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)

screen.addshape(img)
turtle.shape(img)

state_guessed = 0



df = pd.read_csv("50_states.csv")



while state_guessed != 50:
    answer_state = screen.textinput(title=f"{state_guessed}/50 states guessed", prompt="What's another state's name?: ").capitalize()
    for state in df["state"]:
        if state == answer_state:
            state_turtle = turtle.Turtle()
            state_turtle.hideturtle()
            state_turtle.penup()
            state_turtle.goto(int(df[df["state"] == state].x), int(df[df["state"] == state].y))
            state_turtle.write(f"{state}", align="center", font=("Courier", 10, "normal"))
            state_guessed += 1

























screen.exitonclick()