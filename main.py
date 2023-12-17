import turtle as t
import time
import character
screen = t.Screen()
screen.setup(640,360)
screen.bgpic("picture/background/background.gif")
screen.update()


# 
screen.listen()
screen.onkey(character.move_left,'Left')
screen.onkey(character.move_right,'Right')

screen.exitonclick()
