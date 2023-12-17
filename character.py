import turtle as t
player =t.Turtle()
screen=t.Screen()
# 
screen.addshape('picture/character/ship.gif')
player.shape("picture/character/ship.gif")
# 
playerspeed = 20

# sang trai
def move_left():
    x=player.xcor() - playerspeed
    player.setx(x)
# sang phai
def move_right():
    x=player.xcor() + playerspeed
    player.setx(x)
    