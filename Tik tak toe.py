import turtle
import time

# Create the main window
wn = turtle.Screen()
wn.bgcolor('light blue')       # Set background color
wn.setup(740,740)              # Set window size
wn.tracer()                    # Turn off auto updates for manual update control

# Create turtles to draw the grid lines
gid1 = turtle.Turtle()
gid2 = turtle.Turtle()
gid3 = turtle.Turtle()
gid4 = turtle.Turtle()

# Lift pens so they don't draw while moving into position
gid1.penup()
gid2.penup()
gid3.penup()
gid4.penup()

# Set pen thickness for the grid
gid1.pensize(4)
gid2.pensize(4)
gid3.pensize(4)
gid4.pensize(4)

# Position turtles to draw the four main grid lines
gid1.goto(-100,350)
gid2.goto(100,350)
gid3.goto(350,100)
gid4.goto(350,-100)

# Set turtle drawing speed
gid1.speed(10)
gid2.speed(10)
gid3.speed(10)
gid4.speed(10)

# Rotate turtles to face correct directions for drawing lines
gid1.right(90)
gid2.right(90)
gid3.right(180)
gid4.right(180)

# Put pens down to start drawing
gid1.pendown()
gid2.pendown()
gid3.pendown()
gid4.pendown()

# Draw the four grid lines
gid1.fd(700)
gid2.fd(700)
gid3.fd(700)
gid4.fd(700)

# Hide the turtles after drawing
gid1.hideturtle()
gid2.hideturtle()
gid3.hideturtle()
gid4.hideturtle()

# Update the window with drawn grid
wn.update()

# s determines whose turn it is: 1 = Player 1 (O), 2 = Player 2 (X)
s  = 1
i = 0  # Index for board positions

# Function to handle mouse clicks
def click(x,y):
    global i 
    # Each block in the grid corresponds to a specific index in l1
    if x<=-100 and y >= 100: 
        i = 0
        if l1[i] == 0:
            check()
            shape(-200,100)
            victory()
    elif x <= -100 and -100 <= y <= 100 :
        i = 1
        if l1[i] == 0:
            check()
            shape(-200,-100)
            victory()
    elif x <= -100 and y <= -100:
        i = 2
        if l1[i] == 0:
            check()
            shape(-200,-300)
            victory()
    elif -100 <= x <= 100 and y >= 100 :
        i = 3
        if l1[i] == 0:
            check()
            shape(0,100)
            victory()
    elif -100 <= x <= 100 and 100 >= y >= -100:
        i = 4
        if l1[i] == 0:
            check()
            shape(0,-100)
            victory()
    elif -100 <= x <= 100 and y <= -100:
        i = 5
        if l1[i] == 0:
            check()
            shape(0,-300)
            victory()
    elif x >= 100 and y >= 100:
        i = 6
        if l1[i] == 0:
            check()
            shape(200,100)
            victory()
    elif x >= 100 and 100 >= y >= -100:
        i = 7
        if l1[i] == 0:
            check()
            shape(200,-100)
            victory()
    elif x >= 100 and y <= -100:
        i = 8
        if l1[i] == 0:
            check()
            shape(200,-300)
            victory()

# Turtle to draw X's and O's
fig = turtle.Turtle()
fig.speed(0)
fig.pensize(9)

# Variable to control double clicks and end states
timer = 0

# Function to draw O or X based on player turn
def shape(x,y):
    global s
    global timer
    if s == 1:  # Player 1 draws O
        timer = 1
        s = 2
        fig.color("blue")
        fig.penup()
        fig.goto(x,y)
        fig.pendown()
        fig.circle(100)
        wn.update()
        timer  = 0
    else:       # Player 2 draws X
        s = 1
        timer = 1
        fig.color("#C04000")
        fig.penup()
        fig.goto(x,y)
        fig.fd(100)
        fig.left(135)
        fig.pendown()
        fig.fd(282.84)
        fig.penup()
        fig.left(135)
        fig.fd(200)
        fig.left(135)
        fig.pendown()
        fig.fd(282.84)
        fig.right(45)
        timer = 0

# Board state: 0 = empty, 1 = Player 1, 2 = Player 2
l1 = [0,0,0,0,0,0,0,0,0]    
tied = 0  # Move counter

# Function to update board state when a move is made
def check():
    global s
    global i 
    global tied
    l1[i] = s
    tied += 1

# Turtle for displaying victory messages
gid1.penup()
gid1.goto(0,0)
gid1.color("red")

# Function to check winning conditions
def victory ():
    global timer
    # Player 1 wins
    if l1[0] == 1 and l1[1] == 1 and l1[2] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[0] == 1 and l1[3] == 1 and l1[6] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[0] == 1 and l1[4] == 1 and l1[8] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[1] == 1 and l1[4] == 1 and l1[7] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[2] == 1 and l1[5] == 1 and l1[8] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[6] == 1 and l1[4] == 1 and l1[2] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[3] == 1 and l1[4] == 1 and l1[5] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[6] == 1 and l1[7] == 1 and l1[8] == 1:
        timer = 3
        end()
        gid1.write("Winner Player Number 1",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    # Player 2 wins
    if l1[0] == 2 and l1[1] == 2 and l1[2] == 2: 
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal")) 
        bye()
    elif l1[0] == 2 and l1[3] == 2 and l1[6] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[0] == 2 and l1[4] == 2 and l1[8] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[1] == 2 and l1[4] == 2 and l1[7] == 2:
        timer = 3 
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[2] == 2 and l1[5] == 2 and l1[8] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[6] == 2 and l1[4] == 2 and l1[2] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[3] == 2 and l1[4] == 2 and l1[5] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()
    elif l1[6] == 2 and l1[7] == 2 and l1[8] == 2:
        timer = 3
        end()
        gid1.write("Winner Player Number 2",align = "center",font = ('Rockwell',55,"normal"))
        bye()

# Function to close the game after a short delay
def bye():
    time.sleep(3)
    wn.bye()

# Turtle for clearing the screen area before showing winner
gid2.penup()
gid2.goto(0,0)

# Function to draw white rectangle covering board for end screen
def end():
    gid2.goto(-350,90)
    gid2.pendown()
    gid2.color("white")
    gid2.begin_fill()
    gid2.fd(110)
    gid2.left(90)
    gid2.fd(695)
    gid2.left(90)
    gid2.fd(110)
    gid2.left(90)
    gid2.fd(695)
    gid2.end_fill()

# Function to avoid double clicks and handle draw situation
def not_double_click(x,y):
    if timer == 0:
        click(x,y)
    elif timer == 3:
        x = x
    if tied == 9:  # All cells filled
        end()
        gid1.write("No Player Wins",align = "center",font = ('Rockwell',55,"normal")) 
        bye()

# Listen for clicks
wn.onclick(not_double_click)
wn.listen()

# Initial window update
wn.update()

# Keep the window open
turtle.done()
