import turtle
import time
import winsound

# Variables
WIDTH = 700
HEIGHT = 550
dx = 0.5
dy = 0.5
exit = False

# Creating window
window = turtle.Screen()
window.title('Pong Game')
window.setup(WIDTH,HEIGHT)
window.bgpic('pong_pic.png')
window.tracer(10)

# creating box
box = turtle.Turtle()
box.shape('square')
box.speed(0)
box.hideturtle()
box.width(10)
box.color('#00FF00')
box.penup()
box.goto(0,-250)
box.pendown()
box.forward(320)
box.left(90)
box.forward(505)
box.left(90)
box.forward(650)
box.left(90)
box.forward(505)
box.left(90)
box.forward(350)

# CREATING NET IN BETWEEN
line = turtle.Turtle()
line.hideturtle()
line.speed(0)
line.penup()
line.color('#00FF00')
line.left(90)
line.shape('square')
line.width(7)
line.goto(0,-250)
for i in range(13):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# creating objects
ball = turtle.Turtle()
ball.shape('circle')
ball.color('#00FF00')
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.speed(1)

bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape('square')
bat_a.color('#A32CC4')
bat_a.shapesize(stretch_len=1,stretch_wid=5)
bat_a.penup()
bat_a.goto(-315,0)

bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape('square')
bat_b.color('#A32CC4')
bat_b.shapesize(stretch_len=1,stretch_wid=5)
bat_b.penup()
bat_b.goto(305,0)

# creating functions
def right_up():
    y = bat_b.ycor()
    bat_b.sety(y+40)
def right_down():
    y = bat_b.ycor()
    bat_b.sety(y-40)
def left_up():
    y = bat_a.ycor()
    bat_a.sety(y+40)
def left_down():
    y = bat_a.ycor()
    bat_a.sety(y-40)
def end():
    global exit
    exit = True
def stop():
    global dy
    global dx
    final = turtle.Turtle()
    ball.hideturtle()
    ball.clear()
    dx = 0
    dy = 0
    final.hideturtle()
    final.width(4)
    line.clear()
    final.speed(0)
    final.penup()
    final.color('#00FF00')
    if score_a>score_b:
        final.write('Player A won the game',align='center',font =('arial',20))
    elif score_b>score_a:
        final.write('Player B won the game',align = 'center',font =('arial',20))
    else:
        final.write('It was a Draw',align='center',font = 20)
    score.clear()

# creating keyboard functions
window.listen()
window.onkeypress(right_up,'Up')
window.onkeypress(right_down,'Down')
window.onkeypress(left_up,'W')
window.onkeypress(left_up,'w')
window.onkeypress(left_down,'S')
window.onkeypress(left_down,'s')
window.onkeypress(end,'E')
window.onkeypress(end,'e')
window.onkeypress(stop,'q')
window.onkeypress(stop,'Q')

# scoreboard
score_a = 0
score_b = 0
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.speed(0)
score.color('#A32CC4')
score.goto(0,225)
score.write('Player A: {}   Player B: {}'.format(score_a,score_b),font=('arial',15),align= 'center')

def ball_movement():
    x = ball.xcor()
    y = ball.ycor()
    ball.setx(x+dx)
    ball.sety(y+dy)

while exit == False:
    ball_movement()
    # collides with upper boundary
    if ball.ycor()>=240:
        # ball.sety(230)
        dy = dy*(-1)
    # collides with lower boundary
    if ball.ycor()<= -240:
        dy = dy*(-1)
    # collides with right boundary
    if ball.xcor()>=310:
        ball.goto(0,0)
        score_a += 10
        score.clear()
        score.write('Player A: {}   Player B: {}'.format(score_a, score_b), font=('arial', 15), align='center')
        time.sleep(1)
    #collides with right boundary
    if ball.xcor()<=-320:
        ball.goto(0, 0)
        score_b += 10
        score.clear()
        score.write('Player A: {}   Player B: {}'.format(score_a, score_b), font=('arial', 15), align='center')
        time.sleep(1)
    #collision with bat_b
    if ball.xcor()>=280 and (ball.ycor()>bat_b.ycor()-50 and ball.ycor()<bat_b.ycor()+50):
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)
        ball.setx(280)
        dx *= -1
    #collision with bat_a
    if ball.xcor()<=-290 and (ball.ycor()>bat_a.ycor()-50 and ball.ycor()<bat_a.ycor()+50):
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)
        ball.setx(-290)
        dx *= -1
    window.update()
