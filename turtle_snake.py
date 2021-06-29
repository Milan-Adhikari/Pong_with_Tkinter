import turtle
import time
import random

delay = 0.1
end = 0

win = turtle.Screen()
win.title("Snake ")
win.setup(width=500,height=500)
win.bgcolor("black")
win.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.penup()
head.color("#E71313")
head.shape("square")
head.direction = "stop"

segments = []

food = turtle.Turtle()
food.speed(0)
food.penup()
food.color("#FF25E5")
food.shape("circle")
food.goto(30,70)

endtext = turtle.Turtle()
endtext.speed(0)
endtext.color("white")
endtext.penup()
endtext.goto(0,-230)
endtext.hideturtle()
endtext.write("Press 'g' to End Game",align="center",font=(10))

#score
sc = 0
highsc = 0
score = turtle.Turtle()
score.penup()
score.color("white")
score.hideturtle()
score.speed(0)
score.goto(0,220)
score.write("Score : {}     Highscore: {}".format(sc,highsc),align="center",font=("arial",15))

#Functions
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def right():
    head.direction = "right"
def left():
    head.direction = "left"
def enter():
    global end
    end = 1
def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+25)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-25)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+25)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-25)

win.listen()
win.onkeypress(up,"w")
win.onkeypress(down,"s")
win.onkeypress(right,"d")
win.onkeypress(left,"a")
win.onkeypress(enter,"g")


while end == 0:
    win.update()
    #boundary
    if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        sc = 0
        score.clear()
        score.write("Score : {}     Highscore: {}".format(sc, highsc), align="center", font=("arial", 15))
    #food collision
    if head.distance(food)<20:
        x = random.randint(-220,220)
        y = random.randint(-220,220)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.penup()
        new_segment.color("#A460DC")
        new_segment.shape("square")
        segments.append(new_segment)

        sc += 10
        if sc > highsc:
            highsc = sc
        score.clear()
        score.write("Score : {}     Highscore: {}".format(sc, highsc), align="center", font=("arial", 15))

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x =head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    movement()

    #collision with body
    for segment in segments:
        if segment.distance(head)<20:
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            sc = 0
            score.clear()
            score.write("Score : {}     Highscore: {}".format(sc, highsc), align="center", font=("arial", 15))
    time.sleep(delay)
win.mainloop()

