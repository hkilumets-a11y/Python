import turtle
turtle.speed(0)

for x in [-300, -150, 0, 150]:
    turtle.penup();
    turtle.goto(x, -100);
    turtle.setheading(0);
    turtle.pendown()
    
    # House Box (Black)
    for _ in range(4): turtle.forward(100); turtle.right(90)
    
    # Door at the bottom (Red)
    turtle.penup();
    turtle.goto(x + 30, -200);
    turtle.setheading(90);
    turtle.pendown()
    turtle.pencolor("red")
    for _ in range(2):
        turtle.forward(40);
        turtle.right(90);
        turtle.forward(40);
        turtle.right(90)
    
    turtle.penup();
    turtle.goto(x, -100);
    turtle.setheading(60);
    turtle.pendown()
    turtle.pencolor("green")
    turtle.forward(100);
    turtle.right(120);
    turtle.forward(100)
    turtle.pencolor("black")

turtle.done()
