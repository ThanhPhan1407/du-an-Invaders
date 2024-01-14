import turtle as t
import time
import character
import arcade as ac 

bl1 = t.Turtle()
bl2 = t.Turtle()

screen = t.Screen()
screen.setup(640,360)
screen.bgpic("picture/background/background.gif")
screen.update()
bl1.shapesize(1)
bl1.shape('square')
bl2.shapesize(1)
bl2.shape('square')

# di chuyển
screen.listen()
screen.onkey(character.move_left,'Left')
screen.onkey(character.move_right,'Right')

bl1.color('red')
bl2.color('red')
# bắn
bl1.penup()
bl1.hideturtle()
def ban():
    a = character.vitri()
    bl1.setx(a[0])
    bl1.sety(a[1])
    bl1.showturtle()
    while bl1.ycor()<760 :
        bl1.sety(bl1.ycor()+20)
    bl1.hideturtle()
screen.onkey(ban,'space')
    

bl2.penup()
bl2.hideturtle()
def ban():
    a = character.vitri()
    bl2.setx(a[0])
    bl2.sety(a[1])
    bl2.showturtle()
    while bl2.ycor()<760 :
        bl2.sety(bl2.ycor()+20)
    bl2.hideturtle()
screen.onkey(ban,'space')


screen.exitonclick()
#