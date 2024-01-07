import turtle as t
bl2 = t.Turtle()

pl =t.Turtle()
screen=t.Screen()
# 
screen.addshape('picture/character/ship.gif')
pl.shape("picture/character/ship.gif")
# 
pl.penup()
plspeed = 20
pl.goto(0,-300)
pl.pendown()

# sang trai
def move_left():
    x=pl.xcor() - plspeed
    pl.setx(x)
# sang phai
def move_right():
    x=pl.xcor() + plspeed
    pl.setx(x)

def vitri():
    x=pl.xcor()
    y=pl.ycor()
    a=[x,y]
    return a
