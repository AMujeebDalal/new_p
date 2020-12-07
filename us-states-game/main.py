import turtle as t
import pandas as pd

df = pd.read_csv("50_states.csv")
screen = t.Screen()
state = t.Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
i = 0
t.shape(image)
state_list = list(df['state'])
answered_states = []
states_to_learn = []
state.penup()
state.hideturtle()
while i <= 50:
    answer_state = screen.textinput(title=f"Guess the state {i}/50", prompt="What's another state").title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in state_list if state not in answered_states]
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list and answer_state not in answered_states:
        i += 1
        x = int(df[df.state == answer_state]['x'])
        y = int(df[df.state == answer_state]['y'])
        state.goto(x, y)
        state.write(answer_state, align="center", font=("Courier", 10, "normal"))
        answered_states.append(answer_state)
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)

t.mainloop()
