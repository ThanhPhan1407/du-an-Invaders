import turtle as t
import time
import character
import arcade as ac 

bl1 = t.Turtle()
screen = t.Screen()
screen.setup(640,360)
screen.bgpic("picture/background/background.gif")
screen.update()


# di chuyển
screen.listen()
screen.onkey(character.move_left,'Left')
screen.onkey(character.move_right,'Right')

bl1.color('red')

# bắn
bl1.hideturtle()
def ban():
    a = character.vitri()
    bl1.setx(a[0])
    bl1.sety(a[1])
    bl1.showturtle()
    while bl1.ycor()<760 :
        bl1.sety(a[1]+20)
screen.onkey(ban,'space')
    


screen.exitonclick()
#