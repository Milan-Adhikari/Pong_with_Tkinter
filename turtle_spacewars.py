# what i have done here is that, the main bullet moves upward, then i have created
# trailers. the 1st trailer, or the 0th tailer trails the main bullet while
# other trailer trail their successor trailers. in this way, the bullets are moving

import turtle
import random


end = False

colors = ['#00FFFF','#00FF33','#FFFF00','#FFCCFF','#FF9900','#FF33FF','#FF3333','#FF00CC']

window = turtle.Screen()
window.setup(400,550)
window.bgpic('spacewars_complete.png')
window.tracer(0)

# creating a box
box = turtle.Turtle()
box.hideturtle()
box.penup()
box.speed(0)
box.goto(0,-245)
box.color('#FF99CC')
box.width(6)
box.pendown()
box.forward(170)
box.left(90)
box.forward(495)
box.left(90)
box.forward(345)
box.left(90)
box.forward(495)
box.left(90)
box.forward(220)

#score
score1 = 0
score = turtle.Turtle()
score.hideturtle()
score.color('#00FF00')
score.penup()
score.speed(1)
score.goto(0,220)
score.write('Score: {}'.format(score1), align='center', font=('arial', 20))

# shooter
shooter = turtle.Turtle()
shooter.color('cyan')
shooter.shape('triangle')
shooter.begin_fill()
shooter.speed(0)
shooter.penup()
shooter.left(90)
shooter.shapesize(stretch_wid=1.3,stretch_len=1.3)
shooter.goto(0,-210)
shooter.end_fill()

# keyboard functions
def right():
    if shooter.xcor()<=120:
        shooter.setx(shooter.xcor()+40)
def left():
    if shooter.xcor()>-130:
        shooter.setx(shooter.xcor()-40)

# Keyboard
window.listen()
window.onkeypress(right,'D')
window.onkeypress(left,'A')
window.onkeypress(right,'d')
window.onkeypress(left,'a')

# main bullet
bullet = turtle.Turtle()
bullet.shape('circle')
bullet.color('#FF3333')
bullet.penup()
bullet.shapesize(stretch_len=0.4,stretch_wid=0.4)
bullet.speed(0)
bullet.goto(shooter.xcor(),shooter.ycor())

# bullet goto shooter
def goto_shooter(shooter1):
    window.tracer(0)
    bullet.goto(shooter1.xcor(),shooter1.ycor()+25)

#bullet movement
def movement(bullet):
    window.tracer(1)
    bullet.speed(1)
    bullet.sety(bullet.ycor()+20)

# list
list = []

# tracers
def trailers():
    window.tracer(0)
    bullet1 = turtle.Turtle()
    bullet1.shape('circle')
    bullet1.color('#FF0000')
    bullet1.penup()
    bullet1.shapesize(stretch_len=0.4, stretch_wid=0.4)
    bullet1.speed(0)
    bullet1.goto(shooter.xcor(), shooter.ycor())
    list.append(bullet1)
def trailer_movement():
    if len(list) > 0:
        list[0].goto(bullet.xcor(), bullet.ycor())
    for i in range(len(list) - 1, 0, -1):
        list[i].goto(list[i - 1].xcor(), list[i - 1].ycor()+15)
def delete_trailers():
    for trailer in list:
        if trailer.distance(shooter)>200:
            list.remove(trailer)
            trailer.clear()
            trailer.hideturtle()


# faller list
faller_list = []

def fallers():
    #for i in range(4):
        window.tracer(0)
        fall = turtle.Turtle()
        fall.color(random.choice(colors))
        fall.speed(1)
        fall.shapesize(stretch_wid=1,stretch_len=1)
        fall.shape('square')
        fall.right(90)
        fall.penup()
        fall.goto(random.randint(-160,160),250)
        faller_list.append(fall)
def faller_movement():
    window.tracer(0)
    for i in range(len(faller_list)):
        faller_list[i].sety(faller_list[i].ycor()-20)

def collision():
    global score1
    for trailer in list:
        for faller in faller_list:
             if trailer.distance(faller)<30:
                faller_list.remove(faller)
                faller.clear()
                faller.hideturtle()
                score1 += 1
                score.clear()
                score.write('Score: {}'.format(score1), align='center', font=('arial', 20))


def end_greeting():
    window.tracer(0)
    text = turtle.Turtle()
    text.hideturtle()
    text.color('#00FF00')
    text.penup()
    text.speed(0)
    score.goto(0, 30)
    score.clear()
    score.write('Score: {}'.format(score1), align='center', font=('arial', 20))
    text.write('Game Over',align='center',font=('arial',20))


def collision_bottom():
    global end
    for faller in faller_list:
        if faller.ycor() < -240:
            end = True
            bullet.clear()
            shooter.clear()
            bullet.hideturtle()
            shooter.hideturtle()
            for trailer in list:
                trailer.clear()
                trailer.hideturtle()
            for faller1 in faller_list:
                faller1.clear()
                faller1.hideturtle()
            end_greeting()

while True:
    if end == False:
        goto_shooter(shooter)
        trailers()
        trailer_movement()
        delete_trailers()
        movement(bullet)
        if len(faller_list)<3:
            fallers()
        faller_movement()
        collision()
        collision_bottom()
    window.update()

