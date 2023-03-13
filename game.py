import turtle

window = turtle.Screen()
window.title("Pong in python")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

#functions(paddle A)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#functions(paddle B)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard paddle a
window.listen()
window.onkeypress(paddle_a_up, "7")
window.onkeypress(paddle_a_down, "1")

#keyboard paddle b
window.onkeypress(paddle_b_up, "9")
window.onkeypress(paddle_b_down, "3")

#main game loop

while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #border(top and bottom)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*= -1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*= -1

    #border(left and right)
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1

    #paddle detect(paddle_a)
    if ball.xcor()<-340 and (ball.ycor())
        ball.setx(-370)
        ball.dx*=-1
