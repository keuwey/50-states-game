# -*- coding: utf-8 -*-
import turtle
from turtle import Screen, Turtle

import pandas


def setup_screen():
    screen = Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    return screen


def read_state_data():
    try:
        data = pandas.read_csv("50_states.csv")
    except FileNotFoundError:
        print("Error: File '50_states.csv' not found.")
        return None
    return data


def prompt_state_name(guessed_states):
    textinput = setup_screen().textinput(title=f"{len(guessed_states)}/50 States Correct",
                                         prompt="What's another state name?")
    return textinput.title() if textinput is not None else None


def save_states_to_learn(states_to_learn):
    new_data = pandas.DataFrame(states_to_learn)
    new_data.to_csv("states_to_learn.csv")


def main():
    screen = setup_screen()
    if screen is None:
        return

    data = read_state_data()
    if data is None:
        return

    all_states = data.state.to_list()
    guessed_states = []
    turtle_pen = Turtle()
    turtle_pen.hideturtle()
    turtle_pen.penup()

    while len(guessed_states) < 50:
        answer_state = prompt_state_name(guessed_states)

        if answer_state == "Exit":
            states_to_learn = [
                state for state in all_states if state not in guessed_states]
            save_states_to_learn(states_to_learn)
            break

        if answer_state in all_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            turtle_pen.goto(state_data.x.iloc[0], state_data.y.iloc[0])
            turtle_pen.write(state_data.state.iloc[0])


if __name__ == "__main__":
    main()
