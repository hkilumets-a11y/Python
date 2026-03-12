import turtle

 
turtle.speed(0)


turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()


for _ in range(5):
    
    for _ in range(4):
        turtle.forward(200)
        turtle.left(90)
    

turtle.left(72)

turtle.done()