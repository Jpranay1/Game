from tkinter.tix import Balloon
import turtle

wn = turtle.Screen()
wn.title("Pong by pranay")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stops the window from updating

#score 
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set a speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #set a speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
Ball = turtle.Turtle()
Ball.speed(0) #set a speed
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.3
Ball.dy = -0.3

#pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="Center", font=("Courier",24,"normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)

def paddle_a_dw():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def paddle_b_dw():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_dw, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_dw, "Down")

#main game loop

while True:
    wn.update()

    #move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #border check
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    
    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="Center", font=("Courier",24,"normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="Center", font=("Courier",24,"normal"))

    #paddle and ball collisions
    if Ball.xcor() > 340 and (Ball.ycor() < paddle_b.ycor() + 40 and Ball.ycor() > paddle_b.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1
    
    if Ball.xcor() < -340 and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
