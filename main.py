import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("Guess the State")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


#grab the data
state_data = pandas.read_csv("50_states.csv")
state_name = state_data.state.to_list()
x_cor = state_data.x
y_cor = state_data.y

missed_state = state_name
correct = 0
game_is_on = True
while game_is_on:
	answer_state = screen.textinput(f"{correct}/50", "Whats another state's name?").title()
	if answer_state == "Exit":
		break
	if answer_state in state_name:
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		location = state_data[state_data.state == answer_state]
		t.goto(int(location.x), int(location.y))
		t.write(answer_state)
		correct += 1
		missed_state.remove(answer_state)
	elif answer_state not in state_name:
		w = turtle.Turtle()
		w.color("red")
		w.hideturtle()
		w.penup()
		w.goto(-300, 0)
		w.hideturtle()
		w.write("That's not a state...Check your spelling!!!!", align="left", font=("Arial", 20, "bold"))
		time.sleep(3)
		w.clear()

df = pandas.DataFrame(missed_state)
df.to_csv("missed_guesses.csv")


turtle.mainloop()
