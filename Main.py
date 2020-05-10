# First draft

import turtle

# Set up the screen
wn = turtle.Screen()
wn.setup(1627, 842)
wn.bgpic("bgpic.gif")
wn.title("Steichenspiel")
turtle.penup()

# Set up the board
turtle.setx(-200)
turtle.sety(200)
turtle.write("2", font=("Arial", 24, "normal"))

# Close Screen
wn.exitonclick()



