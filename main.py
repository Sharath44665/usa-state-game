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
# val=states_data[states_data["state"]=="Alaska"]
# above line = get the row of Alaska
turtle.shape(image)

my_turtle=turtle.Turtle()
my_turtle.penup()
my_turtle.hideturtle()
i =0
score=0
user_double_check=[]
while i <5:
    # need to add numbers
    user_value=my_screen.textinput(title=f"{score}/50 States Correct", prompt="Enter another state").title()
    states_data_row=states_data[states_data["state"]==user_value]
    print(states_data_row)
    # i=9
    if user_value=="Exit":
        # new_list=[states for states in states_data_row if states not in states_data_row]
        break
    if states_data_row.empty:
        i+=1
    else: # states_data_row["state"]==user_value:
        x_pos= int(states_data_row["x"])
        y_pos= int(states_data_row["y"])
        my_turtle.goto(x=x_pos,y=y_pos)
        my_turtle.write(user_value)

        if user_value in user_double_check:
            pass
        else:
            user_double_check.append(user_value)
            score+=1


        i+=1
    if score==50:
        my_turtle.goto(0,250)
        my_turtle.write("Wow! Super...!", True, align="center", font=('Arial', 12, 'bold'))

my_turtle.goto(x=0,y=250)
my_turtle.write(f"your final score: {score}", True, align="center", font=('Arial', 12, 'bold'))




turtle.mainloop()