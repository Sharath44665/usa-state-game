import turtle
import pandas

hello = {'state': {34: 'Ohio'},
         'x': {34: 176},
         'y': {34: 52}
         }

my_screen= turtle.Screen()
# my_turtle=Turtle()
my_screen.title("USA state Games")
image="blank_states_img.gif"
my_screen.addshape(image)
states_data=pandas.read_csv("50_states.csv")
turtle.shape(image)
turtle.penup()
i =0
while i <5:
    # need to add numbers
    user_value=my_screen.textinput(title=f"{i+1}/5 States Correct", prompt="Enter another state").title()
    states_data_row=states_data[states_data["state"]==user_value]
    x_pos= int(states_data_row["x"])
    y_pos= int(states_data_row["y"])
    turtle.goto(x=x_pos,y=y_pos)
    turtle.write()
    i+=1
    # i=9

turtle.mainloop()