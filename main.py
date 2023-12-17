import turtle as t
import time
screen = t.Screen()
screen.setup(640,360)
screen.bgpic("picture\\background\\background.gif")
screen.update()
screen.addshape('picture\\character\\ship.gif')
t.shape("picture\\character\\ship.gif")
screen.exitonclick()
# 
screen.listen()
